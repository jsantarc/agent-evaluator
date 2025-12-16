from dotenv import load_dotenv
import os
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

  # Load the .env file FIRST, before trying to get variables

load_dotenv() 
llm = ChatOpenAI(model="gpt-4o-mini")  # Create an instance of the OpenAI chat model
memory = ConversationBufferMemory()  # Create memory object to remember conversation history
conversation = ConversationChain(llm=llm, memory=memory)


def chat(message, history):  # Define the chat function that handles each message
    response = conversation.predict(input=message)  # Send message to the model and get response
    return response  # Return the response to display in the chat interface

demo = gr.ChatInterface(  # Create the Gradio chat interface
    fn=chat,  # Use our chat function to handle messages
    title="My AI Chatbot"  # Set the title shown at the top of the interface
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
