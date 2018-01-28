from django.http import *

def home(request):
    return HttpResponse(u'<h1>Merhaba Dunya<h1>')