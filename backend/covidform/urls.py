from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from .views import TempIntoViewSet, TempintoFileViewSet

router = routers.DefaultRouter()
router.register("tempintos", TempIntoViewSet, basename='tempintos')

tempinto_router = routers.NestedDefaultRouter(
    router, "tempintos", lookup='tempinto')
tempinto_router.register("files", TempintoFileViewSet,
                         basename='tempinto-files')

urlpatterns = router.urls+tempinto_router.urls
