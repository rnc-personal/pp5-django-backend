from rest_framework import generics
from .models import HeroContent
from .serializers import (
    HeroContentSerializer,
    CmsDataSerializer
)

class CmsDetailView(generics.RetrieveAPIView):
    serializer_class = CmsDataSerializer

    def get_object(self):
        hero_content = HeroContent.objects.first()

        return {

            'hero_content': hero_content,
        }

