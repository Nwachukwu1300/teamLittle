import json
import alternate_response
import re

def loader(file):
    with open(file) as response:
        return json.load(response)

response_data = loader("response.json")


def get_response(prompt):
    split_input = re.split(r'\s+|[,;?!.#$%ˆ&*()+=><@-]\s*', prompt.lower())


while True:
    user_input = input("You: ")
    print("Little: ", get_response(user_input))
