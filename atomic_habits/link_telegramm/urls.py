from link_telegramm.apps import LinkTelegrammConfig
from django.urls import path
from . import views

app_name = LinkTelegrammConfig.name

urlpatterns = [
    path('send-message/', views.send_message_view, name='send_message'),
]
