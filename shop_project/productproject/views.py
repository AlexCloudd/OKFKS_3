from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from .models import Plate, Artist, Label, Category, Collection, Order, OrderItem
from .forms import (
    PlateForm, ArtistForm, LabelForm, CategoryForm, CollectionForm, 
    RegisterForm, LoginForm, CartAddForm
)
from .cart import Cart


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

@login_required(login_url='productproject:login')
def cart_add(request, plate_id):
    cart = Cart(request)
    plate = get_object_or_404(Plate, id=plate_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart.add(plate=plate, quantity=quantity, update_quantity=False)
    
    return redirect('productproject:cart')


@login_required(login_url='productproject:login')
def cart_remove(request, plate_id):
    cart = Cart(request)
    plate = get_object_or_404(Plate, id=plate_id)
    cart.remove(plate)
    return redirect('productproject:cart')


@login_required(login_url='productproject:login')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required(login_url='productproject:login')
def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('productproject:cart')

    order = Order.objects.create(
        user=request.user,
        total_price=cart.get_total_price()
    )

    for item in cart:
        OrderItem.objects.create(
            order=order,
            plate=item['plate'],
            quantity=item['quantity'],
            price=item['price']
        )

    cart.clear() 
    return redirect('productproject:order_success')


@method_decorator(permission_required('productproject.add_plate', login_url='productproject:login'), name='dispatch')
class PlateCreateView(CreateView):
    model = Plate
    form_class = PlateForm
    template_name = 'plates/plate_form.html'
    success_url = reverse_lazy('productproject:plate_list')  

@method_decorator(permission_required('productproject.change_plate', login_url='productproject:login'), name='dispatch')
class PlateUpdateView(UpdateView):
    model = Plate
    form_class = PlateForm
    template_name = 'plates/plate_form.html'
    success_url = reverse_lazy('productproject:plate_list')

@method_decorator(permission_required('productproject.delete_plate', login_url='productproject:login'), name='dispatch')
class PlateDeleteView(DeleteView):
    model = Plate
    template_name = 'plates/plate_confirm_delete.html'
    success_url = reverse_lazy('productproject:plate_list')


@method_decorator(permission_required('productproject.add_artist', login_url='productproject:login'), name='dispatch')
class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'
    success_url = reverse_lazy('productproject:artist_list')

@method_decorator(permission_required('productproject.change_artist', login_url='productproject:login'), name='dispatch')
class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists/artist_form.html'
    success_url = reverse_lazy('productproject:artist_list')

@method_decorator(permission_required('productproject.delete_artist', login_url='productproject:login'), name='dispatch')
class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'artists/artist_confirm_delete.html'
    success_url = reverse_lazy('productproject:artist_list')


@method_decorator(permission_required('productproject.add_label', login_url='productproject:login'), name='dispatch')
class LabelCreateView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('productproject:label_list')

@method_decorator(permission_required('productproject.change_label', login_url='productproject:login'), name='dispatch')
class LabelUpdateView(UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('productproject:label_list')

@method_decorator(permission_required('productproject.delete_label', login_url='productproject:login'), name='dispatch')
class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('productproject:label_list')


@method_decorator(permission_required('productproject.add_category', login_url='productproject:login'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('productproject:category_list')

@method_decorator(permission_required('productproject.change_category', login_url='productproject:login'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('productproject:category_list')

@method_decorator(permission_required('productproject.delete_category', login_url='productproject:login'), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('productproject:category_list')


@method_decorator(permission_required('productproject.add_collection', login_url='productproject:login'), name='dispatch')
class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_url = reverse_lazy('productproject:collection_list')

@method_decorator(permission_required('productproject.change_collection', login_url='productproject:login'), name='dispatch')
class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections/collection_form.html'
    success_url = reverse_lazy('productproject:collection_list')

@method_decorator(permission_required('productproject.delete_collection', login_url='productproject:login'), name='dispatch')
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collections/collection_confirm_delete.html'
    success_url = reverse_lazy('productproject:collection_list')

class PlateListView(ListView):
    model = Plate
    template_name = 'plates/plate_list.html'
    context_object_name = 'plates'

class PlateDetailView(DetailView):
    model = Plate
    template_name = 'plates/plate_detail.html'
    context_object_name = 'plate'

@method_decorator(login_required(login_url='productproject:login'), name='dispatch')
class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'
    context_object_name = 'artists'

@method_decorator(login_required(login_url='productproject:login'), name='dispatch')
class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/artist_detail.html'
    context_object_name = 'artist'

@method_decorator(login_required(login_url='productproject:login'), name='dispatch')
class LabelListView(ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'

@method_decorator(login_required(login_url='productproject:login'), name='dispatch')
class LabelDetailView(DetailView):
    model = Label
    template_name = 'labels/label_detail.html'
    context_object_name = 'label'

@method_decorator(permission_required('productproject.view_category', login_url='productproject:login'), name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

@method_decorator(permission_required('productproject.view_category', login_url='productproject:login'), name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'

@method_decorator(permission_required('productproject.view_collection', login_url='productproject:login'), name='dispatch')
class CollectionListView(ListView):
    model = Collection
    template_name = 'collections/collection_list.html'
    context_object_name = 'collections'

@method_decorator(permission_required('productproject.view_collection', login_url='productproject:login'), name='dispatch')
class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collections/collection_detail.html'
    context_object_name = 'collection'

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)        
            return redirect('productproject:plate_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('productproject:plate_list')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('productproject:plate_list')