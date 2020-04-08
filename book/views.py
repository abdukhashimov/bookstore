from rest_framework.views import APIView
from rest_framework.response import Response
from book.models import tracker, Book
from rest_framework import status


class BookApiView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'count': tracker.count}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        Book.objects.create(name="data.get('name')")
        return Response(status.HTTP_201_CREATED)
