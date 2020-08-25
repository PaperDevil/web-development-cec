package main

import "github.com/gin-gonic/gin"

func main() {
	app := gin.Default()  // Экземпляр приложения

	// Стартовая страница приложения
	app.GET("/", func(context *gin.Context) {
		context.String(200, "Привет Мир!")
	})

	// Страница приветствия Юзера
	app.GET("/user/:name", func(context *gin.Context) {
		context.String(200, "Привет, " + context.Param("name") + "!")
	})

	// Получение JSON с именем юзера
	app.GET("/user/:name/get", func(context *gin.Context) {
		context.JSON(200, gin.H{
			"username": context.Param("name"),
		})
	})

	// Метод, к которому мы не получим доступ
	app.POST("/user/:name/update", func(context *gin.Context) {
		context.String(200, "Какое-то действие с юзером")
	})

	app.Run(":8080")
}