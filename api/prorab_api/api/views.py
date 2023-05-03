from django.shortcuts import render, HttpResponse

def index(request):
    template='index.html'
    return render(request, template)
