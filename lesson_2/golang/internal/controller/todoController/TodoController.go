package todoController

import (
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/model/todoModel"
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/service/todoService"
	"github.com/gin-gonic/gin"
	"log"
)

type TodoController interface {
	AddTodo(context *gin.Context) todoModel.Todo
	ShowTodo() []todoModel.Todo
	Routes(ctx *gin.Engine)
}

type todoController struct {
	service todoService.TodoService
}

func New(service todoService.TodoService) TodoController {
	return &todoController{
		service: service,
	}
}

func (controller *todoController) AddTodo(context *gin.Context) todoModel.Todo {
	var todo todoModel.Todo
	if err := context.BindJSON(&todo); err != nil {
		log.Fatal(err)
	}
	return controller.service.AddTodo(todo)
}

func (controller *todoController) ShowTodo() []todoModel.Todo {
	return controller.service.ShowTodo()
}

func (controller *todoController) Routes(server *gin.Engine) {
	server.POST("/todo/add", func(context *gin.Context) {
		context.JSON(200, controller.AddTodo(context))
	})
	server.GET("/todo", func(context *gin.Context) {
		context.JSON(200, controller.ShowTodo())
	})
}
