from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_creator = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    builds_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.creator

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                creator=user, followed=obj.creator
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = (
            'id', 'creator', 'name', 'country', 'description',
            'content', 'profile_image', 'profile_banner', 'is_creator'
        )