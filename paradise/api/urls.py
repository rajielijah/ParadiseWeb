from django.urls import path, include
from .views import ItemListView, OrderItemDeleteView, ItemDetailView, OrderDetailView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='Item'),
    path('items/<pk>', ItemDetailView.as_view(), name='Item_Detail'),
    path('order-detail/', OrderDetailView.as_view(), name='order-detail'),
    path('order-detail/<pk>/delete/', OrderItemDeleteView.as_view(), name='order-detail-delete')
]