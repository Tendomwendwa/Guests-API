from django.urls import path
from guests import views


urlpatterns = [
    path('guests/', views.guest_list),
    path('guests/<int:pk>/', views.guest_detail),
]