from django.db import IntegrityError
from rest_framework import serializers
from ratings.models import Rating

class RatingSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    score = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def get_score(self, obj):
        request = self.context['request']
        if request.user == obj.creator:
            return obj.score
        else:
            return 0

    def get_average_rating(self, obj):
            return obj.build.average_rating

    class Meta:
        model = Rating
        fields = [
            'id',
            'creator',
            'build',
            'score',
            'average_rating',
            'created_at',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('User already rated this post')