"""
The view layer of the API, handle string beautify and stuff
"""
import json
from django.http import JsonResponse
from .crocs import cross_origin

import urllib2
import re
from newspaper import Article
from bs4 import BeautifulSoup

import threading
from Queue import Queue

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

news = {}

@cross_origin
def get_company_news(request, company):
    """
    get the request, return retail data
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of news related to company
    """

    natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='e453aa13-66ca-4349-8449-132275a299aa',
    password='F0hlP1SmBDch')

    news = {}
    news_urls = []

    url = 'http://www.afr.com/research-tools/{}/share-prices/shares-news'.format(company)

    conn = urllib2.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html)
    stories = soup.find_all('div', class_='story__wof')

    counter = 0
    for story in stories:
        headline = story.find('a').contents[0]
        summary = story.find('p').contents[0]
        date = story.find('time').contents[0]
        url = story.find('a').get('href',None)

        response = natural_language_understanding.analyze(
        url=url,
        features=[features.Sentiment(), features.Emotion()])

        print response

        news_dict = {'headline': headline, 'date': date, 'summary': summary, 'url': url, 'sentiment': response['sentiment']['document'], 'emotion': response['emotion']['document']['emotion']}
        news[counter] = news_dict
        counter += 1

    return JsonResponse(news)
