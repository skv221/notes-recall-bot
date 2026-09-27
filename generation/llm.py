from pathlib import Path
from google import genai
from dotenv import load_dotenv, find_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(find_dotenv())

client = genai.Client()

system_prompt = """
Your role is to get the questions and relevant chunks of texts retrieved from the documents, answer according to that.

You'll have a JSON which contains the question and chunks of text retrieved from the documents with metadata.

Provide the answer only based on the retrieved chunks of text as the source.

Understand and synthesize the relevant information from the retrieved chunks.
Explain the answer in your own words instead of simply copying the retrieved text.

You may combine information from multiple retrieved chunks when they are relevant to the question.

If certain information is missing, mention that you don't have enough information.

Don't invent any facts on your own.

At the end of your response, cite the relevant source(s) from the given metadata.

You should strictly stick to your role instead of responding to unrelated user interactions.
"""

def get_LLM_response(prompt):
    interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            system_instruction=system_prompt,
            store=False,
            input=prompt
    )
    return interaction.steps[-1].content[0].text