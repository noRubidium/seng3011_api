"""
The view layer of the API, handle string beautify and stuff
"""
import logging
import time
from django.http import HttpResponse, JsonResponse

from .crocs import cross_origin
import urllib2

logging.basicConfig(filename="wrapper.log", level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@cross_origin
def index(request, cmp):
    """
    # Index route, only echo the request
    :param request: http request
    :param cmp: cmp
    :return: http response
    """
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1=909666000&period2={}&interval=1d&events=history&crumb=ujzI9fPyQBk'.format(cmp, int(time.time()))
    try:
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', 'B=3pbbr0hcht280&b=3&s=pp'))
        response = opener.open(url)
        html = response.read()
    except Exception as e:
        logger.error('This is bad {} haha'.format(str(e.reason)))
        return HttpResponse('Not Found REASON:{}, URL:{}'.format(e.reason, url), status=404)
    return HttpResponse(html)
