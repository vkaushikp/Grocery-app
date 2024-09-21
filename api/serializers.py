from rest_framework import serializers
from store.models import GroceryItem
from store.utils import generate_category

class GroceryItemSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = GroceryItem
        fields = ['name', 'quantity', 'category']

    def create(self, validated_data):
        if GroceryItem.objects.filter(name=validated_data['name'], user=self.context['request'].user).exists():
            raise serializers.ValidationError("Item already exists")
        category = generate_category(validated_data['name'])
        user = self.context['request'].user
        return GroceryItem.objects.create(category=category, user=user, **validated_data)
    
    def update(self, instance, validated_data):
        if GroceryItem.objects.filter(name=validated_data['name'], user=self.context['request'].user).exists():
            raise serializers.ValidationError("Item already exists")
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.category = generate_category(validated_data.get('name', instance.name))
        instance.save()
        return instance