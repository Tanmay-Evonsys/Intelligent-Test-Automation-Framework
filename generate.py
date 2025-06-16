import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("\n\nWelcome to the Gherkin feature generator.\n")
print("\033[94mPlease provide a title for the feature. Please input only letters, numbers, '-', and '.' characters.\033[0m")
title = input("Title: ")
print("\033[94m\nPlease input your feature description below in natural language.\033[0m")
text = input("Your input: ")


prompt = "The following input is in natural language. Convert this into a cucumber gherkin syntax .feature file. Do not output anything except this feature file which should be in normal text able to be directly placed in a string in python from the api. Here is the natural language input:"
prompt += text

output = ""

try:
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
except:
    print("\033[91m\nError: An error occurred while prompting the LLM. Please check the API key and make sure you followed all the steps in the README.\033[0m")
    exit()


try:
    f = open("hellocucumber/features/"+ title + ".feature", "w")
    f.write(output)
    f.close()
except Exception as e:
    print("\033[91m\nError: An error occurred while opening the file. Please check your title and try again.\033[0m")
    exit()

print("\033[92m\nSuccess! The Gherkin feature file has been created at: /hellocucumber/features\033[0m")