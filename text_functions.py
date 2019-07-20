# Function returns the name of site; Used to know which HTML tags to use for text extraction
def getSite(page_url):
    if 'www.cnn.com' in page_url:
        return 'cnn'
    elif 'www.foxnews.com' in page_url:
        return 'fox'
    elif 'www.washingtonpost.com' in page_url:
        return 'WaPo'
    elif 'www.nbcnews.com' in page_url:
        return 'nbc'
    else:
        return -1

# Functions that check if word is Positive or Negative; Checks against Positive and Negative Word files
def isPositive(word):
    with open('Positive_Sentiment_Words.txt', 'r') as f:
        for line in f:
            if line.strip() == word:
                return True
        return False

def isNegative(word):
    with open('Negative_Sentiment_Words.txt', 'r') as f:
        for line in f:
            if line.strip() == word:
                return True
        return False

# Function returns a list of words of the article text
def getText(site, soup):
    if site == 'cnn':
        body = soup.find(id= 'body-text')
        text = body.find_all(class_='zn-body__paragraph')
    elif site == 'fox':
        text = soup.find_all(class_='article-body')
    elif site == 'WaPo':
        text = soup.find_all(class_= 'paywall')
    elif site == 'nbc':
        text = soup.find_all(class_='bodyContent___1eruQ')
    else:
        return -1
    full_text = ''
    for i in text:
        full_text += i.get_text() + ' '

    return full_text.split()

# Function returns a tuple of the positive and negative words found in the text
def p_and_n_words(article_text):
    p_words = []
    neg_words = []
    for word in article_text:
        if isPositive(word.lower()):
            p_words.append(word.lower())
            continue
        elif isNegative(word.lower()):
            neg_words.append(word.lower())
            continue
    return p_words, neg_words

