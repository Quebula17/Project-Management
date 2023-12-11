from base.models.card_model import Card
from base.serializers import CardSerializer, CardDefaultSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.permissions import IsAdminUser

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CardSerializer
        else:
            return CardDefaultSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(CardViewSet, self).get_permissions()