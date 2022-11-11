import json
import alternate_response
import re
import random


with open("response.json") as responses:
    data = json.load(responses)


def greet_response(user_inputs):
    score_list = []

    for response in data:
        required_words = response["required_words"]
        response_score, required_score = 0, 0

        if required_words:
            for word in user_inputs:
                if word in required_words:
                    required_score = required_score + 1

        if required_score == len(required_words):
            for word in user_inputs:
                if word in response["input"]:
                    response_score = response_score + 1

        score_list.append(response_score)
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if best_response != 0:
        return random.choice(data[response_index]["response"])
    else:
        return alternate_response.alternate_response()


user_name = input("What should I call you? : ")
while True:
    user_input = input(f"{user_name}: ")
    lower_input = user_input.lower()
    final_input = re.split(r'\s+|[,ˆ&*()_}{";?!@#$%-]\s*', lower_input)
    print("Little: ", greet_response(final_input))


