from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Listing
from listing.choices import bedroom_choices,price_choices,state_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    if page is None:
        page = 1
    return render(request, 'listings/listings.html', {"listings": paginator.get_page(page)})


def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    return render(request, 'listings/listing.html',{"listing":listing})

def search(request):
    keywords=request.GET.get("keywords")
    city=request.GET.get("city")
    state=request.GET.get("state")
    bedrooms=request.GET.get("bedrooms")
    price=request.GET.get("price")
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    if keywords is not None:
        listings=listings.filter(description__icontains=keywords)
    if city is not None and city != '':
        listings=listings.filter(city__iexact=city)
    if state is not None:
        listings=listings.filter(state__iexact=state)
    if bedrooms is not None:
        listings=listings.filter(bedrooms__lte=bedrooms)
    if price is not None:
        listings=listings.filter(price__lte=price)
    return render(request, 'listings/search.html',{"listings":listings,"bedroom_choices":bedroom_choices,"price_choices":price_choices,"state_choices":state_choices,"values":request.GET})
