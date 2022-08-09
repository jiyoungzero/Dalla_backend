from django.urls import path
from .views import *
from . import views

app_name = "crud"

urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/',views.movie_detail_update_delete),


    # path('review_create/', views.review_create),
    path('<int:movie_pk>/review_list_create/', views.review_list_create),
    path('<int:review_pk>/review_detail_update_delete/', views.review_detail_update_delete),

]