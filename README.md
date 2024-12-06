Pirate Chatbot Using Gemini API
This is a fun Python project where you will create a pirate-themed chatbot that responds to user input in pirate speak, using Google's Gemini API.

The chatbot generates responses based on the Gemini-1.5-flash model from Google and is designed to be interactive. It allows users to chat and get creative pirate-style responses!

Prerequisites
Before you start, you will need to:

Create a Google Cloud Account and set up access to the Gemini API.
Install the required libraries for Python.
Set up your API key and store it securely in a .env file.
Setting Up Your Project
1. Create a Gemini API Key:
To use the Gemini API, you need to create an API key from Google Cloud. Follow these steps to create your API key:

Go to the Google Cloud Console.
Create a new project.
Go to APIs & Services → Credentials.
Click Create Credentials → API Key.
Copy the API Key provided and store it securely. You will use this key in your project.
2. Set Up Your Environment:
Install Python (preferably Python 3.x).
Install the required Python packages (explained below).
3. Create the .env File:
Your API Key should not be hard-coded into the script for security reasons. Instead, we will use a .env file to store sensitive information like the API key. Here’s how you set it up:

In the root folder of the project, create a file named .env.
Add the following line to the .env file:
env
Copy code
API_KEY=your-gemini-api-key-here
Replace your-gemini-api-key-here with the API key you created earlier.

4. Install Dependencies:
You will need to install the following Python libraries:

google-generativeai: The library to access the Gemini API.
python-dotenv: To load environment variables from the .env file.
To install the required libraries, open a terminal and run:

bash
Copy code
pip install google-generativeai python-dotenv
Alternatively, you can create a requirements.txt (see below) and use the following command to install everything:

bash
Copy code
pip install -r requirements.txt
5. Run the Project:
Once you've installed the dependencies and set up the .env file, you can start the chatbot by running:
bash
Copy code
python gem.py
This will start an interactive loop where you can type your messages, and the chatbot will respond in pirate speak.

6. Exit the Chat:
To exit the chat, simply type exit and hit Enter.
