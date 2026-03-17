from django.core.management.base import BaseCommand

from octofit_tracker.models import (
    Activity,
    LeaderboardEntry,
    Team,
    UserProfile,
    WorkoutSuggestion,
)


class Command(BaseCommand):
    help = "octofit_db 데이터베이스에 테스트 데이터를 입력합니다."

    def handle(self, *args, **options):
        UserProfile.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        WorkoutSuggestion.objects.all().delete()

        Team.objects.bulk_create(
            [
                Team(name="marvel team", city="New York"),
                Team(name="dc team", city="Gotham"),
            ]
        )

        UserProfile.objects.bulk_create(
            [
                UserProfile(name="Tony Stark", email="tony@marvel.com", level="advanced"),
                UserProfile(name="Steve Rogers", email="steve@marvel.com", level="intermediate"),
                UserProfile(name="Bruce Wayne", email="bruce@dc.com", level="advanced"),
                UserProfile(name="Clark Kent", email="clark@dc.com", level="intermediate"),
            ]
        )

        Activity.objects.bulk_create(
            [
                Activity(
                    user_email="tony@marvel.com",
                    team_name="marvel team",
                    activity_type="HIIT",
                    duration_minutes=45,
                ),
                Activity(
                    user_email="steve@marvel.com",
                    team_name="marvel team",
                    activity_type="Running",
                    duration_minutes=60,
                ),
                Activity(
                    user_email="bruce@dc.com",
                    team_name="dc team",
                    activity_type="Strength",
                    duration_minutes=50,
                ),
                Activity(
                    user_email="clark@dc.com",
                    team_name="dc team",
                    activity_type="Cycling",
                    duration_minutes=40,
                ),
            ]
        )

        LeaderboardEntry.objects.bulk_create(
            [
                LeaderboardEntry(user_email="tony@marvel.com", points=980, rank=1),
                LeaderboardEntry(user_email="bruce@dc.com", points=930, rank=2),
                LeaderboardEntry(user_email="steve@marvel.com", points=890, rank=3),
                LeaderboardEntry(user_email="clark@dc.com", points=850, rank=4),
            ]
        )

        WorkoutSuggestion.objects.bulk_create(
            [
                WorkoutSuggestion(
                    user_email="tony@marvel.com",
                    workout_name="Arc Reactor Intervals",
                    difficulty="hard",
                    target="cardio",
                ),
                WorkoutSuggestion(
                    user_email="steve@marvel.com",
                    workout_name="Shield Circuit",
                    difficulty="medium",
                    target="full body",
                ),
                WorkoutSuggestion(
                    user_email="bruce@dc.com",
                    workout_name="Batcave Strength Block",
                    difficulty="hard",
                    target="strength",
                ),
                WorkoutSuggestion(
                    user_email="clark@dc.com",
                    workout_name="Krypton Core Session",
                    difficulty="medium",
                    target="core",
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("테스트 데이터 적재 완료"))
