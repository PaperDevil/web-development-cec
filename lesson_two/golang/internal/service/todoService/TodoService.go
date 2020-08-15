package Todo

type TodoService interface {
	AddTodo(todo Todo) Todo
	ShowTodo() []Todo
}


