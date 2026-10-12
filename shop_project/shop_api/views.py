from django.shortcuts import render
from rest_framework import permissions, filters

from .permission import PaginationPage, CustomPermission
from .serializers import ArtistSerializer, CategorySerializer, CollectionSerializer, ConditionSerializer, GenreSerializer, LabelSerializer, PlateSerializer, VinylFormatSerializer
from rest_framework import viewsets
from productproject.models import Artist, Category, Collection, Condition, Genre, Label, Plate, VinylFormat

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = PaginationPage 
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']
    
class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class VinylFormatViewSet(viewsets.ModelViewSet):
    queryset = VinylFormat.objects.all()
    serializer_class = VinylFormatSerializer
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    pagination_class = PaginationPage
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    pagination_class = PaginationPage
    permission_classes = [permissions.IsAuthenticated, CustomPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']