package Server

import "github.com/gin-gonic/gin"

type Server struct {
	Port string
	Gin *gin.Engine
}

func New(port string) *Server  {
	return &Server{
		Port: port,
		Gin: gin.Default(),
	}
}

func ServerTest() Server {
	return *New(":8000")
}