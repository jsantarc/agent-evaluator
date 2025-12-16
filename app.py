
import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load env vars (optional in App Runner, but fine locally)
load_dotenv()

# LLM (reads OPENAI_API_KEY from env automatically)
llm = ChatOpenAI(model="gpt-4o-mini")

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

def chat(message, history):
    return conversation.predict(input=message)

demo = gr.ChatInterface(
    fn=chat,
    title="My AI Chatbot",
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    demo.launch(server_name="0.0.0.0", server_port=port)
