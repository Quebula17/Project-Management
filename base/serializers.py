from rest_framework import serializers
from base.models.list_model import List
from base.models.card_model import Card
from base.models.comment_model import Comment
from base.models.user_model import User
from base.models.project_model import Project
from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    email_address = serializers.EmailField(validators=[RegexValidator(regex='^[a-zA-Z0-9_.+-]+@(?:[a-zA-Z0-9-]+\.)?iitr\.ac\.in$')])

    class Meta:
        model = User
        fields = (
                  'user_id',
                  'name',
                  'is_admin',
                  'email_address',
                  'enrollment_number',
                  'current_year',
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