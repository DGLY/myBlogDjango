from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import BlogModel
from .serializer import BlogSerializer,BlogDetailSerializer

class BlogsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

# Create your views here.
class BlogsListViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):

    queryset = BlogModel.objects.all()
    lookup_field = 'identify'
    pagination_class = BlogsPagination

    def get_serializer_class(self):

        if self.kwargs == {}:

            return BlogSerializer
        else:

            return BlogDetailSerializer