## Установка окружениея
```>> python -m venv env
   >> env\Scripts\activate
   >> pip install -r requirements.txt
```
## Создания Базы Данных
```>> python
   $: from models import *
   $: db.connect()
   $: db.create_tables([Worker, Device, Operation])
```
## Заполнение данными
```>> python
   $: from fill import base_fill
   $: base_fill()
```
## Выполнение запросов
Напишите ваш запрос в функции main файла main.py
Запустите: ```>> python main.py```

https://miro.com/app/board/o9J_lXwFOJ0=/