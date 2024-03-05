from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('get-all-products/', views.GetAllProducts.as_view()),
    path('update-product/', views.UpdateProduct.as_view()),
    path('products/category/<int:category_id>/', views.ProductListByCategory.as_view(), name='product-list-by-category'),
    path('get-all-categories/', views.GetAllCategories.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint for token authentication
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
