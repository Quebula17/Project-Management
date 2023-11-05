from django.db import models
from base.models.project_model import Project


class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='lists')

    def __str__(self):
        return self.list_title