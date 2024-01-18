from django.shortcuts import render


def list_all_properties(request):
    context = {

    }
    return render(request, 'property_app/listings.html', context)


def property_detail(request, property_id):
    context = {

    }
    return render(request, 'property_app/listing.html', context)


def search_properties(request):
    context = {

    }
    return render(request, 'property_app/search.html', context)
