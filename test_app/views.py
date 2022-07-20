from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from test_app.models import Book
from test_app.serializers import BookSerializer


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
