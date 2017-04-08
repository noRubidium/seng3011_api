"""
The utility to give cross origin support
"""


def cross_origin(func):
    """
    :param func: a view function return http response
    :return: decorated function
    """
    def inner(*args, **kargs):
        """
        New function created
        """
        response = func(*args, **kargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    return inner
