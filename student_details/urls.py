from django.contrib import admin
from django.urls import path
from students import views

admin.site.site_header = 'Student Details'
admin.site.site_title = 'Admin Portal | Student Details'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('student/<int:student_id>/', views.student, name="student"),
]
