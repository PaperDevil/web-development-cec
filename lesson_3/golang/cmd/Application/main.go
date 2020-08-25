package main

import (
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/Server"
)

func main() {
	server := Server.New(":8080")
	server.Gin.Run()
}
