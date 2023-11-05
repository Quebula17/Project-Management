from base.models.list_model import List
from base.serializers import ListSerializer, ListDefaultSerializer
from rest_framework import viewsets

class ListViewSet(viewsets.ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ListSerializer
        else:
            return ListDefaultSerializer