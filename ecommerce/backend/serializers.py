from django.db.models import fields
from django.db.models.fields import files
from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=['id','first_name', 'last_name', 'email', 'username', 'password','avt']
        extra_kwargs ={
            'password' :{'write_only':'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description","price", "sold","instruction", "origin","IsActive", "images", "category"]

class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields=["id", "name"]

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model=ProductImage
        fields=["id","img"] 

class RatingSerializer(ModelSerializer):
    class Meta:
        model=Rating
        fields=["id","dayandtime","ratingpoint", "ratingcomment","img","product","user"] 
class LoveListSerializer(ModelSerializer):
    class Meta:
        model= LoveList
        fields= '__all__'

class TagSerializer(ModelSerializer):
    class Meta:
        model= IngredientsTag
        fields= '__all__'

class IngredientSerializer(ModelSerializer):
    class Meta:
        model= Ingredients
        fields= '__all__'