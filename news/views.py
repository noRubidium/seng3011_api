"""
The view layer of the API, handle string beautify and stuff
"""
import json
from django.http import HttpResponse, JsonResponse
from .crocs import cross_origin

import urllib2
from newspaper import Article

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

    from bs4 import BeautifulSoup
    url = 'http://www.afr.com/research-tools/{}/share-prices/shares-news'.format(company)

    conn = urllib2.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html)
    links = soup.find_all('a', href=re.compile('^http://www.afr.com/Page/Uuid/*')).get('href',None)

    for link in links:
    	if link is not None:
            news_urls.append(link)

    counter = 0

    for news_url in news_urls:
        a = Article(news_url)
        news_dict = {'headline': a.title, 'date': a.publish_date, 'summary': a.summary, 'image': a.top_image}
        news[str(counter)] =  news_dict
        counter += 1

    return JsonResponse(news)
