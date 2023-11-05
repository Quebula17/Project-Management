from django.contrib import admin
from base.models.list_model import List
from base.models.card_model import Card
from base.models.comment_model import Comment
from django.contrib.auth import get_user_model
from base.models.project_model import Project

User = get_user_model()


admin.site.register(Project)
admin.site.register(User)
admin.site.register(List)
admin.site.register(Card)
admin.site.register(Comment)



