from base.models.comment_model import Comment
from base.serializers import CommentSerializer, CommentDefaultSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.permissions import IsAdminUser

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommentSerializer
        else:
            return CommentDefaultSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(CommentViewSet, self).get_permissions()