from base.models.project_model import Project
from base.serializers import ProjectSerializer, ProjectDefaultSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.permissions import IsAdminUser

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProjectSerializer
        else:
            return ProjectDefaultSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]
        else:
            self.permission_classes = [IsAuthenticated, ]
        return super(ProjectViewSet, self).get_permissions()