from django.urls import path, include
from base.views import authorization, project_viewset, user_viewset, list_viewset, card_viewset, comment_viewset, authenticate
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'projects', project_viewset.ProjectViewSet,basename="project")
router.register(r'users', user_viewset.UserViewSet,basename="user")
router.register(r'lists', list_viewset.ListViewSet,basename="list")
router.register(r'cards', card_viewset.CardViewSet,basename="card")
router.register(r'comments', comment_viewset.CommentViewSet,basename="comment")

urlpatterns = [
    path('', include(router.urls)),
    path('oauth/authorize/', authorization.oauth_authorize, name='oauth_authorize'),
    path('oauth/callback/', authorization.get_access_token, name='get_access_token'),
    path('get_user_data/', authorization.get_user_data, name='get_user_data'),


    path('token/', authenticate.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]