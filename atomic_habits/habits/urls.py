from habits.apps import HabitsConfig
from django.contrib import admin
from django.urls import path
from habits.views import HabiteListAPIView, HabiteCreateAPIView, HabitePublicListAPIView, HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/", HabiteListAPIView.as_view(), name="habit-list"), # Список привычек текущего пользователя с пагинацией.
    path("habit/create/", HabiteCreateAPIView.as_view(), name="habit-create"), # Создание привычки.
    path("habit/public", HabitePublicListAPIView.as_view(), name="habit-public-list"), # Список публичных привычек.
    path("habit/update/<int:pk>", HabitUpdateAPIView.as_view(), name="habit-update"), #Редактирование привычки.
    path("habit/delete/<int:pk>", HabitDestroyAPIView.as_view(), name="habit-delete"), #Удаление привычки
]
