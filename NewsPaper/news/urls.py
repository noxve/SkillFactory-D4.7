from django.urls import path
# Импортируем созданные нами представления
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchPost

urlpatterns = [
   path('', PostList.as_view(), name='news.html'),
   path('<int:pk>', PostDetail.as_view(), name='new.html'),
   path('search/', SearchPost.as_view(), name='search.html'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]