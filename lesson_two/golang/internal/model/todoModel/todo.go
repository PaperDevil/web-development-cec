package Todo

type Todo struct {
	Title string
	Description string
}

func New(title, desc string) *Todo  {
	return &Todo{
		Title: title,
		Description: desc,
	}
}