from peewee import *
from datetime import datetime

db = SqliteDatabase('database.db')
# Хорошей практикой является вынесение путей в переменные окружения,
# тогда функция выглядела бы так: SqliteDatabase(getenv('DATABASE_PATH'))


class TodoItem(Model):
    id = IntegerField(verbose_name="ID", primary_key=True, index=True)
    text = CharField(max_length=64, verbose_name="Заголовок", null=False)
    datetime_of_creation = DateTimeField(default=datetime.now, verbose_name="Дата и время создания", null=False)
    is_complete = BooleanField(default=False, verbose_name="Выполнен ли пункт")
    is_delete = BooleanField(default=False, verbose_name="Удалён ли пункт")

    class Meta:
        database = db
        # Нужно для успешного создания модели в нужно БД


# db.connect()
# db.create_tables([TodoItem])
# Эти команды нужно выполнить в консоли импортировав переменную db и класс TodoItem
