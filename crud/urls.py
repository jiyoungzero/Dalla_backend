from django.urls import path
from .views import *
from . import views

app_name = "crud"

urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/',views.movie_detail_update_delete),

    # path('<int:movie_pk>/review_list_create/', views.review_list_create),
    # path('<int:review_pk>/review_detail_update_delete/', views.review_detail_update_delete),
    path('<int:movie_pk>/reviews/', views.review_list_create),
    #해당 movie 값의 리뷰목록 끌고온다는걸 url로 설명하기 위해 movie_pk값 받아오는 쪽으로 설계했음
    path('<int:movie_pk>/reviews/<int:review_pk>', views.review_detail_update_delete),

]