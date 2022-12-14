from django.urls import path
from .views import PostList, PostDetail, NewsCreate, NewsEdit, NewsDelete, CategoryListView, subscribe

urlpatterns = [
   path('', PostList.as_view(), name='all_news'),
   path('<int:pk>', PostDetail.as_view(), name='news'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   # path('become/', become_author, name='become_author'),
]
