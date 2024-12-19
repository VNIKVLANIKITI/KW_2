import os
import django
from django.conf import settings

# Указываем путь к проекту Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atomic_habits.settings')

# Настройка окружения Django
django.setup()

# Доступ к настройкам
# my_variable = settings.TG_BOT_TOKEN  # Здесь MY_VARIABLE - имя вашей переменной
my_variable = getattr(settings, 'TG_BOT_TOKEN', 'default_value')


print(f"Значение переменной: {my_variable}")
