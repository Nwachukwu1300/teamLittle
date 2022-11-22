import requests
# The first video that gave me an overview of how to work with news api- https://www.youtube.com/watch?v=TOHnGTYCuII&t=613s
# The website that taught me how to work and document data from the news api website-  https://newsapi.org/docs/endpoints/top-headlines

# Personal API key
API_KEY = "1a210072c96c49c59719a370d0fbd69b"

# Specific country, word, publisher, or sorting for the results of the news
# I had set the initial country to America, the specific word to news about Apple, the specific publisher to
# technocrunch and the specific sorting to popularity
specific_country = "us"
specific_word = "apple"
specific_publisher = "techcrunch"
specific_sorting = "popularity"

# The variable that sores the URL for the british headlines
british_headlines_url = "https://newsapi.org/v2/top-headlines?country=gb&apiKey=" + API_KEY

# The variable that stores the URL for the news relating to any specific word
specific_word_url = "https://newsapi.org/v2/everything?q=" + specific_word + \
                    "&from=2022-11-15&to=2022-11-15&sortBy=popularity&language=en&apiKey=" + API_KEY

# The variable that stores the URL for the news from any specific publisher
specific_publisher_url = "https://newsapi.org/v2/everything?domains=" + specific_publisher + ".com&apiKey=" + API_KEY

# The variable that stores the URL for the news relating to any specific country
specific_country_url = "https://newsapi.org/v2/top-headlines?country=" + specific_country + "&apiKey=" + API_KEY

# The variable that stores the URL for news that would be customized
custom_url = "https://newsapi.org/v2/everything?domains=" + specific_publisher + ".com&q=" + specific_word + \
             "&from=2022-11-15&to=2022-11-15&sortBy=" + specific_sorting + "&apiKey=" + API_KEY

# Variable to store the response from its respective URL
custom_response = requests.get(custom_url)
# Variable to store the data from its respective response variable
custom_data = custom_response.json()

# Variable to store the response from its respective URL
british_response = requests.get(british_headlines_url)
# Variable to store the data from its respective response variable
british_data = british_response.json()

# Variable to store the response from its respective URL
country_response = requests.get(specific_country_url)
# Variable to store the data from its respective response variable
country_data = country_response.json()

# Variable to store the response from its respective URL
specific_response = requests.get(specific_word_url)
# Variable to store the data from its respective response variable
specific_data = specific_response.json()

# Variable to store the response from its respective URL
publisher_response = requests.get(specific_publisher_url)
# Variable to store the data from its respective response variable
publisher_data = publisher_response.json()


# A custom function that gets the articles from its data variable to be used by other functions later in the code
def custom():
    return custom_data.get("articles")


# A specific_words function that gets the articles from its data variable to be used by other functions later in the code
def specific_words():
    return specific_data.get("articles")


# A publisher function that gets the articles from its data variable to be used by other functions later in the code
def publisher():
    return publisher_data.get("articles")


# A british articles function that gets the articles from its data variable to be used by other functions later in the code
def articles_british():
    return british_data.get("articles")


#  A function that prints the top 10 headlines in England I got this idea from: https://www.youtube.com/watch?v=aYE1nRKBx2k&t=572s
def top_ten_british():
    print("TOP 10 HEADLINES IN ENGLAND")
    for i in range(10):
        top = british_data["articles"][i]["title"]
        print(str(i + 1), ".", top, "\n")
    return "\n"

#  A function that prints the top 10 headlines in any country
def top_ten_country():
    print(f"TOP 10 HEADLINES IN THE {specific_country.upper()}")
    for c in range(10):
        top = country_data["articles"][c]["title"]
        print(str(c + 1), ".", top, "\n")
    return "\n"

# A function that prints the title of the headlines in England
def titles_british():
    for t in articles_british():
        print(t["title"], "\n")
    return "\n"

# A function that prints the title of the headlines for news relating to a specific word
def titles_specific():
    for w in specific_words():
        print(w["title"], "\n")
    return "\n"

# A function that prints the title of the headlines for news published from a specific publisher
def titles_publisher():
    for p in publisher():
        print(p["title"], "\n")
    return "\n"

# A function that prints the title of the headlines for news relating to a specific country,sorting, publisher or word.
def titles_custom():
    for cu in custom():
        print(cu["title"], "\n")
    return "\n"
