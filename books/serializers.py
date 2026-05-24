from rest_framework import serializers
from .models import book

class Bookserializer(serializers.ModelSerializer):

    class Meta:
        model = book
        fields = '__all__'

    
    def validate_movie(self,value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "movie name is too short"
            )
        return value
