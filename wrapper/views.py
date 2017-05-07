"""
The view layer of the API, handle string beautify and stuff
"""
import logging
from django.http import HttpResponse, JsonResponse

from .crocs import cross_origin
import urllib2

logging.basicConfig(filename="wrapper.log", level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@cross_origin
def index(request, url):
    """
    # Index route, only echo the request
    :param request: http request
    :param url: url
    :return: http response
    """
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except Exception as e:
        logger.error('This is bad {}'.format(str(e.reason)))
        return HttpResponse('Not Found REASON:{}, URL:{}'.format(e.reason, url), status=404)
    return HttpResponse(html)

