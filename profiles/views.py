from django.db.models import Count
from rest_framework import generics, filters
# from django_filters.rest_framework import DjangoFilterBackend
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        builds_count=Count('creator__build', distinct=True),
        followers_count=Count('creator__followed', distinct=True),
        following_count=Count('creator__following', distinct=True)
    ).order_by('-created_at')

    serializer_class = ProfileSerializer

    # filter_backends = [
    #     filters.OrderingFilter,
    #     DjangoFilterBackend,
    # ]

    filterset_fields = [
        'creator__following__followed__profile',
        'creator__followed__creator__profile',
    ]

    ordering_fields = [
        'builds_count',
        'followers_count',
        'following_count',
        'creator__following__created_at',
        'creator__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.annotate(
        builds_count=Count('creator__build', distinct=True),
        followers_count=Count('creator__followed', distinct=True),
        following_count=Count('creator__following', distinct=True)
    ).order_by('-created_at')

    serializer_class = ProfileSerializer