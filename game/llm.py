import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

user_dir = os.path.expanduser("~")
env_path = os.path.join(user_dir, '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def generate_structured_response(model: str, input: str, schema: BaseModel, instructions: str = None):
    response = client.responses.create(
        model=model,
        input=input,
        instructions=instructions,
        text={"format": {"type": "json_schema", "name": "BidResponse", "schema": schema.model_json_schema()}}
    )
    return response.output[0].content[0].text


class Response(BaseModel):
    class Config:
        extra = "forbid" # or "allow" or "ignore"
        allow_inf_nan = False
        # https://docs.pydantic.dev/1.10/usage/model_config/

