from django.shortcuts import render
from django.http import HttpResponseRedirect
from mailchimp import utils
from mailchimp.chimpy.chimpy import ChimpyException
import logging
import requests
import sys

MAILCHIMP_LIST_ID = 'secret'

# Get an instance of a logger
logger = logging.getLogger(__name__)

def subscribe(request):

    if request.POST['email']:
        try:
            email_address = request.POST['email']
            list = utils.get_connection().get_list_by_id(MAILCHIMP_LIST_ID)
            list.subscribe(email_address, {'EMAIL': email_address})
            return HttpResponseRedirect('/subscription/success')
        except ChimpyException:
            return HttpResponseRedirect('/subscription/subscribed')
    else:
        return HttpResponseRedirect('/subscription/failure')

def success(request):
    return render(request, 'subscription/success.html')

def failure(request):
    return render(request, 'subscription/failure.html')

def already_subscribed(request):
    return render(request, 'subscription/already_subscribed.html')
