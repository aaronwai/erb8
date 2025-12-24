from django.shortcuts import render

# Create your views here.
def listings(request):
    print(request.path)
    return render(request, 'listings/listings.html')

def listing(request,listing_id):
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')