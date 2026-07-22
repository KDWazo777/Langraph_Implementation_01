import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from app.tools import calculator

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

agent = create_react_agent(
    model=llm,
    tools=[calculator],
    prompt="""
You are an AI assistant.

Whenever the user asks a mathematical question,
ALWAYS use the calculator tool.

Do not perform calculations yourself.
"""
)