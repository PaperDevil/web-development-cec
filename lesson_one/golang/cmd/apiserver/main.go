package main

import "github.com/go-martini/martini"


func main() {
  m := martini.Classic()

  // Стартовая страница приложения
  m.Get("/", func() string {
    return "Привер Мир!"
  })

  // Страница приветствия Юзера
  m.Get("/user/:username", func (params martini.Params) string {
	  return "Привет, " + params["username"] + "!"
  })
  m.Run()
}