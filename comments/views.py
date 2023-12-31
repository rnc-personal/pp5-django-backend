from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from .models import Comments, Ratings, Build
from .serializers import CommentSerializer, CommentDetailSerializer, RatingSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['build']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comments.objects.all()

class RatingsList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ratings.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['build']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Ratings.objects.all()
