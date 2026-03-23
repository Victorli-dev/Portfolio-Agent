import os
from dotenv import load_dotenv
from anthropic import AsyncAnthropic


def initialize_kernel() -> dict:
    load_dotenv("Setup.env")
    return {
        "api_key": os.environ["ANTHROPIC_API_KEY"],
        "model": os.environ["ANTHROPIC_MODEL"],
    }


def create_client() -> AsyncAnthropic:
    config = initialize_kernel()
    return AsyncAnthropic(api_key=config["api_key"])
