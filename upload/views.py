from django.shortcuts import render, HttpResponseRedirect, reverse
from . import file_uploader


def upload(request):
    if request.POST:
        res = file_uploader.to_s3(request.FILES)

    return render(request, 'upload/upload.html')
