from django.db import IntegrityError
from rest_framework import generics, permissions, serializers
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from ratings.models import Rating
from ratings.serializers import RatingSerializer


class RatingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(creator=self.request.user)
        return queryset

    def perform_create(self, serializer):
            creator = self.request.user
            build = serializer.validated_data.get('build')
            try:
                rating = Rating.objects.get(creator=creator, build=build)
                rating.score = serializer.validated_data.get('score')
                rating.save()
            except Rating.DoesNotExist:
                serializer.save(creator=creator)
            except IntegrityError:
                raise serializers.ValidationError('User already rated this post')

class RatingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_update(self, serializer):
        serializer.save()