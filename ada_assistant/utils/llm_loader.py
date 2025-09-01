import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise RuntimeError("Missing MISTRAL_API_KEY. Add it to your .env file.")

llm = ChatMistralAI(
    model="mistral-medium-latest",
    api_key=api_key
)
