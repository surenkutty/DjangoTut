from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','categroy','mrp_price','offer_price','description']
        
    def validate(self, data):
        special_char="!@#$%^&*()+=,><[]"
        if any(c in special_char for c in data['name']):
            raise serializers.ValidationError("canot use special cheracters")
        return data
        