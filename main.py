# Importing json, random and nltk
# The first video I watched for the project: https://www.youtube.com/watch?v=1lwddP0KUEg&t=1523s
# From the video I knew that the chatbot would need the nltk module
import json
import random
import nltk

# Initialising the json response file to the "data" variable
with open("response.json") as responses:
    data = json.load(responses)


# A function that returns a random string from the dictionary of responses the chatbot would give if the
# user's message doesn't make sense
def alternate_response():
    # The list of strings the program can choose from
    alternates = [
        "My apologies I didn't catch that.",
        "I would appreciate if you could be more descriptive.",
        "Please try asking another question, I can't yet respond to that one.",
        "It seems like you wrote something that I don't fully grasp.",
        "Would you mind rephrasing it for me?"
    ]
    final_response = random.randrange(len(alternates))
    return alternates[final_response]


# I got the idea of counting the number of times a certain word appears in the input and scoring them to
# decide the appropriate response from: https://www.youtube.com/watch?v=azP_d7SiRDg&list=LL&index=3&t=495s the youtube
# video also had an influence in my "greet_response" function

def greet_response(user_inputs):
    # An initially empty list of the scores that would later be appended
    listed_scores = []

    # A loop that goes through the JSON file
    for response in data:
        # The required words variable that got assigned to the required_words key in the data dictionary
        required_words = response["required_words"]
        response_score, required_score = 0, 0

        # To make sure the required words are more than zero
        if len(required_words) > 0:
            for word in user_inputs:
                if word in required_words:
                    # Appending the required words score by 1
                    required_score = required_score + 1

        # To check whether the required words score is equal to the length of required words
        if required_score == len(required_words):
            for word in user_inputs:
                if word in response["input"]:
                    # Appending the response words score by 1
                    response_score = response_score + 1

        # Appending the response scores to the initial empty list
        listed_scores.append(response_score)
    # Collecting the best response which would be the maximum figure in the listed scores
    best_response = max(listed_scores)
    # Getting the index of the best response variable
    response_index = listed_scores.index(best_response)

    # Condition to check if there was any response the chatbot could understand.
    if best_response != 0:
        # Returns a random choice for the program to use to respond
        return random.choice(data[response_index]["response"])
    else:
        # Calls the alternate_response function
        return alternate_response()


# First thing the users see when they run the program which shows Little's ability to tell the news
print("Hello my name is Little.\nI am a chatbot that can tell you the news of any country in the world, in any category"
      ", for any specific publisher you want, or news about a particular story you want.\n"
      "If you would like to leave just type 'exit.'")
user_name = input("What should I call you? : ")
# A while loop that runs forever
while 1:
    # The variable that stores the user input and
    user_input = input(f"{user_name}: ")
    # Converts the user's input to lower case
    lower_input = user_input.lower()
    # If the user types "exit" or "end" in the terminal then the code would break
    if lower_input == "exit" or lower_input == "end":
        break
    # Tokenizes the lower cased to make it easier for the bot to understand
    final_input = nltk.word_tokenize(lower_input)
    # Prints "little:" to make the user easily know what Little(the chatbot) has to say
    print("Little: ", greet_response(final_input))
