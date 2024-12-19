from celery import shared_task
from link_telegramm.views import send_telegram_message
from datetime import datetime
from django.conf import settings

'''
@shared_task
def send_reminder(periodicity, event_time):
    # Проверим сколько осталось времени до события на основании поля "action_time"
    print(event_time+periodicity)
    return event_time+periodicity
'''

'''
@shared_task
def send_reminder(habit_id):
        # Ваш токен и chat_id
    bot_token = settings.TG_BOT_TOKEN  #"ваш_бот_токен"  # Замените на токен вашего бота
    chat_id = settings.TG_CHAT_ID  #"ваш_чат_id"  # Замените на ID вашего чата или username
    print(chat_id)
    text = "Напоминание о новой привычке!!!"

    try:
        # Отправка сообщения
        result = send_telegram_message(bot_token, chat_id, text)
        return JsonResponse({"status": "success", "result": result})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    '''
'''
    print('Создаем задачу НАПОМИНАНИЕ')
    from habits.models import habit  # Импорт модели внутри задачи
    try:
        habit_obj = habit.objects.get(id=habit_id)
        send_telegram_message(f"Напоминание для привычки с id {habit_id}")
    except habit.DoesNotExist:
        print(f"Habit with id {habit_id} does not exist.")
        '''

import requests
from celery import shared_task
from django.urls import reverse
from django.conf import settings


@shared_task
def send_reminder(habit_id, message_text):
    print('Отправим напоминание')

    # Получение полного URL к вашему view
    base_url = settings.BASE_URL  # Например, "http://127.0.0.1:8000"
    print(f"Base URL: {base_url}")
    send_message_url = f"{base_url}{reverse('link_telegramm:send_message')}"
    print(f"Send message URL: {send_message_url}")

    # Подготовка данных для отправки (текст сообщения)
    payload = {
        "text": message_text  # Текст сообщения, передаваемый в контроллер
    }

    try:
        # Отправка POST-запроса с текстом сообщения
        response = requests.post(send_message_url, json=payload)
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}")


    

    '''
    # Данные, которые нужно отправить
    data = {
        "habit_id": habit_id,
        "message": "Напоминание о новой привычке!!!"
    }
    '''

'''
    try:
        # Отправка POST-запроса на URL
        #response = requests.post(send_message_url, json=data)
        response = requests.post(send_message_url)
        # Проверка статуса ответа
        response.raise_for_status()  # Бросит исключение при статусах 4xx/5xx
        return JsonResponse({"status": "success", "result": response.json()})
    except requests.RequestException as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
'''