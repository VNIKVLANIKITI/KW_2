from django.contrib import admin
from users.models import User
from habits.models import habit, place, action, reward

admin.site.register(User)
admin.site.register(habit)
admin.site.register(place)
admin.site.register(action)
admin.site.register(reward)
