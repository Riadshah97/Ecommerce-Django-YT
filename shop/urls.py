from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



app_name="shop"
urlpatterns = [
     path('' ,views.home),
     path('category/<slug:val>', views.Categoryview.as_view(),name="category"),
     path('product-detail/<int:pk>', views.ProductDetails.as_view(),name="product-detail"),

]+static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
