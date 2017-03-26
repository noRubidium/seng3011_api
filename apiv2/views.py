from django.http import HttpResponse

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


def showMerchandiseData(request, categories, states="AUS"):
    return HttpResponse("This is the API end point v2.")
    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response

def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')
    return HttpResponse("categories: " + categories + " <br>states: " + states + " <br>startDate: " + startDate + " <br>endDate: " + endDate)
    # get start/end date from request
    # init a Merchandise Object
    # put JSON dump of that
    pass  # return JSON response
