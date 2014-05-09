from django.conf import settings
from django.shortcuts import render, render_to_response, RequestContext, Http404, HttpResponseRedirect,  HttpResponse
from django.template.defaultfilters import slugify
from django.core.servers.basehttp import FileWrapper

from .models import UserTransaction


def library(request):
	if request.user.is_authenticated():
		products = request.user.usertransaction.products.all()
		return render_to_response("profiles/library.html", locals(), context_instance=RequestContext(request))
	else:
		raise Http404