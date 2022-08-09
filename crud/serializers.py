from rest_framework import serializers
from .models import *

class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'content','created_at','updated_at')
        
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'