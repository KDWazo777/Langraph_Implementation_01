import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from app.tools.Cal_tool import calculator, no_result

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

agent = create_react_agent(
    model=llm,
    tools=[calculator, no_result],
    prompt=
"""
Whenever the user asks a mathematical question,
Always use the calculator tool.

Do not perform calculations yourself.
"""
)

print(agent.get_graph().draw_ascii())