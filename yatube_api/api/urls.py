from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register(
    r'posts',
    PostViewSet,
    basename='posts'
)
router_v1.register(
    r'groups',
    GroupViewSet,
    basename='group'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include([
        path('', include(router_v1.urls)),
        path('', include('djoser.urls.jwt')),
    ]))
]
