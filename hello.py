import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

# Load the workmodel that you want to finetune
workmodel = openai.Workmodel.load("YOUR_WORKMODEL_ID")

# Create a training dataset
training_dataset = [
    {
        "input": "This is a prompt.",
        "output": "This is a response."
    },
    {
        "input": "This is another prompt.",
        "output": "This is another response."
    }
]

# Finetune the workmodel
workmodel.fine_tune(training_dataset)

# Save the finetuned workmodel
workmodel.save("YOUR_FINETUNED_WORKMODEL_ID")