"""
" Simple D&D Flavor Text Generator
"""

import openai
import pprint

# Please sign up for an OpenAI account, generate an API key and paste it below
# https://platform.openai.com/docs/api-reference/authentication
openai.api_key = "YOUR OPEN AI KEY HERE"

# prompt user for a short adventure topic, i.e. goblin bandits
topic = input("Enter adventure topic: ")

# generate flavor text
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Topic: {topic}\nDungeons and dragons adventure:",
    temperature=0.8,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
)

# we use a pretty printer to make the output a bit easier to read
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(response.choices[0].text)
