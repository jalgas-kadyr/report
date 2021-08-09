from django.db.models import *


class Master(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    username = CharField(max_length=30)
    password = CharField(max_length=30)
    status = BooleanField()
    current_well = CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname


class Dispatcher(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    username = CharField(max_length=30)
    password = CharField(max_length=30)
    status = BooleanField()
    complex = CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname


class Supervisor(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    username = CharField(max_length=30)
    password = CharField(max_length=30)
    status = BooleanField()
    current_well = CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname


class Chief(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    username = CharField(max_length=30)
    password = CharField(max_length=30)
    status = BooleanField()
    current_well = CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname
