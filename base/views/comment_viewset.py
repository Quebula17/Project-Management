from base.models.comment_model import Comment
from base.serializers import CommentSerializer, CommentDefaultSerializer
from rest_framework import viewsets

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommentSerializer
        else:
            return CommentDefaultSerializer