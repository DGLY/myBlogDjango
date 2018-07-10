from rest_framework import serializers

from .models import BlogModel

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogModel
        fields = ['author','title','identify','digest','category','add_time']


class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogModel
        fields = '__all__'