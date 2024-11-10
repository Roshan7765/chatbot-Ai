from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

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

def handle_conversation():
    context = ""
    print("AI: Hello! How can I help you today? (Type 'exit' to quit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("AI: Goodbye!")
            break

        result = chain.invoke({"context": context, "question": user_input})

        print("AI:", result)

        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
  