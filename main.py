# Importing json, random and nltk
import json
import random
import nltk

with open("response.json") as responses:
    data = json.load(responses)


def alternate_response():
    alternates = [
        "My apologies I didn't catch that.",
        "I would appreciate if you could be more descriptive.",
        "Please try asking another question, I can't yet respond to that one.",
        "It seems like you wrote something that I don't fully grasp.",
        "Would you mind rephrasing it for me?"
    ]
    final_response = random.randrange(len(alternates))
    return alternates[final_response]


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
        return alternate_response()


print("Hello my name is little, I am a chatbot that can tell you the news of any country in the world, in any category"
      ", for any specific publisher you want, or news about a particular story you want.")
user_name = input("What should I call you? : ")
while True:
    user_input = input(f"{user_name}: ")
    lower_input = user_input.lower()
    final_input = nltk.word_tokenize(lower_input)
    print("Little: ", greet_response(final_input))
