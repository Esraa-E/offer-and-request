from rest_framework import serializers
from .models import *



#multiple images
class offerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=offerImages
        fields=["id","offerimg","image"]
#end multiple images

# احذفي من عندك offerSerializer وحطي ده بداله 
class offerSerializer(serializers.ModelSerializer):
    img= offerImageSerializer(many=True,read_only=True)
    uploaded_images=serializers.ListField(
        child=serializers.ImageField(max_length=1000000,allow_empty_file=False,use_url=False),
        write_only=True
    )
    class Meta:
        model=offermodel
        fields=["phone_number","rent_start_time","rent_finish_time","price","favorit","location","discount","level","bedrooms","bathrooms","area","description","conditions","ava","rev","furnished","viewer","video","img","uploaded_images"]
        
    def create(self,validated_data):
        uploaded_images =validated_data.pop("uploaded_images")
        offerModel=offermodel.objects.create(**validated_data)
        for image in uploaded_images:
            offer_image=offerImages.objects.create(offerimg=offerModel,image=image)
            
        return offermodel
        
        
#اااااااااااااااااا

class addofferSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddOffermodel
        fields='__all__'
        


class requesrSerializer(serializers.ModelSerializer):
    class Meta:
        model=requestmodel
        fields='__all__'



class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model=commentmodel
        fields='__all__'
