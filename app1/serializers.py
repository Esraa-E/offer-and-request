from rest_framework import serializers
from .models import *

class offerSerializer(serializers.ModelSerializer):
    class Meta:
        model=offer
        fields='__all__'


class addofferSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddOffer
        fields='__all__'
        


class requesrSerializer(serializers.ModelSerializer):
    class Meta:
        model=request
        fields='__all__'



class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'
