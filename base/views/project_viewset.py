from base.models.project_model import Project
from base.serializers import ProjectSerializer, ProjectDefaultSerializer
from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProjectSerializer
        else:
            return ProjectDefaultSerializer
