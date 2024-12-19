from rest_framework.exceptions import ValidationError
from django.apps import apps
from rest_framework import serializers

def ValidateHabitReward(fields):
    def validator(serializer, attrs):
        habit_link = attrs.get('habit_link')
        myreward = attrs.get('myreward')
        print('ПОЛЕ', habit_link)
        print('ПОЛЕ', myreward)
        # Пример проверки: если habit_link пустой, а myreward задан
        if habit_link and myreward:
            raise ValidationError("Нельзя одновременно выбрать связанную привычку и указать вознаграждение.")

    return validator

class ValidateLongTime:
    def __init__(self, field_name=None):
        self.field_name = field_name

    def __call__(self, value):
        try:
            value = float(value)  # Преобразуем значение в число
        except (TypeError, ValueError):
            raise ValidationError('Значение должно быть числом.')

        if value > 120:
            raise ValidationError(f'Значение для поля "{self.field_name}" не должно превышать 120.')
        

class ValidateHabitLink_myreward:
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        # Убедимся, что работаем с ID, а не с объектом
        if hasattr(value, 'id'):
            value = value.id

        Habit = apps.get_model('habits', 'habit')  # Получаем модель по имени

        try:
            habit_instance = Habit.objects.get(id=value)
            if habit_instance.myreward:
                raise serializers.ValidationError(
                    f"У объекта habit с id {value} не должно быть заполнено поле myreward."
                )
        except Habit.DoesNotExist:
            raise serializers.ValidationError(f"Объект habit с id {value} не существует.")

class ValidateHabitLink_is_nice:
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        # Убедимся, что работаем с ID, а не с объектом
        if hasattr(value, 'id'):
            value = value.id

        Habit = apps.get_model('habits', 'habit')  # Получаем модель по имени

        try:
            habit_instance = Habit.objects.get(id=value)
            if habit_instance.is_nice:  # Проверяем поле is_nice
                raise serializers.ValidationError(
                    f"У объекта habit с id {value} поле is_nice не должно быть заполнено."
                )
        except Habit.DoesNotExist:
            raise serializers.ValidationError(f"Объект habit с id {value} не существует.")