from bs4 import BeautifulSoup
import requests
import re
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from heapq import nlargest
nltk.download('punkt')
nltk.download('stopwords')


url_2 = 'https://en.wikipedia.org/wiki/Double-Cross_System'


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_soup = soup.find_all('p')
    return article_soup

def get_article_content(article_soup):
    content = []
    for item in article_soup:
        content.append(item.get_text())
    #remove shorter sentences to keep headers and non article related paragraphs out of the analysis
    no_short_paras = []
    for sentence in content:
        if len(sentence) > 50:
            no_short_paras.append(sentence)
    article_string = ' '.join(no_short_paras)
    return article_string

def get_word_freq(content):
   ps = PorterStemmer()
   stop_words = nltk.corpus.stopwords.words('english')
   content=re.sub("(\\W|\\d)"," ",content)
   content = content.strip()
   tokens = word_tokenize(content)
   word_frequencies = {}
   for tok in tokens:
      tok = ps.stem(tok)
      if tok in stop_words:
         continue
      if tok not in word_frequencies.keys():
         word_frequencies[tok] = 1
      else:
         word_frequencies[tok] += 1
   return word_frequencies

def get_sentence_scores(sentences, freq_table) -> dict:
    sentence_value = dict()
    for sentence in sentences:
        #get sentence word count
        word_count_in_sentence = (len(word_tokenize(sentence)))
        #set initial word count for sentence minus stop words
        word_count_in_sentence_except_stop_words = 0
        #create sentence value table
        for word_val in freq_table:
            if word_val in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence in sentence_value:
                    sentence_value[sentence] += freq_table[word_val]
                else:
                    sentence_value[sentence] = freq_table[word_val]

        if sentence in sentence_value:
            sentence_value[sentence] = sentence_value[sentence] / word_count_in_sentence_except_stop_words

    return sentence_value

def get_final_summary(sentence_scores, theshold, combined):
    select_length = int(len(sentence_scores)*theshold)
    if select_length > 10:
        select_length = 10
    if combined == True:
        select_length = 15
    summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

    final_summary = ' '.join(summary)

    return final_summary

def get_article_summary_from_url(url, theshold):
    article_soup = get_soup(url)

    content_text = get_article_content(article_soup)

    word_freq = get_word_freq(content_text)

    sentence_tokens = sent_tokenize(content_text)

    sentence_scores = get_sentence_scores(sentence_tokens, word_freq)

    summary = get_final_summary(sentence_scores, theshold, False)
    return summary

def get_article_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_body = soup.find_all('p')
    article_links = []
    for item in article_body:
        children = item.findChildren('a')
        for child in children:
            article_links.append(child['href'])
    article_links = article_links[:3]
    new_links = []
    for link in article_links:
        new_links.append('https://en.wikipedia.org' + link)
    new_links.append(url)
    return new_links

def get_linked_article_summaries(url):
    link_list = get_article_links(url)
    summaries = []
    for article_url in link_list:
        summary = get_article_summary_from_url(article_url, 0.2)
        summaries.append(summary)
        print(f'\n SUMMARY for {article_url}: \n{ summary } \n\n\n')
    combined_summary = get_multiple_article_summary(link_list, 0.4)
    print(f'\n COMBINED ARTICLE SUMMARY: \n{ combined_summary } \n\n\n')


def get_multiple_article_summary(url_list, threshold):
    big_ole_soup = []

    for url in url_list:
        url_soup = get_soup(url)
        contents = get_article_content(url_soup)
        big_ole_soup.append(contents)

    content_text = ' '.join(big_ole_soup)

    word_freq = get_word_freq(content_text)

    sentence_tokens = sent_tokenize(content_text)

    sentence_scores = get_sentence_scores(sentence_tokens, word_freq)

    summary = get_final_summary(sentence_scores, threshold, True)

    return summary


get_linked_article_summaries(url_2)