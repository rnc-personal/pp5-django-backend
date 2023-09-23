from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from pp5djangoapi.permissions import IsOwnerOrReadOnly
from .models import Comments, Ratings
from .serializers import CommentSerializer, CommentDetailSerializer, RatingSerializer, AverageRatingSerializer

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



# class AverageRatingsPerBuild(generics.ListAPIView):
#     serializer_class = AverageRatingSerializer

#     def get_queryset(self):
#         # Calculate the average rating per build using Django's aggregation functions
#         queryset = Ratings.objects.values('build').annotate(average_rating=Avg('rating_value'))

#         # Create an empty list to store the results
#         results = []

#         for item in queryset:
#             build_id = item['build']
#             average_rating = item['average_rating']
#             results.append({'build': build_id, 'average_rating': average_rating})
#             print(f"Build {build_id}: Average Rating = {average_rating}")

#         # Calculate the overall average rating
#         all_averages = sum(item['average_rating'] for item in queryset) / len(queryset)
#         print(f"All Scores: {results}")
#         print(f"Manual Calculation: {all_averages}")

#         # Append the overall average rating to the results
#         results.append({'all_averages': all_averages})

#         return results


class AverageRatingsPerBuild(generics.ListAPIView):
    serializer_class = AverageRatingSerializer

    def get_queryset(self):
        # Calculate the average rating per build using Django's aggregation functions
        queryset = Ratings.objects.values('build').annotate(average_rating=Avg('rating_value'))

        # Create a list to store the results
        results = []

        for item in queryset:
            build_id = item['build']
            average_rating = item['average_rating']
            results.append({'build': build_id, 'average_rating': average_rating})

        return results



