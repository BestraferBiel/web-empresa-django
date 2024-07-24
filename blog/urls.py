from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name="blog"),
    path('category/<int:category_id>/', blog_views.category, name="category"),
    
]