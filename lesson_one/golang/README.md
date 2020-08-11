# Создание
1) Создадим минимальную разметку \
```$ mkdir cmd\apiserver``` \
```$ echo >> cmd\apiserver\main.go``` \
2) Проверим наличие в системе Go \
```$ go version``` \
3) Проверим наличие компилятора gcc (нужен для пакетов Go) \
```$ gcc --version``` \
4) Создаём отдельное окружение для модулей Go \
```$ go mod init github.com/PaperDevil/web-development-cec/lesson_one/golang``` \
5) Устанавливаем пакет go-martini/martini \
```$ go get github.com/go-martini/martin``` \