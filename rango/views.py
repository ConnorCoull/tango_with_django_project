from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.

def index(request):
    ''' Query the database for a list of ALL categories currently stored.
    Order the categories by the number of likes in descending order.
    Retrieve the top 5 ONLY -- or all if there are less than 5
    Place the list in our context_dict dictionary (with boldmessage)
    that will be passed to the template engine.'''
    #this queries the category model to retreive the top 5 categories
    #the use of '-likes' notes that it is in decending order 'likes' would give ascending
    #pythons list syntax then takes a subset of these up to 5, as specified
    category_list = Category.objects.order_by('-likes')[:5]


    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    #render the response and send it back
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Connor Coull.'}
    return render(request, 'rango/about.html', context=context_dict)
