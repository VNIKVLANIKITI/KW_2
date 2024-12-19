from django.http import JsonResponse
from .utils import send_telegram_message
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_message_view(request):
    # Проверяем метод запроса
    if request.method == "POST":
        try:
            # Парсим тело запроса как JSON
            body = json.loads(request.body)

            # Получаем параметр "text"
            text = body.get("text")
            if not text:
                return JsonResponse({"status": "error", "message": "Missing 'text' parameter"}, status=400)

            # Ваш токен и chat_id
            bot_token = settings.TG_BOT_TOKEN  # Токен вашего Telegram-бота
            chat_id = settings.TG_CHAT_ID  # ID вашего чата

            # Логирование для проверки
            print(f"Sending to chat_id: {chat_id}, text: {text}")

            # Отправка сообщения
            result = send_telegram_message(bot_token, chat_id, text)

            # Возврат успешного ответа
            return JsonResponse({"status": "success", "result": result})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON payload"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid HTTP method"}, status=405)
