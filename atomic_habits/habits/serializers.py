from rest_framework import serializers
from habits.models import habit
from habits.validators import ValidateHabitReward, ValidateLongTime, ValidateHabitLink_myreward, ValidateHabitLink_is_nice


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = habit
        fields = ('action_name', 'action_time', "is_nice",'action_place', 'habit_link', 'periodicity', 'time_long', 'is_public', 'myreward')

    def validate_habit_vs_revard(self, attrs):
        # Вызываем валидатор
        ValidateHabitReward(fields=['habit_link', 'myreward'])(self, attrs)
        return attrs
    def validate_time_long(self, value):
        validator = ValidateLongTime(field_name="time_long")
        validator(value)
        return value
    def validate_habit_link_reward(self, value):
        # Вызываем валидатор для проверки поля habit_link
        validator = ValidateHabitLink_myreward(field_name="habit_link")
        validator(value)
        return value
    def validate_habit_link_is_nice(self, value):
        # Вызываем валидатор для проверки поля habit_link
        validator = ValidateHabitLink_is_nice(field_name="habit_link")
        validator(value)
        return value