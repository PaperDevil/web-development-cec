from models import *


def base_fill():
    w1 = Worker(first_name="Алексей", last_name="Митюшин", age=48, post="Начальник цеха").save()
    w2 = Worker(first_name="Сергей", last_name="Ищенко", age=34, post="Инженер запчастей").save()
    w3 = Worker(first_name="Михаил", last_name="Ридванов", age=41, post="Инженер запчастей").save()

    wing = Device(name="Крыло", price=42000, worker=w1).save()
    tail = Device(name="Хвост", price=56000, worker=w2).save()
    chassis = Device(name="Шасси", price=21000, worker=w3).save()

    Operation(worker=w1, device=wing).save()
    Operation(worker=w2, device=tail).save()
    Operation(worker=w3, device=chassis).save()