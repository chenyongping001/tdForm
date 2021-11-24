from os import name
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
from .views import TempIntoViewSet, TempintoFileViewSet

router = routers.DefaultRouter()
router.register("tempintos", TempIntoViewSet, basename='tempintos')

tempinto_router = routers.NestedDefaultRouter(
    router, "tempintos", lookup='tempinto')
tempinto_router.register("files", TempintoFileViewSet,
                         basename='tempinto-files')

urlpatterns = [
    path("", include(router.urls+tempinto_router.urls)),
    path('qj_tempinto/', views.QJTempinto.as_view(), name='qj_tempinto')
]

# urlpatterns = router.urls+tempinto_router.urls
