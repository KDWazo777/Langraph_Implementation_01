from fastapi import APIRouter, HTTPException

from app.agents.agent import agent
from app.agents.company_agent import company_agent
from app.utils.schemas import TestRequest

router = APIRouter(prefix="/api")

def select_agent(user_input: str):
    user_input = user_input.lower()

    # Routing logic
    if any(op in user_input for op in ["+", "-", "*", "/", "%", "**"]):
        return agent

    return company_agent

@router.post("/test")
async def test(req: TestRequest):

    try:
        agent = select_agent(req.input)
        response = agent.invoke({"messages": [{"role": "user","content": req.input}]})
        return { "success": True,"result": response["messages"][-1].content}

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))