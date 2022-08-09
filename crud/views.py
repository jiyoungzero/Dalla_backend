from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie
from .serializers import MovieListSerializers
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