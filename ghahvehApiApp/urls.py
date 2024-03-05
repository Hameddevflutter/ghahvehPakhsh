from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('get-all-products/', views.GetAllProducts),
    path('update-product/', views.UpdateProduct),  
    path('products/category/<int:category_id>/', views.ProductListByCategory.as_view(), name='product-list-by-category'),
    path('get-all-categories/', views.GetAllCategories),
     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
