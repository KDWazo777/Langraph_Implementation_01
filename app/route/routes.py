import json
from fastapi import APIRouter, HTTPException
from langchain_core.messages import AIMessage

from app.agents.agent import agent
from app.agents.company_agent import company_agent
from app.utils.schemas import TestRequest

router = APIRouter(prefix="/api")

def select_agent(user_input: str):
    user_input = user_input.lower()
    if any(op in user_input for op in ["+", "-", "*", "/", "%", "**"]):
        return agent
    return company_agent

@router.post("/test")
async def test(req: TestRequest):
    try:
        selected_agent = select_agent(req.input)
        response = selected_agent.invoke({"messages": [{"role": "user", "content": req.input}]})
        
        messages = response.get("messages", [])
        if not messages:
            raise HTTPException(status_code=500, detail="Agent returned an empty message state.")
            
        ai_messages = [msg for msg in messages if isinstance(msg, AIMessage) or getattr(msg, "type", None) == "ai"]
        final_message = ai_messages[-1] if ai_messages else messages[-1]
        
        content = final_message.content

# Handle different content formats
        if isinstance(content, list):
            if len(content) > 0 and isinstance(content[0], dict) and "text" in content[0]:
                content = content[0]["text"]
            elif len(content) > 0 and isinstance(content[0], str):
                content = content[0]

        elif isinstance(content, dict):
            if "text" in content:
                content = content["text"]
            elif "result" in content:
                content = content["result"]

        return {"success": True, "result": str(content)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
