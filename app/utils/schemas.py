from pydantic import BaseModel

class TestRequest(BaseModel):
    input: str