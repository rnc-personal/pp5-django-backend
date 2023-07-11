from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_creator = serializers.SerializerMethodField()

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.creator


    class Meta:
        model = Profile
        fields = (
            'id', 'creator', 'name', 'country', 'description',
            'content', 'profile_image', 'profile_banner', 'is_creator'
        )