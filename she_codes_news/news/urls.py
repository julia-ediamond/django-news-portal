from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
