from base.models.card_model import Card
from base.serializers import CardSerializer, CardDefaultSerializer
from rest_framework import viewsets

class CardViewSet(viewsets.ModelViewSet):

    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CardSerializer
        else:
            return CardDefaultSerializer