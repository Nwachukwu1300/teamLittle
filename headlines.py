import requests
API_KEY = "1a210072c96c49c59719a370d0fbd69b"

specific_country = "us"
specific_word = "apple"
specific_publisher = "techcrunch"
specific_sorting = "popularity"

british_headlines_url = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=" + API_KEY

specific_word_url = "https://newsapi.org/v2/everything?q=" + specific_word +\
                    "&from=2022-11-15&to=2022-11-15&sortBy=popularity&language=en&apiKey=" + API_KEY

specific_publisher_url = "https://newsapi.org/v2/everything?domains=" + specific_publisher +".com&apiKey=" + API_KEY

specific_country_url = "https://newsapi.org/v2/top-headlines?country=" + specific_country +"&apiKey=" + API_KEY

custom_url = "https://newsapi.org/v2/everything?domains="+specific_publisher+".com&q=" + specific_word +\
                    "&from=2022-11-15&to=2022-11-15&sortBy="+specific_sorting+"&apiKey=" + API_KEY


custom_response = requests.get(custom_url)
custom_data = custom_response.json()
british_response = requests.get(british_headlines_url)
british_data = british_response.json()
country_response = requests.get(specific_country_url)
country_data = country_response.json()
specific_response = requests.get(specific_word_url)
specific_data = specific_response.json()
publisher_response = requests.get(specific_publisher_url)
publisher_data = publisher_response.json()


def custom():
    return custom_data.get("articles")


def specific_words():
    return specific_data.get("articles")


def publisher():
    return publisher_data.get("articles")


def articles_british():
    return british_data.get("articles")


def top_ten_british():
    print("TOP 10 HEADLINES IN ENGLAND")
    for i in range(10):
        top = british_data["articles"][i]["title"]
        print(str(i+1),".", top,"\n")
    return "\n"


def top_ten_country():
    print(f"TOP 10 HEADLINES IN THE {specific_country.upper()}")
    for c in range(10):
        top = country_data["articles"][c]["title"]
        print(str(c+1),".", top,"\n")
    return "\n"


def titles_british():
    for t in articles_british():
        print(t["title"],"\n")
    return "\n"


def titles_specific():
    for w in specific_words():
        print(w["title"],"\n")
    return "\n"


def titles_publisher():
    for p in publisher():
        print(p["title"],"\n")
    return "\n"


def titles_custom():
    for cu in custom():
        print(cu["title"],"\n")
    return "\n"
