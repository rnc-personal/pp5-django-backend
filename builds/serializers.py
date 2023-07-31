from rest_framework import serializers
from builds.models import Build
from user_save.models import Save

class BuildSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='creator.profile.id')
    profile_image = serializers.ReadOnlyField(source='creator.profile.image.url')
    save_id = serializers.SerializerMethodField()
    saves_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.creator

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Save.objects.filter(creator=user, build=obj).first()
            return save.id if save else None
        return None

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
                'build_monitor', 'save_id', 'saves_count', 'comments_count',
            ]