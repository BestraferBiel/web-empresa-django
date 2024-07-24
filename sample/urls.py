
from django.urls import path
from sample import views as sample_views

urlpatterns = [
    path('<int:page_id>/', sample_views.sample, name="sample"),
    
]