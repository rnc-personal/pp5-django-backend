from rest_framework import serializers
from .models import HeroContent

class HeroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroContent
        fields = '__all__'

class CmsDataSerializer(serializers.Serializer):
    hero_content = HeroContentSerializer()

