from rest_framework import serializers
from products.models import Product, Product_Images
from users.models import Favorite, Cart


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = ('id', 'image')

class ProductsSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, source='product_image_obj')
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'price', 'items', 'images')
        depth = 1

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductsSerializer(instance.product).data
        return response

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductsSerializer(instance.product).data
        return response