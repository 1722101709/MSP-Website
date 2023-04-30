from django.urls import path
from django.contrib import admin
from .import views
urlpatterns = [
    path('', views.home),
    path('company/<str:pk>', views.company),
    path('eligibility/<str:pk>', views.eligibility),
    path('job_notifications', views.jobNotifications),
    path('internships', views.internships),
    path('internship/<str:pk>', views.internship),
    path('interviewTopics', views.interviewTopics),
    path('interview/<str:pk>', views.interview),
    path('contests', views.contests),
    path('contests/register', views.contestsRegistration),
    path('contests/login', views.contestsLogin),
    path('contests/forgotPassword', views.forgotPassword),
    path('contests/home', views.contestsHome),
    path('solutions', views.solutions),
    path('about_us', views.about_us),
    path('admin', views.admin),
    path('1729-ADMIN-1729-ADMIN-1729-ADMIN-1729/', admin.site.urls),
]