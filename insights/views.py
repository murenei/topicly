from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.generic import View
import datetime as dt

# Create your views here.
def index(request):
    now = dt.datetime.now()
    html = '<html><body><p>The time is %s</p></body></html>' % now
    context = {
        'data': now
    }
    return HttpResponse(html)



def get_data(request):
    data = {
        'name': 'Joatmon',
        'orders': 20
    }
    return JsonResponse(data)

def insights(request, random_nr):
    text = 'Here is a random number'
    context = {
        'words': text,
        'numbers': int(random_nr),
    }
    template_name = 'insights/base.html'
    print(context)
    return render(request, template_name, context)
