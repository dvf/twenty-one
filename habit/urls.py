from django.conf.urls import url

from habit import views


urlpatterns = [
    url('^create/$', views.HabitCreateView.as_view(), name='create'),
    url('^log/complete/$', views.DailyLogCompleteView.as_view(), name='log-complete'),
    url('^$', views.HabitView.as_view(), name='index'),
]
