# bring in the magic
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext


def test_view(request):
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        return render(request, 'test_view.html', {}, context)

    return render(request, 'test_view.html', {}, context)
