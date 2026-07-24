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

If there is a Request with Mathametics formulas(+,-,*,/,%,**)

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
But if the question is about Company related(ceo,location)

Request

```json
{
  "input": "who is ceo ?"
}
```

Response

```json
{
    "success": true,
    "result": "The CEO of the company is Salim Aktar."
}
```

At last if question / promt doesnt match the criteria it would gave result like as followed

Request

```json
{
  "input": "who is Managing Director ?"
}
```

Response

```json
{
    "success": true,
    "result": "I am sorry, but I do not have information about who the Managing Director is."
}
```
