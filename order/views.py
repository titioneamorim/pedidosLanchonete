from django.shortcuts import render

def home_order(request):
    return render(request, 'home_order.html')
