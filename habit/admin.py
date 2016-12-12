from django.contrib import admin

from habit.models import DailyLog, Habit


@admin.register(DailyLog, Habit)
class HabitAdmin(admin.ModelAdmin):
    pass
