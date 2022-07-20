from rest_framework.serializers import HyperlinkedModelSerializer

from test_app.models import Book


class BookSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['url', 'title', 'author']
