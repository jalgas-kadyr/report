from django.contrib import admin
from .models import *


admin.site.register(Master)
admin.site.register(Supervisor)
admin.site.register(Dispatcher)
admin.site.register(Chief)