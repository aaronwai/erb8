from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import district_choices, rooms_choices, room_choices
from django.db.models import Q
# Create your views here.
def listings(request):
    listings = Listing.objects.filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {"listings" : paged_listings}
    return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing" : listing}
    return render(request, 'listings/listing.html', context)
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords)| Q(title__icontains=keywords) | Q(doctor__name__icontains=keywords))
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list =queryset_list.filter(district__iexact=district) 
    if 'rooms' in  request.GET:
        rooms = request.GET['rooms']
        if rooms:
            queryset_list =queryset_list.filter(rooms__gte=rooms)
    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
        if room_type:
            queryset_list = queryset_list.filter(room_type__iexact=room_type)  
    paginator = Paginator(queryset_list,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)                     
    context = {
        "listings": paged_listings,
        'district_choices': district_choices,
        'rooms_choices': rooms_choices,
        'room_choices': room_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)