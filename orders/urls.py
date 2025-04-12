from django.urls import path
from .views import OrderListView, OrderCreateView, OrderDetailView

urlpatterns = [
    path('order/', OrderListView.as_view(), name='order-list'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/<int:id>/', OrderDetailView.as_view(), name='order-detail'),
]