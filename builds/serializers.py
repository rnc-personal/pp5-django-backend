from rest_framework import serializers
from builds.models import Build

class BuildSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='creator.profile.id')
    profile_image = serializers.ReadOnlyField(source='creator.profile.image.url')
    average_rating = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.creator

    def get_average_rating(self, obj):
        return obj.average_rating

    class Meta:
            model = Build
            fields = [
                'id', 'creator', 'is_owner', 'profile_id',
                'profile_image', 'created_at', 'updated_at',
                'build_name', 'content', 'main_image',
                'gallery_image_1', 'gallery_image_2',
                'gallery_image_3', 'gallery_image_4',
                'build_cpu', 'build_mobo', 'build_ram',
                'build_disk', 'build_gpu', 'build_case',
                'build_monitor', 'average_rating',
            ]