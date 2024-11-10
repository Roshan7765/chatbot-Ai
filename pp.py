from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM

app = Flask(__name__)
model = OllamaLLM(model="llama3.2")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    context = data.get('context', '')
    question = data.get('question', '')
    
    response = model.invoke(input=f"Context: {context}\nQuestion: {question}")
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
