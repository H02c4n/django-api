from django.http import HttpResponse



def dashboard(req):
    return HttpResponse('This is real home page')