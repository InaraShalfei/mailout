from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import ClientViewSet, MailOutViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('mailouts', MailOutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
