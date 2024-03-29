from django.urls import path
from . import views

app_name = 'Music'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('<int:album_id>/favorite', views.favorite, name='favorite'),
]
