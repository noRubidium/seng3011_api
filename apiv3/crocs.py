def cross_origin(func):
    def inner(*args, **kargs):
        response = func(*args, **kargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    return inner
