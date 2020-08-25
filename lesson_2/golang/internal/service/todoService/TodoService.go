package todoService

import (
	"github.com/PaperDevil/web-development-cec/tree/master/lesson_two/golang/internal/model/todoModel"
)

type TodoService interface {
	AddTodo(todo todoModel.Todo) todoModel.Todo
	ShowTodo() []todoModel.Todo
}

type todoService struct {
	todos []todoModel.Todo
}

func New() TodoService {
	return &todoService{}
}

func (service *todoService) AddTodo(todo todoModel.Todo) todoModel.Todo {
	service.todos = append(service.todos, todo)
	return todo
}

func (service *todoService) ShowTodo() []todoModel.Todo {
	return service.todos
}