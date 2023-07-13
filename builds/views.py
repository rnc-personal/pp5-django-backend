from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Build
from .serializers import BuildSerializer


class BuildList(APIView):
    serializer_class = BuildSerializer
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