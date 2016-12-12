from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property

from common.models import BaseModel


class Habit(BaseModel):
    name = models.CharField(max_length=200, help_text="What is your goal?")

    start_date = models.DateField(help_text="When do you want to begin?")

    # FK
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    @property
    def is_over(self):
        return (timezone.now().date() - self.start_date).days > 21

    @cached_property
    def is_fail(self):
        daily_logs = DailyLog.objects.filter(habit=self)
        for day in daily_logs:
            if day.accomplished is False:
                return True
        return False


class DailyLog(BaseModel):
    accomplished = models.BooleanField(default=False)
    day = models.DateField()

    # FK
    habit = models.ForeignKey('habit.Habit')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='daily_logs')

    @property
    def is_over(self):
        return (timezone.now().date() - self.day).days > 0

    @property
    def can_complete(self):
        if self.accomplished is True:
            return False
        return timezone.now().date() == self.day

    @property
    def ending_today(self):
        return self.day == timezone.now().date()

    @property
    def get_context(self):
        if self.is_over and self.accomplished is False:
            return 'fail'
        elif self.accomplished is True:
            return 'win'
        elif self.ending_today:
            return 'warning'
        else:
            return 'primary'

    def integer_day(self):
        return self.day.weekday()
