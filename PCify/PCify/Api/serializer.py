from rest_framework import serializers 
from Api.models import Api
 
 
class ApiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Api
        fields = ('id',
                  'title',
                  'description',
                  'published')