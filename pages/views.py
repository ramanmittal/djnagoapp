from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Listing
from realtors.models import Realtor
from listing.choices import bedroom_choices,price_choices,state_choices
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    return render(request,"pages/index.html", {"listings": listings,"bedroom_choices":bedroom_choices,"price_choices":price_choices,"state_choices":state_choices})

def about(request):
    realtors=Realtor.objects.order_by("-hire_date")
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
    return render(request,"pages/about.html",{'realtors':realtors,'mvp_realtors':mvp_realtors})

# Create your views here.
