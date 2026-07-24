import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from app.tools.company_tool import company_info

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)

company_agent = create_react_agent(
    model=llm,
    tools=[company_info],
    prompt="""
You are a Company Assistant.
Always use the company_info tool to answer questions
about the company.
Do not make up information.
"""
)