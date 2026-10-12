from rest_framework import serializers
from productproject.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name', 'description']
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'description', 'country', 'photo']
        
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name', 'description', 'country', 'logo']
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']
        
class VinylFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VinylFormat
        fields = ['name', 'description', 'grade']
        
class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['name', 'description', 'grade']
        
class PlateSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label="Цена", max_digits=10, decimal_places=2)
    class Meta:
        model = Plate
        fields = ['name', 'description', 'price', 'year', 'photo', 'is_exist' ]