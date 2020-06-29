from .serializers import (
    ItemSerializer, OrderSerializer, OrderItemSerializer, ItemDetailSerializer
)
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from paradise.models import *
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)


class ItemListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()


class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        try:
            order = Order.objects.get(user=self.request.user, ordered=True)
            return order
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")

class OrderItemDeleteView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = OrderItem.objects.all()