import base64
import datetime
import os
import re
import urllib2
import json
from bs4 import BeautifulSoup
from newspaper import Article
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

import errno

news_urls_data = dict()
individual_news_data = dict()


def get_news(company):
    news = dict()
    filename = './db/news/company/{}.json'.format(company)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    try:
        f = open(filename, 'r')
        news = json.loads(f.read())
        f.close()
    except (IOError, ValueError):
        list_of_news = list()

        url = 'http://www.afr.com/research-tools/{}/share-prices/shares-news'.format(company)

        conn = urllib2.urlopen(url)
        html = conn.read()

        soup = BeautifulSoup(html)
        stories = soup.find_all('div', class_='story__wof')

        for story in stories:
            url = story.find('a').get('href', None)
            if url in news_urls_data.keys():
                list_of_news.append(news_urls_data[url])
            else:
                headline = story.find('a').contents[0]
                summary = story.find('p').contents[0]

                time_string = story.find('time').contents[0]
                matches_date_format = re.match(r'\d+/\d+/\d+', time_string)

                if matches_date_format:
                    dateobj = datetime.datetime.strptime(time_string, '%d/%m/%Y')
                else:
                    dateobj = datetime.datetime.now()

                date = datetime.date.strftime(dateobj, '%Y-%m-%d')

                news_dict = {'headline': headline, 'date': date, 'summary': summary, 'url': url}
                list_of_news.append(news_dict)
                news_urls_data[url] = news_dict

        news['data'] = list_of_news
        f = open(filename, 'w+')
        f.write(json.dumps(news))
        f.close()
    return news


def get_news_detail(encoded_url):
    news_data = dict()

    filename = './db/news/lnk/{}.json'.format(encoded_url)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    try:
        f = open(filename, 'r')
        news_data = json.loads(f.read())
        f.close()
    except (IOError, ValueError):
        url = base64.b64decode(encoded_url)
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
        news_data['date'] = datetime.date.strftime(a.publish_date, '%Y-%m-%d')
        news_data['summary'] = a.summary
        news_data['text'] = a.text
        news_data['image'] = a.top_image

        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2017-02-27',
            username='e453aa13-66ca-4349-8449-132275a299aa',
            password='F0hlP1SmBDch')

        response = natural_language_understanding.analyze(
            url=url,
            features=[features.Sentiment(), features.Emotion()])

        news_data['sentiment'] = response['sentiment']['document']
        news_data['emotion'] = response['emotion']['document']['emotion']

        news_data['url'] = url

        f = open(filename, 'w+')
        f.write(json.dumps(news_data))
        f.close()
    return news_data


def get_summary(company):
    d = get_news(company)

    def get_score(news):
        encoded_url = base64.b64encode(news['url'])
        details = get_news_detail(encoded_url)
        result = dict()
        result['emotion'] = details['emotion']
        result['sentiment'] = details['sentiment']
        return result

    result = {}

    scores = map(get_score, d['data'])
    num_news = len(scores)

    def sum_score(x, y):
        return y['sentiment']['score'] + x

    def sum_emotion(x, y):
        emo = y['emotion']
        for k in emo:
            x[k] = x.get(k, 0) + emo[k]/num_news
        return x

    result['sentiment'] = dict()
    # set positive
    result['sentiment']['positive'] = dict()
    positives = filter(lambda n: n['sentiment']['label'] == 'positive', scores)
    result['sentiment']['positive']['count'] = len(positives)
    result['sentiment']['positive']['total'] = reduce(sum_score, positives, 0) / len(positives)

    # set negative
    result['sentiment']['negative'] = dict()
    negative = filter(lambda n: n['sentiment']['label'] == 'negative', scores)
    result['sentiment']['negative']['count'] = len(negative)
    result['sentiment']['negative']['total'] = reduce(sum_score, negative, 0) / len(negative)

    result['emotion'] = dict()
    reduce(sum_emotion, scores, result['emotion'])
    return result
