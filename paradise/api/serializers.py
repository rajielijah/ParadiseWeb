from rest_framework import serializers
from paradise.models import *

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = (
            'title',
            'price',
            'category',
            'description',
            'image',
            'slug',
            'discount_price'
        )

    def get_category(self, obj):
        return obj.get_category_display()


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField

    class Meta:
        model = OrderItem
        fields = (
            'item',
            'quantity',
        )

    def get_item(self, obj):
        return ItemSerializer(obj.item).data

class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'order_item',
            'item',
            'status',
            'user'
        )
    def get_order_item(self, obj):
        return OrderItemSerializer(obj.item.all(), many=True).data

class ItemDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = (
            'title',
            'price',
            'discount_price',
            'category',
            'slug',
            'description',
            'image',
            )

    def get_category(self, obj):
        return obj.get_category_display()