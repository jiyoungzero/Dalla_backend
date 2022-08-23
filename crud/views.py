from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Review
from .serializers import MovieListSerializers, ReviewSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def movie_list_create(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializers(movies, many=True)
        
        return Response(data=serializer.data)
    
    if request.method == 'POST':

        serializer = MovieListSerializers(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        


@api_view(['GET'])
def movie_detail_update_delete(request, movie_pk):
    movie =get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieListSerializers(movie)
        
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = MovieListSerializers(instance=movie, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        movie.delete()
        data = {
            'movie':movie_pk
        }
        return Response(data)

# /////////////////////////////////////////////////////////////
# 리뷰 일대다 관계



@api_view(['GET', 'POST'])
def review_list_create(request,movie_pk): 
    #get 요청에서 특정 movie의 리뷰리스트 받기 위해 movie_pk 파라미터로 받음

    if request.method == 'GET':
        # reviews = Review.objects.all()
        # 위 방법보단 아래 방법 추천, 여기서 파라미터로 받은 movie_pk로 리뷰객체 중 해당 무비의 리뷰만 거르면 됨
        reviews = Review.objects.filter(movie=movie_pk)
        serializer = ReviewSerializers(reviews, many=True)
        
        return Response(data=serializer.data)
    
    if request.method == 'POST':

        serializer = ReviewSerializers(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)


@api_view(['GET','PATCH','DELETE'])
def review_detail_update_delete(request, review_pk, movie_pk): 
    #여기도 역시 특정 movie의 review 디테일을 보는거니까 movie_pk 값도 파라미터로 받는게 좋겠지?
    
    # review =get_object_or_404(Review, pk=review_pk)
    # PUT: 대상 리소스의 모든 속성을 수정한다.
    # PATCH: 대상 리소스의 일부 속성만 수정한다.
    # 먼저 Review.objects.filter(movie=movie_pk)로 아까처럼 해당 영화 리뷰만 1차로 거르고
    # 그 다음 review_pk에 해당하는 리뷰로 한번 더 걸러서 특정 리뷰 detail로 찾아가면 좋을 듯
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializers(review)
        
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = ReviewSerializers(instance=review, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        review.delete()
        data = {
            # 'movie':review_pk 
            'review':review_pk #여기도 특정 리뷰를 지워야 하니 키값을 'review'로 해야겠지?
        }
        return Response(data)
    



