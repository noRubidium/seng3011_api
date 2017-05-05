"""
The utility to give cross origin support
"""


def cross_origin(func):
    """
    :param func: a view function return http response
    :return: decorated function
    """
    def inner(*args, **kwargs):
        """
        New function created
        """
        response = func(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    return inner
