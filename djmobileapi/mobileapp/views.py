from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    mob = request.POST.get('mob', None)

    response = requests.get('http://postalpincode.in/api/pincode/%s' % mob)
    postaldat = response.json()
    context = {'city': postaldat['Message'],
               'cites': postaldat['PostOffice']}

    return render(request, 'home.html', context)
