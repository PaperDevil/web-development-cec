# Создание
1) Проверяем версию Python \
```$ python -V``` \
2) Создаём виртуальное окружение для хранения зависимостей \
```$ python -m venv venv``` \
3) Дальше нужно активировать окружение \
Windows: ```$ .\venv\Scripts\activate``` \
Linux: ```$ source ./venv/Scripts/activate``` \
4) Устанавливаем пакет Flask и проверяем его наличие \
```$ python -m pip install flask``` \
```$ python -m pip freeze``` \
5) Создаём первый Python модуль для запуска приложения\
```$ echo >> main.py```