from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, Optional

from openai import OpenAI

from .config import get_settings


@dataclass
class CarSearchFilters:
    make: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    max_price: Optional[int] = None
    min_price: Optional[int] = None
    min_year: Optional[int] = None
    max_year: Optional[int] = None


settings = get_settings()

_client: Optional[OpenAI] = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        if not settings.openai_api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set, but LLM is required for the bot"
            )
        _client = OpenAI(api_key=settings.openai_api_key)
    return _client


_TOOLS: list[Dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "search_cars",
            "description": (
                "Extract structured filters for searching cars in the database."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "make": {
                        "type": "string",
                        "description": "Car brand (e.g. BMW, Toyota, Honda).",
                    },
                    "model": {
                        "type": "string",
                        "description": "Car model (e.g. 3 Series, Corolla).",
                    },
                    "color": {
                        "type": "string",
                        "description": "Preferred color in user language.",
                    },
                    "max_price": {
                        "type": "integer",
                        "description": "Maximum price in the same currency as DB (e.g. JPY).",
                    },
                    "min_price": {
                        "type": "integer",
                        "description": "Minimum price in the same currency as DB (e.g. JPY).",
                    },
                    "min_year": {
                        "type": "integer",
                        "description": "Earliest production year.",
                    },
                    "max_year": {
                        "type": "integer",
                        "description": "Latest production year.",
                    },
                },
                "required": [],
            },
        },
    }
]


async def extract_filters_from_query(user_query: str) -> CarSearchFilters:
    """
    Использует Function Calling, чтобы вытащить фильтры поиска из свободного текста.
    """
    client = _get_client()

    completion = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You help to search cars in a database. "
                    "User speaks mostly Russian. Extract only filters, "
                    "do not translate brand/model names."
                ),
            },
            {
                "role": "user",
                "content": user_query,
            },
        ],
        tools=_TOOLS,
        tool_choice={"type": "function", "function": {"name": "search_cars"}},
    )

    message = completion.choices[0].message
    tool_calls = message.tool_calls or []
    if not tool_calls:
        return CarSearchFilters()

    args_raw = tool_calls[0].function.arguments
    try:
        data: Dict[str, Any] = json.loads(args_raw)
    except json.JSONDecodeError:
        return CarSearchFilters()

    return CarSearchFilters(
        make=data.get("make"),
        model=data.get("model"),
        color=data.get("color"),
        max_price=data.get("max_price"),
        min_price=data.get("min_price"),
        min_year=data.get("min_year"),
        max_year=data.get("max_year"),
    )

