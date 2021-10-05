from django.contrib.auth.models import Permission
from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(IsActive=True)
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class LoveListViewSet(viewsets.ModelViewSet):
    queryset = LoveList.objects.all()
    serializer_class = LoveListSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = IngredientsTag.objects.all()
    serializer_class = TagSerializer

class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer