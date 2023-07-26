from django.db import IntegrityError
from rest_framework import serializers
from user_save.models import Save

class SaveSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')
    
    class Meta:
        model = Save
        fields = [
            'id',
            'creator',
            'build',
            'created_at',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('This Build is already saved.')