from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

app = Flask(__name__)

template = """
Answer the question below.

Here is the conversation history:
{context}

Question: {question}
Answer:
"""

model = OllamaLLM(model='llama3.2')
prompt = ChatPromptTemplate.from_template(template)
chain = LLMChain(prompt=prompt, llm=model)
conversation_history = ""

@app.route("/ask", methods=["POST"])
def ask():
    global conversation_history
    user_input = request.json.get("question")
    context = request.json.get("context", conversation_history)
    result = chain.invoke({"context": context, "question": user_input})
    
    # Update conversation history
    conversation_history += f"\nUser: {user_input}\nAI: {result}"
    
    return jsonify({"response": result, "context": conversation_history})

if __name__ == "__main__":
    app.run(port=5000)
