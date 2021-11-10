from django.urls import path, include
from .views import TempIntoViewSet, TempintoFileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'', TempIntoViewSet)
router.register(r'upload', TempintoFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
