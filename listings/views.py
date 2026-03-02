from django.shortcuts import get_object_or_404 ,render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import price_choices, bedroom_choices, state_choices
from .models import Listing

# Create your views here.
# all listings view
def index(request):
    listings = Listing.objects.all().order_by('id').filter(is_published=True)

    paginator = Paginator(listings, 6)  # Show 3 on page
    page_number = request.GET.get("page")
    page_listings = paginator.get_page(page_number)

    context = {
        'listings': page_listings
    }

    return render(request, 'listings/listings.html', context )

# single listing view
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)




# Search listing wiev
def search(request):
    queryset_list=Listing.objects.all().order_by('-list_date')


# Setarea campurilor din formul de search

    # Check if keyword exists in search form field
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Check for city 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

     # Check for state 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

     # Check for bedroom 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__exact=bedrooms)

     # Check for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)






    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings':queryset_list,
        'values':request.GET

    }
    return render(request, 'listings/search.html', context)
