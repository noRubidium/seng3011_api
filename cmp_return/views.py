"""
The view layer of the API, handle string beautify and stuff
"""
import logging
import time
import urllib2
from datetime import datetime
from django.http import HttpResponse, JsonResponse

from .crocs import cross_origin

logging.basicConfig(filename="wrapper.log", level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

cache = dict()

@cross_origin
def index(request, cmp):
    """
    # Index route, only echo the request
    :param request: http request
    :param cmp: cmp
    :return: http response
    """
    if cmp in cache:
        return HttpResponse(cache[cmp])
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=909666000&period2={}&interval=1d&events=history&crumb=ujzI9fPyQBk'.format(cmp, int(time.time()))
    try:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', 'B=3pbbr0hcht280&b=3&s=pp'))
        response = opener.open(url)
        html = response.read()
        cache[cmp] = html
    except Exception as e:
        logger.error('This is bad {} haha'.format(str(e.reason)))
        return HttpResponse('Not Found REASON:{}, URL:{}'.format(e.reason, url), status=404)
    return HttpResponse(html)

def filter_data_by_date(html, starting_date, ending_date):
    result = ''
    for line in html.split('\n'):
        pieces = line.split(',')
        if not pieces[0] == 'Date':
            try:
                date = datetime.strptime(pieces[0], '%Y-%m-%d')
            except:
                continue
            if starting_date > date:
                continue
            if ending_date < date:
                break
        result += line + '\n'
    return result

@cross_origin
def filtered(request, cmp, start, end):
    """
    # Index route, only echo the request
    :param request: http request
    :param cmp: cmp
    :return: http response
    """
    sd = datetime.strptime(start, '%Y-%m-%d')
    ed = datetime.strptime(end, '%Y-%m-%d')
    if cmp in cache:
        return HttpResponse(filter_data_by_date(cache[cmp], sd, ed))
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=909666000&period2={}&interval=1d&events=history&crumb=ujzI9fPyQBk'.format(cmp, int(time.time()))
    try:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', 'B=3pbbr0hcht280&b=3&s=pp'))
        response = opener.open(url)
        html = response.read()
        cache[cmp] = html
    except Exception as e:
        logger.error('This is bad {} haha'.format(str(e.reason)))
        return HttpResponse('Not Found REASON:{}, URL:{}'.format(e.reason, url), status=404)
    return HttpResponse(filter_data_by_date(html, sd, ed))
