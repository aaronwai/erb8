from django.shortcuts import render
from listings.models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request,'pages/index.html', context)
def about(request):
    print(request, request.path)
    return render(request,'pages/about.html')