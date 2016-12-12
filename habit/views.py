from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import FormView
from django.views.generic import TemplateView

from habit.forms import HabitCreateForm
from habit.models import Habit, DailyLog


class HabitView(LoginRequiredMixin, TemplateView):
    template_name = 'habit/habit.html'

    def get_context_data(self, **kwargs):
        context = super(HabitView, self).get_context_data(**kwargs)

        # Get the List of Habits for a User
        habits = Habit.objects.filter(user=self.request.user)

        context['habits'] = habits
        context['no_habits'] = habits.count() == 0
        return context


class HabitCreateView(LoginRequiredMixin, FormView):
    template_name = 'habit/habit-create.html'
    form_class = HabitCreateForm
    success_url = reverse_lazy('habit:index')

    def form_valid(self, form):
        habit = form.save(commit=False)
        habit.user = self.request.user
        habit.save()

        # Create the DailyLogs for each day
        daily_logs = []
        today = timezone.now().date()
        for i in range(0, 21):
            daily_logs.append(
                DailyLog(
                    accomplished=False,
                    habit=habit,
                    user=self.request.user,
                    day=today + timedelta(days=i)
                )
            )
        DailyLog.objects.bulk_create(daily_logs)
        messages.success(self.request, "Congratulations and Good Luck")
        return super(HabitCreateView, self).form_valid(form)


class DailyLogCompleteView(LoginRequiredMixin, View):

    def post(self, request):
        log = request.POST.get('log')
        log = get_object_or_404(DailyLog, pk=int(log))
        if log.can_complete and log.user == self.request.user:
            log.accomplished = True
            log.save()
            messages.success(request, "Well Done!")
        else:
            messages.error(request, "An error occurred.")
        return redirect('habit:index')