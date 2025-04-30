import requests  # Import the requests library to make HTTP requests

# Set your model name and host URL for the Ollama server
OLLAMA_MODEL = "deepseek-r1:1.5b"  # The name of the model to use
OLLAMA_HOST = "http://localhost:11434"  # The host URL where the Ollama server is running

# Function to send a prompt to the Ollama server and get a response
def ask_ollama(prompt):
    # Define the API endpoint URL
    url = f"{OLLAMA_HOST}/api/generate"
    
    # Set the headers for the HTTP request
    headers = {"Content-Type": "application/json"}
    
    # Define the payload (data) to send in the POST request
    payload = {
        "model": OLLAMA_MODEL,  # Specify the model to use
        "prompt": prompt,       # The user's input prompt
        "stream": False         # Set to True for streaming responses (not used here)
    }

    # Send a POST request to the Ollama server
    response = requests.post(url, json=payload, headers=headers)
    
    # Check if the response status is OK (200)
    if response.status_code == 200:
        # Return the response content if successful
        return response.json()["response"]
    else:
        # Return an error message if the request failed
        return f"Error {response.status_code}: {response.text}"

# Main program execution starts here
if __name__ == "__main__":
    while True:  # Infinite loop to keep asking for user input
        # Prompt the user for input
        user_prompt = input("Enter your prompt (type '/bye' to exit): ")
        
        # Check if the user wants to exit
        if user_prompt.strip().lower() == "/bye":
            print("Goodbye!")  # Print a goodbye message
            break  # Exit the loop
        
        # Call the ask_ollama function with the user's input and get the response
        reply = ask_ollama(user_prompt)
        
        # Print the response from the Ollama server
        print("\n🧠 Deepseek Response:\n", reply)
