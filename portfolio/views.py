from django.shortcuts import render

# Create your views here.

def portfolio_home(request):
    return render(request, 'portfolio/portfolio_home.html')