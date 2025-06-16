import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Welcome to the Gherkin feature generator.\n\n")
print("Please provide a title for the feature. Please input only letters, numbers, '-', and '.' characters.")
title = raw_input("Title: ")
print("Please input your feature description below in natural language.")
text = raw_input("Your input: ")


prompt = "The following input is in natural language. Convert this into a cucumber gherkin syntax .feature file. Do not output anything except this feature file which should be in normal text able to be directly placed in a string in python from the api. Here is the natural language input:"
prompt += text

try:
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
except:
    print("An error occurred while prompting the LLM.")

try:
    f = open("/hellocucumber/features/"+ title + ".feature", "w")
    f.write(output)
    f.close()
except Exception as e:
    print("An error occurred while opening the file. Please check your title and try again.")
    exit()

print("Success! The Gherkin feature file has been created at: /hellocucumber/features")