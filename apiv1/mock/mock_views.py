"""
The mocked views
"""
from django.http import HttpResponse


def show_merchandise_data(_, categories, states="AUS"):
    """
    Mock show merch data
    """
    return HttpResponse("This is merchandise. Our categories: \"{0}\", "
                        "these are the states: \"{1}\"".format(categories, states))


def show_retail_data(_, categories, states="AUS"):
    """
    mock show retail data
    """
    return HttpResponse("This is retail. Our categories: \"{0}\", "
                        "these are the states: \"{1}\"".format(categories, states))
