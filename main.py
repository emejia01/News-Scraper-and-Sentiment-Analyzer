import requests
import text_functions
from bs4 import BeautifulSoup


page_url = input("Enter article URL: ")
site = text_functions.getSite(page_url)

while site == -1:
    page_url = input("INVALID URL or UNSUPPORTED SITE ENTERED. Please enter a valid URL: ")
    site = text_functions.getSite(page_url)

page_url = requests.get(page_url)
soup = BeautifulSoup(page_url.content, 'html.parser')

article_text = text_functions.getText(site, soup)

# Unpack Positive and Negative list from function
positive_words, negative_words = text_functions.p_and_n_words(article_text)

print('\n{} Positive Words Found: \n{}'.format(len(positive_words), positive_words))
print('\n{} Negative Words Found: \n{}\n'.format(len(negative_words), negative_words))

# Calculating Percentage of Positive and Negative words
percent_positive = len(positive_words) / (len(positive_words) + len(negative_words))
percent_positive *= 100
percent_negative = 100 - percent_positive


if percent_positive > percent_negative:
    print("ANALYSIS: The article has a POSITIVE narrative")
elif percent_negative > percent_positive:
    print("ANALYSIS: The article has a NEGATIVE narrative")
else:
    print("ANALYSIS: Too close to call either positive or negative.")