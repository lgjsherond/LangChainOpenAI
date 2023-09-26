import os
import openai
from dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

llm=OpenAI(model_name="text-ada-001")
llm("Tell me a joke")