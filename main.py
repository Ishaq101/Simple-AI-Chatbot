import asyncio
from typing import AsyncIterable

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain.schema import HumanMessage
from pydantic import BaseModel
from langchain.callbacks import AsyncIteratorCallbackHandler

from src.llms.LLM import model_gemini
from src.agents.LLMAgent import LLMAgent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    content: str



@app.post("/get_aianswer")
async def get_aianswer(message: Message):
    """Endpoint to handle autograder requests."""
    callback = AsyncIteratorCallbackHandler()
    callbacks = [callback]

    llm_agent = LLMAgent(model=model_gemini)
    llm_agent.callback = callback
    llm_agent.callbacks = callbacks

    generator = llm_agent.generate(
        messages=[HumanMessage(content=message.content)]
    )

    return StreamingResponse(generator, media_type="text/event-stream")