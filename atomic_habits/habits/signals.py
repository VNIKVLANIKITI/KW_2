from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta, datetime
from habits.models import habit
from habits.tasks import send_reminder

@receiver(post_save, sender=habit)
def schedule_habit_reminder(sender, instance, created, **kwargs):
    if created:  # Только при создании объекта
        # Получаем текущее время
        now = datetime.now()
        
        # Получаем время действия привычки и соединяем с текущей датой
        habit_time = datetime.combine(now.date(), instance.action_time)
        
        # Рассчитываем задержку: за 1 час до времени действия привычки
        delay = (habit_time - timedelta(hours=1) - now).total_seconds()

        # Если задержка отрицательная, значит время действия уже прошло, и нужно скорректировать
        if delay < 0:
            periodicity_map = {
                'every_hour': timedelta(hours=1),
                'twice_day': timedelta(hours=12),
                'three_times_day': timedelta(hours=8),
                'every_day': timedelta(days=1),
                'every_two_days': timedelta(days=2),
                'every_three_days': timedelta(days=3),
                'every_five_days': timedelta(days=5),
                'weekly': timedelta(weeks=1),
            }
            interval = periodicity_map.get(instance.periodicity, timedelta(days=1))
            delay += interval.total_seconds()  # Добавляем интервал, чтобы время было в будущем

        # Генерация текста сообщения
        message_text = f"Напоминание для привычки: {instance.action_name}. Следующее действие в {instance.action_time}."

        # Отправка задачи Celery
        send_reminder.apply_async((instance.id, message_text), countdown=delay)
