from django.contrib.auth import get_user_model
from base.serializers import UserSerializer
from rest_framework import viewsets
from base.permissions import IsAdminUser

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]
        return super(UserViewSet, self).get_permissions()