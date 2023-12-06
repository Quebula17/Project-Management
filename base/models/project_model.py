from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    maintainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintained_projects')
    team_members = models.ManyToManyField(User, related_name='projects')
    github_link = models.URLField()

    def __str__(self):
        return self.project_name