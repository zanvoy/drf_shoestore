from django.conf.urls import include, url
from api.views import ShoeColorViewSet, ManufacturerViewSet, ShoeTypeViewSet, ShoeViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'shoe', ShoeViewSet, basename='shoe')
router.register(r'shoe_color', ShoeColorViewSet, basename='shoe color')
router.register(r'shoe_type', ShoeTypeViewSet, basename='shoe type')
router.register(r'manufacurer', ManufacturerViewSet, basename='manufacturer')

urlpatterns = [
    url(r'^api/', include(router.urls))
]