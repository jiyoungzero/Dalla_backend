from rest_framework import serializers
from .models import *

class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'