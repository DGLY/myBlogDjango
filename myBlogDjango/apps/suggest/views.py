from rest_framework import mixins
from rest_framework import viewsets

from .models import SuggestModel
from .serializer import SuggestDetailSerializer

# Create your views here.

class createSuggestViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):

    queryset = SuggestModel.objects.all()
    serializer_class = SuggestDetailSerializer