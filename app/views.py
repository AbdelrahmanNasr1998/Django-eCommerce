import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response
from django.contrib import messages
from .forms import UserLoginForm, NewUserForm
from .serializers import ProductsSerializer, FavoriteSerializer, CartSerializer
from products.models import Category, Product
from users.models import Favorite, Cart
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import OuterRef, Subquery
from django.db.models import Q


class HomeView(View):
    def get(self, request):
        context = {'user': request.user}
        cats = Category.objects.all()
        context['cats'] = cats
        return render(request, 'app/home.html', context)


class ProductsView(View):
    def get(self, request, category):
        try:
            context = {'user': request.user}
            cats = Category.objects.all()
            instance = Product.objects.filter(category__name=category)
            serializer = ProductsSerializer(instance, many=True)
            products = serializer.data
            context['cats'] = cats
            context['category'] = category
            if products:
                context['products'] = products
                return render(request, 'app/products.html', context)
            else:
                return render(request, 'app/products.html', context)
        except:
            raise Http404


class ProductDetailsView(View):
    def get(self, request, category, product):
        # try:
            context = {'user': request.user}
            cats = Category.objects.all()
            instance = Product.objects.get(category__name=category, id=product)
            serializer = ProductsSerializer([instance], many=True)
            product = serializer.data
            if product:
                context['cats'] = cats
                context['category'] = category
                context['product'] = product
                context['range'] = range(1, int(instance.items)+1)
                if request.user.is_authenticated:
                    try:
                        context['favorite'] = Favorite.objects.get(user=request.user, product=instance.id)
                    except ObjectDoesNotExist:
                        pass
                return render(request, 'app/product_details.html', context)
            else:
                raise Http404
        # except:
        #     raise Http404

    def post(self, request, category, product):
        # try:
            context = {'user': request.user}
            instance = Product.objects.get(id=product)
            items = request.POST.get('items')
            if Cart.objects.filter(user=context['user'], product=instance.id).exists():
                cart_pro = Cart.objects.get(user=context['user'], product=instance.id)
                total_items = int(items) + int(cart_pro.items)
                if instance.items >= total_items:
                    price = int(total_items) * int(instance.price)
                    Cart.objects.update(user=context['user'], product=instance, items=total_items, price=price)
                else:
                    pass
            else:
                price = int(items) * int(instance.price)
                Cart.objects.create(user=context['user'], product=instance, items=items, price=price)
            return redirect("Cart")
        # except:
        #     raise Http404


class LoginView(View):
    form_class = UserLoginForm
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            cats = Category.objects.all()
            context = {
                'form': self.form_class(),
                'cats': cats,
            }
            return render(request, 'app/login.html', context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.warning(request, 'username or password is incorrect!.')
                return redirect("Login")
        else:
            for key, error in list(form.errors.items()):
                messages.error(request, error)
        return render(request, 'app/login.html', {'form': form})


class RegisterView(View):
    form_class = NewUserForm
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            cats = Category.objects.all()
            context = {
                'form': self.form_class(),
                'cats': cats,
            }
            return render(request, 'app/register.html', context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("Login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            NewUserForm()
            return render(request, "app/register.html", {"form": NewUserForm})


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('Login')
        else:
            return redirect('Login')


class FavoriteView(View):
    def get(self, request):
        if request.user.is_authenticated:
            cats = Category.objects.all()
            instance = Favorite.objects.filter(user=request.user)
            serializer = FavoriteSerializer(instance, many=True)
            favorite = serializer.data
            context = {
                'favorite': favorite,
                'cats': cats,
            }
            return render(request, 'app/favorite.html', context)
        else:
            return redirect('Login')


class AddFavoriteView(View):
    def get(self, request, product_id):
        if request.user.is_authenticated:
            if Favorite.objects.filter(user=request.user, product=Product.objects.get(id=product_id)).exists():
                return redirect('Favorite')
            else:
                Favorite.objects.create(user=request.user, product=Product.objects.get(id=product_id))
                return redirect('Favorite')
        else:
            return redirect('Login')


class DeleteFavoriteView(View):
    def get(self, request, favorite_id):
        if request.user.is_authenticated:
            if Favorite.objects.filter(user=request.user, id=favorite_id).exists():
                Favorite.objects.filter(user=request.user, id=favorite_id).delete()
                return redirect('Favorite')
            else:
                return redirect('Favorite')
        else:
            return redirect('Login')


class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            instance = Cart.objects.filter(user=request.user)
            serializer = CartSerializer(instance, many=True)
            cart = serializer.data
            context = {
                'cart': cart
            }
            return render(request, 'app/cart.html', context)
        else:
            return redirect('Login')