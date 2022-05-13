from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentsGeneralView.as_view()),
    path('<int:pk>', views.StudentsSpecificView.as_view()),
]
