from django.shortcuts import render

def home_order(request):
    return render(request, 'home_order.html')

def update_product_screen(request, id):
    product = _SERVICE.search_product_by_id(id)
    return render(request, 'edit-product.html', context={'product':product})

def save_product(request):
    serializer = ProductSerializer(data=request.POST)

def search_product_by_therm(request):
    therm = request.GET.get('therm')
    products = _SERVICE.search_products_by_therm(therm)
    return render(request, 'home-products.html', context={'products':products})