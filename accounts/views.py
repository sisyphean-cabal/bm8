from django.shortcuts import render

# Create your views here.


def registerPage(req):
    return render(req, 'accounts/register.html')