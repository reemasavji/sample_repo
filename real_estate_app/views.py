from django.shortcuts import render

# Create your views here.
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import *

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='text-align:center'>Hello World!!!</h1>")

def index(request):
	listings = Listing.objects.all().order_by("-list_date")[:3]
	context = {
		'listings' : listings,
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'price_choices': price_choices,
	}
	
	return render(request,'real_estate_app/index.html',context)

def about(request):
	realtors = Realtor.objects.all()
	if Realtor.objects.filter(is_mvp=True).exists():
		seller = Realtor.objects.filter(is_mvp=True)[0]
	else:
		seller = ''
	return render(request,'real_estate_app/about.html',{'realtors':realtors,'seller':seller})