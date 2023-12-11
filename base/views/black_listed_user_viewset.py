from base.models.black_listed_users import BlacklistedUser
from base.serializers import BlacklistedUserSerializer, BlacklistedUserDefaultSerializer
from rest_framework import viewsets
from base.permissions import IsAdminUser

class BlacklistedUserViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser]
    queryset = BlacklistedUser.objects.all()
    serializer_class = BlacklistedUserSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return BlacklistedUserSerializer
        else:
            return BlacklistedUserDefaultSerializer

