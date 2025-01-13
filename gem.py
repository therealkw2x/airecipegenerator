import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('API_KEY'))

# Initialize the model (use the "gemini-1.5-flash" model or whichever is appropriate)
model = genai.GenerativeModel("gemini-1.5-flash")

# System message to guide the model to respond in pirate speak
system_message = "You are a Recipe generator. Respond with detailed recipes for any cuisine or dietary preferance provided. Include ingredients, measurements, and step by step instructions. Avoid uneseccary commentary."

# Function to generate responses in pirate speak
def generate_pirate_response(user_message):
    # Combine the system message with the user's input to guide the model's response
    prompt = f"{system_message} User: {user_message} Recipe:"

    # Generate the response using the model
    response = model.generate_content(prompt)

    return response.text

# Example of interacting with the chatbot
if __name__ == "__main__":
    print("Welcome to the Recipe Generator!")
    while True:
        user_input = input("\nEnter your request (e.g., 'vegan lasagna recipe') or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Thanks for using the Recipe Generator. Goodbye!")
            break
        try:
            recipe = generate_recipe(user_input)
            print("\nHere is your recipe:\n")
            print(recipe)
        except Exception as e:
            print("An error occurred:", str(e))
