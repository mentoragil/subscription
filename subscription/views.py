from django.shortcuts import render
from django.http import HttpResponseRedirect
from mailchimp import utils
from mailchimp.chimpy.chimpy import ChimpyException
import logging
import requests
import sys

MAILCHIMP_LIST_ID = '17edfa12f6'
#API_KEY = '3a0e977cf36db4fe9a4c46eb3b9272d4-us10'

# Get an instance of a logger
logger = logging.getLogger(__name__)

def subscribe(request):

    if request.POST['email']:
        try:
            email_address = request.POST['email']
            #data = '{ "apikey": "' + API_KEY + '", "id": "' + MAILCHIMP_LIST_ID + '", "email": { "email": "' + email_address + '" }, "merge_vars": {}, "email_type": "html", "double_optin": true, "update_existing": true, "replace_interests": true, "send_welcome": true }'
            #response = requests.post('https://us10.api.mailchimp.com/2.0/lists/Subscribe.json', data=data, headers={'Content-type': 'application/json', 'Accept': 'text/plain'}, verify=False).text
            #print >>sys.stderr, response
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
