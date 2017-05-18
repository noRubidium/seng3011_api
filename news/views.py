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

@cross_origin
def get_company_news(request, company):
    """
    get the request, return retail data
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of news related to company
    """

    news = {}
    news_urls = []

    url = 'http://www.afr.com/research-tools/{}/share-prices/shares-news'.format(company)

    conn = urllib2.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html)
    links = soup.find_all('a', href=re.compile('^http://www.afr.com/Page/Uuid/*'))

    for tag in links:
        link = tag.get('href',None)
    	if link is not None:
            news_urls.append(link)

    counter = 0
    for news_url in news_urls:
        a = Article(news_url)
        a.download()
        a.parse()
        a.nlp()
        news_dict = {'headline': a.title, 'date': a.publish_date, 'summary': a.summary, 'image': a.top_image}
        news[counter] =  news_dict
        counter += 1

    # print news

    return JsonResponse(news)
