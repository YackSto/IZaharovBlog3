
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name="detail_post"),
    path('add_post/', views.AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', views.EditPost.as_view(), name="edit_post"),
    path('article/<int:pk>/delete', views.DeletePost.as_view(), name="delete_post"),
    path('categories/<slug:slug_id>/', views.CategoryList.as_view(), name="category"),
    path('like/<int:pk>', views.LikeView, name="like_post"),
    path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name="add_comment"),
    path('search/', views.SearchView.as_view(), name="search")
] 
