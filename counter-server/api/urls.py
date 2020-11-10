from api import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

urlpatterns = [
    path('counter/', views.CounterView.as_view()),
    path('counter/reset/', views.CounterReset.as_view()),
]

urlpatterns += router.urls
