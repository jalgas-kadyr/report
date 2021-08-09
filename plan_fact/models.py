from django.db.models import *


class Plan(Model):
    well = CharField(max_length=30)
    date = DateField()
    plan = IntegerField()
    fact = IntegerField(null=True)
    difference = IntegerField()
