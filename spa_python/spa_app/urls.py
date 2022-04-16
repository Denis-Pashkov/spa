
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Table_view.as_view(), name='spa_app'),
    path('api/v1/spa/', views.TableApiView.as_view(), name='spa_app_api'),
]
