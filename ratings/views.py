from rest_framework import generics, permissions
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from ratings.models import Rating
from ratings.serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class RatingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()