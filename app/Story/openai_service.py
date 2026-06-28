from openai import OpenAI
from app.core.config import OPENAI_API_KEY, MODEL_NAME
from app.utils.prompt_template import build_prompt

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_story(prompt):

    final_prompt = build_prompt(prompt)

    response = client.responses.create(
        model=MODEL_NAME,
        input=final_prompt
    )

    return response.output_text
