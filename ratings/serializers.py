from django.db import IntegrityError
from rest_framework import serializers
from ratings.models import Rating

class RatingSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = Rating
        fields = [
            'id',
            'creator',
            'build',
            'rating',
            'created_at',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('User already rated this post')