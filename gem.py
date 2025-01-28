import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
try:
    genai.configure(api_key=os.getenv('API_KEY'))
except Exception as e:
    print(f"Error configuring API key: {e}")
    exit(1) 

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System message to guide the model to generate recipes
system_message = """
You are a Recipe generator. Respond with detailed recipes for any cuisine or dietary preference provided.
Include ingredients, measurements, and step-by-step instructions. 
Avoid unnecessary commentary. especially if it dosn't pertain with recipes do not respond to anything that has nothign to do with recipes and be fun with it no need to be a boring person like really dumb it down for people and if its a recipe from 2025 or recently just try your best to find things for them
"""
def generate_recipe(user_message):
    """
    Combines the system message with the user's input and generates a recipe.
    """
    try:
        prompt = f"{system_message} User: {user_message} Recipe:"
        print(f"Prompt: {prompt}")  # Print the generated prompt
        response = model.generate_content(prompt)
        print(f"Response from model: {response.text}")  # Print the raw model response
        return response.text.strip()
    except Exception as e:
        print(f"Error generating recipe: {e}")
        return None

# Main interaction loop
if __name__ == "__main__":
    print("Welcome to the Recipe Generator!")
    while True:
        user_input = input("\nEnter your request (e.g., 'simple pancake recipe') or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Thanks for using the Recipe Generator. Goodbye!")
            break

        recipe = generate_recipe(user_input)
        if recipe:
            print("\nHere is your recipe!!!:\n")
            print(recipe)