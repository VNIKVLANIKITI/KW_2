from django.db import models
from django.conf import settings
from django.utils import timezone
from rest_framework import permissions

# место
class place(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


# действие
class action(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}" 

    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'

# вознаграждение
class reward(models.Model):
    id = models.AutoField(primary_key=True)  # Поле с автоинкрементом
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}" 

    class Meta:
        verbose_name = 'Вознаграждение'
        verbose_name_plural = 'Вознаграждения'

#Привычка:
class habit(models.Model):
    id = models.AutoField(primary_key=True)  # Поле с автоинкрементом
    # Пользователь — создатель привычки.
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Создатель')
    # Место — место, в котором необходимо выполнять привычку.    
    action_place = models.ForeignKey(place, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Место выполнения')
    # Время — время, когда необходимо выполнять привычку.
    action_time = models.TimeField(default=timezone.now, verbose_name='Время выполнения')
    # Действие — действие, которое представляет собой привычка.
    action_name = models.ForeignKey(action, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Действие')
    # Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
    is_nice = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    # Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
    habit_link = models.ForeignKey('habits.habit', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Связанная привычка')
    # Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
    periodicity_CHOICES = [
        ('every_hour', 'каждый час'),
        ('twice_day', 'дважды в день'),
        ('three_times_day', 'трижды в день'),
        ('every_day', 'каждый день'),
        ('every_two_days', 'каждые два дня'),
        ('every_three_days', 'каждые три дня'),
        ('every_five_days', 'каждые пять дней'),
        ('weekly', 'еженедельно'),
    ]
    periodicity = models.CharField(max_length=20, choices=periodicity_CHOICES, default='every_day', verbose_name='Периодичность')
    # Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
    time_long = models.IntegerField(default=0, verbose_name='Продолжительность выполнения (мин)')
    # Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
    myreward = models.ForeignKey(reward, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Вознаграждение')
    # Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.
    is_public = models.BooleanField(default=False, verbose_name='Публичная')

    def __str__(self):
        # я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
        return f" я буду {self.action_name} в {self.action_time} в {self.action_place}" 
    
    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет редактировать объект только его владельцу.
    Остальным пользователям разрешен только доступ на чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ на чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешаем запись только владельцу объекта
        return obj.owner == request.user
