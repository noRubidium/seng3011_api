"""
The view layer of the API, handle string beautify and stuff
"""
import json
from django.http import JsonResponse
from .crocs import cross_origin

import urllib2
# import re
from newspaper import Article
from bs4 import BeautifulSoup
import base64
import datetime

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

from .utils import news_urls_data, individual_news_data

@cross_origin
def get_company_news(request, company):
    """
    get the request, return news items for the company
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of news related to company
    """

    news = dict()
    list_of_news = list()

    url = 'http://www.afr.com/research-tools/{}/share-prices/shares-news'.format(company)

    conn = urllib2.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html)
    stories = soup.find_all('div', class_='story__wof')

    for story in stories:
        url = story.find('a').get('href',None)
        if url in news_urls_data.keys():
            list_of_news.append(news_urls_data[url])
        else:
            headline = story.find('a').contents[0]
            summary = story.find('p').contents[0]

            dateobj = datetime.datetime.strptime(story.find('time').contents[0], '%d/%m/%Y')
            date = datetime.date.strftime(dateobj, '%Y-%m-%d')

            news_dict = {'headline': headline, 'date': date, 'summary': summary, 'url': url}
            list_of_news.append(news_dict)
            news_urls_data[url] = news_dict

    news['data'] = list_of_news

    return JsonResponse(news)


@cross_origin
def get_news_item_data(request, encodedurl):
    """
    get the request, return data for the news article
    :param request: http request
    :param news_url: url of the news article
    :return: JSON of news article data
    """
    url = base64.b64decode(encodedurl)
    news_data = dict()

    if url in individual_news_data.keys():
        news_data = individual_news_data[url]
    else:
        conn = urllib2.urlopen(url)
        html = conn.read()

        soup = BeautifulSoup(html)

        involved_companies = soup.find_all('li', class_='topic-labels__item')
        involved_codes = list()

        for comp in involved_companies:
            code = comp.find('a').contents[0]
            involved_codes.append(code)

        news_data['involved_companies'] = involved_codes

        a = Article(url)
        a.download()
        a.parse()
        a.nlp()

        news_data['headline'] = a.title
        news_data['date'] = a.publish_date
        news_data['summary'] = a.summary
        news_data['text'] = a.text

        natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='e453aa13-66ca-4349-8449-132275a299aa',
        password='F0hlP1SmBDch')

        response = natural_language_understanding.analyze(
        url=url,
        features=[features.Sentiment(), features.Emotion()])

        news_data['sentiment'] = response['sentiment']['document']
        news_data['emotion'] = response['emotion']['document']['emotion']

        individual_news_data[url] = news_data

    return JsonResponse(news_data)
