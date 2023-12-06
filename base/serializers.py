from rest_framework import serializers
from base.models.list_model import List
from base.models.card_model import Card
from base.models.comment_model import Comment
from base.models.project_model import Project
from django.core.validators import RegexValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[RegexValidator(regex='^[a-zA-Z0-9_.+-]+@(?:[a-zA-Z0-9-]+\.)?iitr\.ac\.in$')])

    class Meta:
        model = User
        fields = (
                  'id',
                  'username',
                  'is_admin',
                  'email',
                  'current_year',
                  'first_name',
                  'last_name'
                )

class ProjectSerializer(serializers.ModelSerializer):
    maintainer = UserSerializer()
    team_members = UserSerializer(many=True)
    # github_link = serializers.URLField(validators = [RegexValidator(regex='https?://(www\.)?github\.com/[A-Za-z0-9-]+/[A-Za-z0-9_.-]+')])

    class Meta:
        model = Project
        fields = (
                  'project_id',
                  'project_name',
                  'description',
                  'maintainer',
                  'team_members',
                  'github_link',
                  )
        
class ProjectDefaultSerializer(serializers.ModelSerializer):
    github_link = serializers.URLField(validators = [RegexValidator(regex='https?://(www\.)?github\.com/[A-Za-z0-9-]+/[A-Za-z0-9_.-]+')])

    class Meta:
        model = Project
        fields = (
                  'project_id',
                  'project_name',
                  'description',
                  'maintainer',
                  'team_members',
                  'github_link',
                  )


class ListSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = List
        fields = (
            'list_id',
            'list_title',
            'project',
            )

class ListDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = (
            'list_id',
            'list_title',
            'project',
            )

class CardSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True)
    task_list = ListSerializer()

    class Meta:
        model = Card
        fields = (
                  'card_id',
                  'card_title',
                  'is_verified',
                  'assigned_users',
                  'task_list',
                  'description',
                  )
        
class CardDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = (
                'card_id',
                'card_title',
                'is_verified',
                'assigned_users',
                'task_list',
                'description',
            )

class CommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    card = CardSerializer()

    class Meta:
        model = Comment
        fields = (
                  'comment_id',
                  'card',
                  'sender',
                  'contents'
                  )
        
class CommentDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
                  'comment_id',
                  'card',
                  'sender',
                  'contents'
                  )
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name

        return token