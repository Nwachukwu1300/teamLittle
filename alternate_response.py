import random


def alternate_response():
    alternates = [
        "My apologies I didn't catch that.",
        "I would appreciate if you could be more descriptive.",
        "Please try asking another question if I can't yet respond to that one.",
        "It seems like you wrote something that I don't fully grasp.",
        "Would you mind rephrasing it for me?"
    ]

    final_response = random.randrange(len(alternates))

    return alternates[final_response]
