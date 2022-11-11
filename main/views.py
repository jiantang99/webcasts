from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': "Welcome to the best Django tutorials"
    }
    return render(request, 'pages/home.html', context)

def about_us(request):
    context = {
        'title': "About us"
    }
    return render(request, 'pages/about_us.html', context)