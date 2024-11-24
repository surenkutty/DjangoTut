from rest_framework import serializers
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','category_name']
        
class ProductSerializers(serializers.ModelSerializer):
    # category = serializers.CharField(write_only=True)
    class Meta:
        model=Product
        fields=['id','name','category','mrp_price','offer_price','description']
        depth=1
    def validate(self, data):
        special_char="!@#$%^&*()+=,><[]"
        if any(c in special_char for c in data['name']):
            raise serializers.ValidationError("canot use special cheracters")
        return data
    """
    def create(self, validated_data):
        
        category_name = validated_data.pop('category')
        
        
        category, created = Category.objects.get_or_create(category_name=category_name)
        
        
        product = Product.objects.create(category=category, **validated_data)
        return product

    def update(self, instance, validated_data):
        
        category_name = validated_data.pop('category', None)
        
      
        if category_name:
            category, created = Category.objects.get_or_create(category_name=category_name)
            instance.category = category
        

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
    """
