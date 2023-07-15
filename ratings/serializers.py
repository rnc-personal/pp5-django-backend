from django.db import IntegrityError
from rest_framework import serializers
from ratings.models import Rating

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
        return None

    def get_average_rating(self, obj):
        return obj.build.average_rating

    def validate_score(self, value):
        request = self.context['request']
        if self.instance and request.user == self.instance.creator:
            return value
        raise serializers.ValidationError("You can only edit your own score.")

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
