from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comments, Ratings

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'user', 'build', 'rating_value')

class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_creator = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='creator.id')
    profile_image = serializers.ReadOnlyField(source='creator.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    rating = RatingSerializer(many=False, read_only=True)

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.creator

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comments
        fields = (
            'id', 'creator',  'profile_id',
            'content', 'profile_image', 'build', 'is_creator', 'created_at', 'updated_at', 'rating',
        )

class CommentDetailSerializer(CommentSerializer):
    build = serializers.ReadOnlyField(source='build.id')

