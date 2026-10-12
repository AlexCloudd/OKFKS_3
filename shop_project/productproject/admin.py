from django.contrib import admin
from .models import (
    Plate, Artist, Label, Category, 
    Collection, Genre, VinylFormat, Condition, Order, OrderItem
)

@admin.register(Plate)
class PlateAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(VinylFormat)
class VinylFormatAdmin(admin.ModelAdmin):
    pass

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass