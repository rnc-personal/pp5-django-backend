from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Build
from .serializers import BuildSerializer
from pp5djangoapi.permissions import IsOwnerOrReadOnly

class BuildList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        builds = Build.objects.all()
        serializer = BuildSerializer(
            builds, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = BuildSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class BuildDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BuildSerializer

    def get_object(self, pk):
        try:
            build = Build.objects.get(pk=pk)
            self.check_object_permissions(self.request, build)
            return build
        except Build.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        build = self.get_object(pk)
        serializer = BuildSerializer(
            build, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        build = self.get_object(pk)
        serializer = BuildSerializer(
            build, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        build = self.get_object(pk)
        build.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )