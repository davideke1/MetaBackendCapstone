from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns =[
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu-view'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-view'),
    path('restaurant/booking/', include(router.urls)),
]