import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardEntryViewSet,
    TeamViewSet,
    UserProfileViewSet,
    WorkoutSuggestionViewSet,
)

codespace_name = os.environ.get('CODESPACE_NAME')
codespace_host = f"{codespace_name}-8000.app.github.dev" if codespace_name else None
if codespace_host:
    base_url = f"https://{codespace_host}"
else:
    base_url = "http://localhost:8000"

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardEntryViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutSuggestionViewSet, basename='workouts')


@api_view(["GET"])
def api_root(request):
    # API root map for the five MongoDB-backed collections.
    return Response(
        {
            "users": f"{base_url}/api/users/",
            "teams": f"{base_url}/api/teams/",
            "activities": f"{base_url}/api/activities/",
            "leaderboard": f"{base_url}/api/leaderboard/",
            "workouts": f"{base_url}/api/workouts/",
        }
    )

urlpatterns = [
    path('', api_root, name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
