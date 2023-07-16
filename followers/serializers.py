from rest_framework import serializers
from .models import User, Follower
from django.db import IntegrityError

class FollowerSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    followed_by = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'creator', 'created_at', 'followed', 'followed_by']

    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('You already follow this user')