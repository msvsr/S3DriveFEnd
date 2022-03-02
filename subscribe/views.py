from django.shortcuts import render, HttpResponseRedirect, reverse
from . import to_subscribe


def upload(request):
    if request.POST:
        res = to_subscribe.subscribe(request.POST)
        return render(request, 'subscribe/subscribe.html', {'message': res})

    return render(request, 'subscribe/subscribe.html')
