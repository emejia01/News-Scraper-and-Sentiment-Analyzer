# News-Scraper-and-Sentiment-Analyzer

This repository contains the Python code that is able to 
extract the textual data from the URL of a news article 
webpage (Currently works with CNN, MSNBC/NBC News, The Washington Post,
 and Fox News). After extracting the data, the text is then 
 analyzed against a list of positive and negative sentiment 
 words to determine whether the narrative of the article is 
 positive or negative.

## Necessary Installations

The necessary packages: 

* BeautifulSoup4

* Requests

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages.

```bash
pip install Requests
```

```bash
pip install BeautifulSoup4
```

## Usage/How it works

When the program is executed, the user will be prompted to 
enter the URL of the news article that is to be analyzed; 
The program currently works with CNN, MSNBC/NBC News, 
The Washington Post, and Fox News.

After the URL is entered, a request is made to the URL using 
the Requests package. After the request is made, the program 
proceeds to parse the content of the requested page using 
BeautifulSoup. The program proceeds to extract the textual 
data from the page using the corresponding HTML tags 
(The tags used depend on the site that is requested). 
The text is put into a list, where each word is its own 
separate item of the list.

Each item of the resulting list of words is then analyzed 
against a list of Positive and Negative Sentiment words 
(These are words that relate to a positive or negative feeling/bias). 
If a word in the list matches a sentiment word, the 
triggered word is put into a positive or negative list. After 
all the words in the list are iterated through, the 
negative count is compared with the positive count. 


The list of triggered positive and negative words 
are returned. The program also returns whether the article 
is generally positive or negative 
(Based on the ratio of Positive to Negative words).

* CURRENTLY WORKING ON MORE EFFICIENT UPDATE WITH GUI. COMING SOON! *

## License

[MIT](https://choosealicense.com/licenses/mit/)

Positive and Negative Sentiment Words Obtained by:

* Minqing Hu and Bing Liu. "Mining and Summarizing Customer 
Reviews." Proceedings of the ACM SIGKDD International 
Conference on Knowledge Discovery and Data Mining (KDD-2004), 
Aug 22-25, 2004, Seattle, Washington, USA
