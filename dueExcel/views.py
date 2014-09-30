# Create your views here.
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def mytest(request):
    now = datetime.datetime.now()
    return render_to_response('test.html', {'currenttime':now}, context_instance = RequestContext(request))