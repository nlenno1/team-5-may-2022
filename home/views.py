from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about_us(request):
    """ A view to return the about us page """

    return render(request, 'home/about-us.html')


def how_to_use(request):
    """ A view to return the how to use page """

    return render(request, 'home/how-to-use.html')
