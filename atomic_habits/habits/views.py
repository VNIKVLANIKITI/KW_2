from rest_framework import generics
from habits.serializers import HabitSerializer
from habits.models import habit, IsOwnerOrReadOnly
from habits.paginators import habitPaginator
from habits.tasks import send_reminder


class HabiteListAPIView(generics.ListAPIView):
    """ Список привычек текущего пользователя с пагинацией """
    serializer_class = HabitSerializer
    pagination_class = habitPaginator

    def get_queryset(self):
        return habit.objects.filter(creator=self.request.user)


class HabitePublicListAPIView(generics.ListAPIView):
    """ Список публичных привычек """
    serializer_class = HabitSerializer
    pagination_class = habitPaginator
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return habit.objects.filter(is_public=True)


class HabiteCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    queryset = habit.objects.all()
    serializer_class = HabitSerializer
'''
    # постановка периодической задачи напоминания за час до события при создании "Привычки"
    def perform_create(self, serializer):
        # Получаем значение полей event_time из сериализатора
        event_time = serializer.validated_data.get('action_time')
        periodicity = serializer.validated_data.get('periodicity')
        # Сохраняем объект
        serializer.save()
        # ставим задачу
        send_reminder(periodicity, event_time)
'''

class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование привычки """
    serializer_class = HabitSerializer
    queryset = habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = habit.objects.all()
