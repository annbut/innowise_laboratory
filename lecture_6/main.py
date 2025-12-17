"""Minimal FastAPI application for Docker healthcheck."""

from __future__ import annotations

from fastapi import FastAPI

# Create FastAPI application instance.
app = FastAPI()


@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    """Return simple status payload for health checking."""
    return {"status": "ok"}
