from django.http import HttpResponse



def show_merchandise_data(request, categories, states="AUS"):
    return HttpResponse("This is merchandise. Our categories: \"{0}\", these are the states: \"{1}\"".format(categories, states))

def show_retail_data(request, categories, states="AUS"):
    return HttpResponse("This is retail. Our categories: \"{0}\", these are the states: \"{1}\"".format(categories, states))