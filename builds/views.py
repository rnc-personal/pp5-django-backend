from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from .models import Build
from .serializers import BuildSerializer


class BuildList(generics.ListCreateAPIView):
    serializer_class = BuildSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Build.objects.annotate(
        saves_count=Count('saves', distinct=True),
        comments_count=Count('comments', distinct=True)
        ).order_by('-created_at')
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'creator__followed__creator__profile',
        'saves__creator__profile',
        'creator__profile',
    ]

    ordering_fields = [
        'saves_count',
        'comments_count',
        'saves__created_at',
    ]

    search_fields = [
        'creator__username',
        'build_name',
        'build_cpu',
        'build_mobo',
        'build_gpu',
        'build_ram',
        'build_disk',
        'build_case',
        'build_monitor',
    ]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class BuildDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuildSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Build.objects.annotate(
        saves_count=Count('saves', distinct=True),
        comments_count=Count('comments', distinct=True),
        rating_1_avg=Avg('user_rating_1', distinct=True)
    ).order_by('-created_at')