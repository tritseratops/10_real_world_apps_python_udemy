from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name = 'blog_view'),
    path('', views.PostList.as_view(), name = 'home'),
    path('about/', views.AboutView.as_view(), name = 'about_view'),
]