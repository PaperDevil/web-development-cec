package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	server := gin.Default()

	// Генерация формы...

	// Нативная форма
	server.GET('/native-formm', func(c *gin.Context) {
		c.HTML(http.StatusOK, '', nil)
	})
	server.POST('/native-form', func(c *gin.Context) {
		//...
	})

	server.Run()
}