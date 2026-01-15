from fastapi import FastAPI
import os

app = FastAPI()

AGENT_NAME = os.getenv("AGENT_NAME", "law-purple-agent")
MODEL = os.getenv("MODEL", "DeepSeek V3.2")

@app.get("/.well-known/agent-card.json")
def agent_card():
    return {
        "name": AGENT_NAME,
        "description": "A minimal Purple Agent that serves an A2A agent-card and placeholder endpoints.",
        "model": MODEL,
        "endpoints": {"health": "/health", "echo": "/echo"},
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/echo")
def echo(payload: dict):
    return {"received": payload}
