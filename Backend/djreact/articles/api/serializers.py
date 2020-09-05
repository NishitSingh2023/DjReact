from rest_framework import serializers
from articles.models import Article

class articleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

