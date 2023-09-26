import requests
import langchain
from newspaper import Article


# Set the OpenAI API key
OPENAI_API_KEY = "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"

# Scrape the article
article_url = "https://www.example.com/article.html"
response = requests.get(article_url)
html = response.content

# Extract the title and text of the article
article=Article(html)
article.parse()
title = article.title
text = article.text

# Preprocess the text
text = text.replace("\n", "")
text = text.replace("\t", "")

# Generate a summary of the article
summary = langchain.summarize(text, max_tokens=100)

# Print the summary
print(summary)
