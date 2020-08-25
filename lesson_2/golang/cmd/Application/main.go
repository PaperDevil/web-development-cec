package main

import (
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/Server"
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/controller/todoController"
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/service/todoService"
)

var (
	todoS todoService.TodoService = todoService.New()
	todoC todoController.TodoController = todoController.New(todoS)
)


func main() {
	server := Server.New(":8080")
	todoC.Routes(server.Gin)
	server.Gin.Run()
}
