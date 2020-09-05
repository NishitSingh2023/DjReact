from rest_framework import viewsets

from articles.models import Article
from .serializers import articleSerializers

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = articleSerializers
 
'''
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from articles.models import Article
from .serializers import articleSerializers

class articleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = articleSerializers

class articleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = articleSerializers

class articleCreateView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = articleSerializers

class articleDeleteView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = articleSerializers

class articleUpdateView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = articleSerializers
'''
