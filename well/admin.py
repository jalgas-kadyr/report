from django.contrib import admin
from .models import *


admin.site.register(WellRoad)
admin.site.register(Well)
admin.site.register(Report)
admin.site.register(Operation)
admin.site.register(OperationCode)
admin.site.register(Consumptions)

