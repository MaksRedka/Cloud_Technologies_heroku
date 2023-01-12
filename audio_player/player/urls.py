from rest_framework import routers
from .api import AudioViewSet


router = routers.DefaultRouter()
router.register('api/audio', AudioViewSet, 'audio')

urlpatterns = router.urls

