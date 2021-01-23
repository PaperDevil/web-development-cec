from peewee import *
from datetime import datetime

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Worker(BaseModel):
    id = BigIntegerField(primary_key=True)
    first_name = CharField(max_length=64, verbose_name="Имя")
    last_name = CharField(max_length=64, verbose_name="Фамилия")
    age = IntegerField()
    post = CharField(max_length=64, verbose_name="Должность")


class Device(BaseModel):
    id = BigIntegerField(primary_key=True)
    name = CharField(max_length=64, verbose_name="Тип девайса")
    price = IntegerField(verbose_name="Цена")
    worker = ForeignKeyField(Worker, backref="devices")


class Operation(BaseModel):
    id = BigIntegerField(primary_key=True)
    timestamp = DateTimeField(verbose_name="Время записи", default=datetime.now)
    worker = ForeignKeyField(Worker)
    device = ForeignKeyField(Device)
