Hosted website: jparkjmc.pythonanywhere.com

**Select Company -> Select Year -> LLM-generated insights + sentiment analysis temporal visualization**

I want to express a **disclaimer** that I did this entire project during the little free time I had while I was on family vacation. I was given this assignment during my family vacation, and it was due before I could come back. While this is evidently not my best work, I'm very proud of what I built given the circumstances.

**Data Handling Tech Stack (files under sec-filings)**

Python - most familiar with for data handling

IPYNB/COLAB - Data wrangling/preprocessing

sec-edgar - recommended library

sec-api.io API & sec-edgar - common API uses for sec filings

huggingface Prosious/FinBERT - model used for sentiment analysis

OpenAI API - specifically used gpt-3.5-turbo

Colab was really good to keep track of progress of the data given that it saves my work in progress in midst of data wrangling, preprocessing, and api calls. OpenAI I used as I'm most familiar with their API.

**Web App Tech stack (all files relevant to deployment)**

Flask for backend

HTML/CSS for frontend

I wanted to deploy a simple web app that can demonstrate the functionality of LLM insights on 10-K filings. I chose to keep the tech stack extremely simple so I can focus more on extracting/preprocessing/LLM inferencing the data, which is the most improtant part.


