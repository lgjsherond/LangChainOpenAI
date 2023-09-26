import openai

openai.api_key = "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"

workmodel=openai.Workmodel.load("YOUR_WORKMODEL_ID")
poem=workmodel.generate(prompt="Write a poem about a fish")
print(poem.text)