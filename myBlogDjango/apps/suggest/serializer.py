from rest_framework import serializers

from .models import SuggestModel

class SuggestDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuggestModel
        fields = '__all__'