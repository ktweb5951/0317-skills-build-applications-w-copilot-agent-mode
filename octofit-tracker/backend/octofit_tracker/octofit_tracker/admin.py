from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "level")
    search_fields = ("name", "email")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
    search_fields = ("name", "city")


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("user_email", "team_name", "activity_type", "duration_minutes")
    search_fields = ("user_email", "team_name", "activity_type")


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ("user_email", "points", "rank")
    search_fields = ("user_email",)
    ordering = ("rank",)


@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ("user_email", "workout_name", "difficulty", "target")
    search_fields = ("user_email", "workout_name", "target")
