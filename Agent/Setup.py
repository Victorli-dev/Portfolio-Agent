import os
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic
import streamlit as st

_ENV_PATH = Path(__file__).parent.parent / ".env"


def initialize_kernel() -> dict:
    load_dotenv(_ENV_PATH, override=True)
    api_key = os.getenv("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY")
    model = os.getenv("ANTHROPIC_MODEL") or st.secrets.get("ANTHROPIC_MODEL")
    return {
        "api_key": api_key,
        "model": model,
    }


def create_client() -> Anthropic:
    config = initialize_kernel()
    return Anthropic(api_key=config["api_key"])
