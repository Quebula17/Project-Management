from base.models.list_model import List
from base.serializers import ListSerializer, ListDefaultSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.permissions import IsAdminUser

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ListSerializer
        else:
            return ListDefaultSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(ListViewSet, self).get_permissions()