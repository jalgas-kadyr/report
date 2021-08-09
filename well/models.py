from django.db.models import *


class Well(Model):
    name = CharField(max_length=30)
    plan = IntegerField()
    fact = IntegerField()
    speed = IntegerField()
    master = CharField(max_length=30)
    supervisor = CharField(max_length=30)
    driller = CharField(max_length=30)
    appointment = CharField(max_length=30)
    type = CharField(max_length=50)
    customer = CharField(max_length=30)
    xcor = CharField(max_length=10)
    ycor = CharField(max_length=10)
    complex = CharField(max_length=30)
    altitude = IntegerField()
    chief = CharField(max_length=30)
    preparation_begin = DateField()
    begin_date = DateField()
    planned_end = DateField()

    def __str__(self):
        return self.name


class WellRoad(Model):
    well = CharField(max_length=30)
    x = IntegerField()
    y = IntegerField()
    z = IntegerField()

    def __str__(self):
        return self.well


class Report(Model):
    number = IntegerField()
    well = CharField(max_length=30)
    fact = IntegerField()
    drilled = IntegerField()
    drilled24 = IntegerField()
    last_drilled = IntegerField()
    to_drill = IntegerField()
    last_column = IntegerField()
    next_column = IntegerField()
    diameter = IntegerField()
    days = IntegerField()
    meeting = TimeField()
    days_without_incident = IntegerField()
    days_after_uncountable_case = IntegerField()
    date = DateField()

    def __str__(self):
        return self.well + ' ' + str(self.number)


class Operation(Model):
    group = CharField(max_length=30)
    operation = CharField(max_length=30)
    code = CharField(max_length=10)
    description = CharField(max_length=1000)
    type = CharField(max_length=1)
    well = CharField(max_length=30)
    number = IntegerField()
    notes = CharField(max_length=500)
    begin_time = TimeField()
    end_time = TimeField()
    date = DateField()

    def __str__(self):
        return str(self.code)


class OperationCode(Model):
    group = CharField(max_length=30)
    operation = CharField(max_length=30)
    code = CharField(max_length=2)
    type = CharField(max_length=1)

    def __str__(self):
        return str(self.code)


class Consumptions(Model):
    type = CharField(max_length=30)
    name = CharField(max_length=30)
    well = CharField(max_length=30)
    count = IntegerField()
    type_m = CharField(max_length=30)
    date = DateField()