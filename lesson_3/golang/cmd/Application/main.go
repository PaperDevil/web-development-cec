package main

import (
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/Server"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

func main() {
	// Создание сервера
	server := Server.New(":8080")

	// Настройки сервера
	server.Gin.LoadHTMLGlob("templates/*")

	// Роутинг
	server.Gin.GET("/", func (c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", gin.H{
			"title": "Hello, my Lord!",
		})
	})

	server.Gin.GET("/:name", func(c *gin.Context) {
		name := c.Param("name")
		c.HTML(http.StatusOK, "index.html", gin.H{
			"title": "Hello, " + name,
		})
	})

	// Запуск сервера
	if err := server.Gin.Run(":8081"); err != nil {
		log.Fatal(err)
	}
}
