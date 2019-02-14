from django.urls import path
from .views import index_view,category_detail

app_name = "category"

urlpatterns = [
    path('', index_view),
    path('<str:slug>',category_detail),
]