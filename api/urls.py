from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import ClientViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
