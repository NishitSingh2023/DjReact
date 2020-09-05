from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls


'''
from django.urls import path
from .views import articleListView, articleDetailView, articleCreateView, articleDeleteView, articleUpdateView

urlpatterns = [
    path('', articleListView.as_view()),
    path('create/', articleCreateView.as_view()),
    path('<pk>', articleDetailView.as_view()),
    path('<pk>/update/', articleUpdateView.as_view()),
    path('<pk>/delete/', articleDeleteView.as_view()),

]
'''
