from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

print("OPENAI_API_KEY:", OPENAI_API_KEY)
print("MODEL_NAME:", MODEL_NAME)
