from fastapi import APIRouter, HTTPException

from app.agent import agent
from app.schemas import TestRequest

router = APIRouter(prefix="/api")


@router.post("/test")
async def test(req: TestRequest):

    try:

        response = agent.invoke({"messages": [{"role": "user","content": req.input}]})

        return { "success": True,"result": response["messages"][-1].content}

    except Exception as e:

        raise HTTPException(status_code=500,detail=str(e))