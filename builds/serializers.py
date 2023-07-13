from rest_framework import serializers
from builds.models import Build

class BuildSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='creator.profile.id')
    profile_image = serializers.ReadOnlyField(source='creator.profile.image.url')
    content = serializers.ReadOnlyField(source='builds.content')
    main_image = serializers.ReadOnlyField(source='builds.main_image.url')
    gallery_image_1 = serializers.ReadOnlyField(source='builds.gallery_image_1.url')
    gallery_image_2 = serializers.ReadOnlyField(source='builds.gallery_image_2.url')
    gallery_image_3 = serializers.ReadOnlyField(source='builds.gallery_image_3.url')
    gallery_image_4 = serializers.ReadOnlyField(source='builds.gallery_image_4.url')
    build_cpu = serializers.ReadOnlyField(source='builds.build_cpu')
    build_mobo = serializers.ReadOnlyField(source='builds.build_mobo')
    build_ram = serializers.ReadOnlyField(source='builds.build_ram')
    build_disk = serializers.ReadOnlyField(source='builds.build_disk')
    build_gpu = serializers.ReadOnlyField(source='builds.build_gpu')
    build_case = serializers.ReadOnlyField(source='builds.build_case')
    build_monitor = serializers.ReadOnlyField(source='builds.build_monitor')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.creator

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
                'build_monitor'
            ]