from rest_framework import generics, permissions
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from user_save.models import SaveLike
from user_save.serializers import SaveSerializer

class SaveList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class SaveDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Save.objects.all()