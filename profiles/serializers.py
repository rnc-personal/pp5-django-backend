from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Profile
        fields = (
            'id', 'creator', 'name', 'country', 'description',
            'content', 'profile_image', 'profile_banner'
        )