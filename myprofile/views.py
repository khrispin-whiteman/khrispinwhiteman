from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myprofile/index.html')


def contact(request):
    return render(request, 'myprofile/contact.html')