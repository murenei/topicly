from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.generic import View
import datetime as dt

# Create your views here.


def index(request):
    now = dt.datetime.now()
    # html = '<html><body><p>The time is %s</p></body></html>' % now
    context = {
        'data': now
    }
    template_name="insights/index.html"
    # return HttpResponse(html)
    return render(request, template_name,context)


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
    template_name = 'insights/chart.html'
    print(context)
    return render(request, template_name, context)


def bokeh(request):
    from bokeh.plotting import figure, output_file, save

    # prepare some data
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    # output to static HTML file
    output_file("insights/lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)

    save(p)

    template_name = 'insights/lines.html'

    return render(request, template_name)


def cyto(request):
    import networkx as nx
    G = nx.karate_club_graph()
    context = {
        'nodes': list(G.nodes),
        'edges': list(G.edges),
    }
    template_name = 'insights/cyto.html'

    return render(request, template_name, context)


# REST API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class GetData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        data = {
            "labels": ["red", "blue", 'yellow'],
            "default": [12, 19, 3, 5, 2, 3],
            "users": len(usernames),
        }
        return Response(data)
