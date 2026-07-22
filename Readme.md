# LangGraph + FastAPI + Gemini

A simple AI Agent built using:

- FastAPI
- LangGraph
- LangChain
- Google Gemini
- Tool Calling

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## API

POST `/api/test`

Request

```json
{
    "input":"What is 18*5 ?"
}
```

Response

```json
{
    "success": true,
    "result": "The answer is 90."
}
```
