from django import forms
from .models import Plate, Artist, Label, Category, Collection
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class PlateForm(forms.ModelForm):
    class Meta:
        model = Plate
        fields = [
            'name', 'description', 'price', 'year', 'photo',
            'category', 'artist', 'label', 'genre',
            'vinyl_format', 'condition', 'collection'
        ]


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'description', 'country', 'photo']


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'description', 'country', 'logo']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass
        
class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.HiddenInput())
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())