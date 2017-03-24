from django.http import HttpResponse

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point.")


def showMerchandiseData(request, categories, states="AUS"):
    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response

def showRetailData(request, categories, states="AUS"):
    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response