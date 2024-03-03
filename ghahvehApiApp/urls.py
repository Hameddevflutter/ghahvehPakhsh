from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('get-all-products/', views.GetAllPosts),
    path('update-post/', views.UpdatePost),  # Add this line for the UpdatePost view
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
