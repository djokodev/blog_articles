from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete



urlpatterns = [
    path("", BlogHome.as_view(), name="home"),
    path("create_post/", BlogPostCreate.as_view(), name="create_post"),
    path("update_post/<str:slug>/", BlogPostUpdate.as_view(), name="update_post"),
    path("detail_post/<str:slug>/", BlogPostDetail.as_view(), name="detail_post"),
    path("delete_post/<str:slug>/", BlogPostDelete.as_view(), name="delete_post"),
]
