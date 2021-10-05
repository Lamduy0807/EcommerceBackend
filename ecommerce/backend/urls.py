from django import urls
from django.urls import path
from django.urls.conf import include
from rest_framework import routers, viewsets
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category',views.CategoryViewSet)
router.register('img',views.ProductImageViewSet)
router.register('rating', views.RatingViewSet)
router.register("lovelist",views.LoveListViewSet)
router.register("tag",views.TagViewSet)
router.register("ingredient",views.IngredientsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
