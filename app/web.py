"""
Lightweight HTTP server for Render Free.

Render Free requires the service to bind to an HTTP port; otherwise the process
is killed. The Telegram bot itself stays on long-polling — this server exists
purely to satisfy the platform health check.
"""

from fastapi import FastAPI

app = FastAPI(title="AskBot health server")


@app.get("/")
async def root() -> dict:
    return {"status": "ok"}


@app.get("/health")
async def health() -> dict:
    return {"status": "healthy"}
