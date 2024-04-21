from django.shortcuts import render
from django.views import View
from .models import Category, Client, Product,  Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, request):
        category = Category.objects.all()
        products = Product.objects.all()
        clients = Client.objects.all()
        context = {
            'category': category,
            'products': products,
            'clients': clients
        }
        return render(request, 'main/index.html', context)

class ShopView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'main/shop.html', context)

class ShopDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        return render(request, 'main/shop-detail.html', {'products': products})

class CartView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'main/cart.html', {'products': products})

class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'main/checkout.html', {'products': products})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.all()
        context = {
            'profile': profile
        }
        return render(request, 'main/profile.html', context)

