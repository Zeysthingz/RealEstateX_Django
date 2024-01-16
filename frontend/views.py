from django.shortcuts import render


# index page
def index(request):
    context = {

    }
    return render(request, 'index.html', context)


# about page
def about(request):
    context = {

    }
    return render(request, 'about.html', context)
