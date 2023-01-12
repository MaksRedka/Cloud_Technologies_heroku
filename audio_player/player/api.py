from .models import Audio
from rest_framework import viewsets, permissions
from .serializers import AudioSerializer


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AudioSerializer

