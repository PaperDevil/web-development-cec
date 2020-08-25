package todoModel

type Todo struct {
	Title string `json:"title"`
	Description string `json:"description"`
}

func New(title, desc string) *Todo {
	return &Todo{
		Title: title,
		Description: desc,
	}
}