from .views import *
from rest_framework import routers

urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'collections', CollectionViewSet)  
router.register(r'artists', ArtistViewSet)
router.register(r'labels', LabelViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'vinyl-formats', VinylFormatViewSet)
router.register(r'conditions', ConditionViewSet)
router.register(r'plates', PlateViewSet)
urlpatterns += router.urls