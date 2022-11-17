import requests

specific_word = "apple"
specific_publisher = "techcrunch"

british_headlines_url = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=1a210072c96c49c59719a370d0fbd69b"

specific_word_url = "https://newsapi.org/v2/everything?q="+specific_word+\
                    "&from=2022-11-15&to=2022-11-15&sortBy=popularity&apiKey=1a210072c96c49c59719a370d0fbd69b"

specific_publisher_url = "https://newsapi.org/v2/everything?domains="+specific_publisher+\
                         ".com&apiKey=1a210072c96c49c59719a370d0fbd69b"


response = requests.get(british_headlines_url)
data = response.json()
specific_response = requests.get(specific_word_url)
specific_data = specific_response.json()
publisher_response = requests.get(specific_publisher_url)
publisher_data = publisher_response.json()


def specific_words():
    return specific_data.get("articles")


def publisher():
    return publisher_data.get("articles")


def articles_british():
    return data.get("articles")


def top_ten_british():
    print("TOP 10 HEADLINES IN ENGLAND")
    for i in range(10):
        top = data["articles"][i]["title"]
        print(str(i+1),".", top)
    return


def titles_british():
    for t in articles_british():
        print(t["title"])


def titles_specific():
    for s in specific_words():
        print(s["title"])


def titles_publisher():
    for p in publisher():
        print(p["title"])

"""
print(titles_specific())
print(articles_british())
print(top_ten_british())
print(titles_british())
"""
print(titles_publisher())

