from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, start_ml_training

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start-ml-training/', start_ml_training, name='start-ml-training'),
]
