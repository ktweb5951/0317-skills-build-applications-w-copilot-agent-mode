from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class CollectionEndpointTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.bulk_create(
            [
                Team(name="marvel team", city="New York"),
                Team(name="dc team", city="Gotham"),
            ]
        )

        UserProfile.objects.bulk_create(
            [
                UserProfile(name="Tony Stark", email="tony@marvel.com", level="advanced"),
                UserProfile(name="Bruce Wayne", email="bruce@dc.com", level="advanced"),
            ]
        )

        Activity.objects.create(
            user_email="tony@marvel.com",
            team_name="marvel team",
            activity_type="HIIT",
            duration_minutes=45,
        )
        LeaderboardEntry.objects.create(user_email="tony@marvel.com", points=980, rank=1)
        WorkoutSuggestion.objects.create(
            user_email="tony@marvel.com",
            workout_name="Arc Reactor Intervals",
            difficulty="hard",
            target="cardio",
        )

    def test_api_root_returns_collection_links(self):
        response = self.client.get(reverse("api-root"))
        self.assertEqual(response.status_code, 200)
        for key in ["users", "teams", "activities", "leaderboard", "workouts"]:
            self.assertIn(key, response.data)

    def test_users_endpoint(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get("/api/activities/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
