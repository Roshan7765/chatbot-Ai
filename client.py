import requests

def handle_conversation():
    context = ""  # Initialize empty context for conversation history
    
    print("Welcome to the AI Chat! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            break
        
        # Update context with user input for conversation history
        context += f"User: {user_input}\n"
        
        # Send context and question to Flask microservice
        response = requests.post("http://localhost:5000/chat", json={"context": context, "question": user_input})
        
        # Get AI response and update context with it
        assistant_response = response.json().get("response", "")
        context += f"AI: {assistant_response}\n"
        
        print("AI:", assistant_response)

if __name__ == "__main__":
    handle_conversation()
