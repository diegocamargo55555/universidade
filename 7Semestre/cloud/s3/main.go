package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	// 1. Inicializar Banco de Dados
	InitDB()

	// 2. Configurar o Gin
	r := gin.Default()

	// 3. Carregar Templates HTML (estão na raiz)
	r.LoadHTMLGlob("*.html")

	// 4. Servir Arquivos Estáticos (diretamente da raiz)
	r.StaticFile("/style.css", "./style.css")
	r.StaticFile("/exorcist.jpg", "./exorcist.jpg")

	// 5. Tratamento de Erro 404 (Página Não Encontrada)
	r.NoRoute(func(c *gin.Context) {
		c.HTML(404, "404.html", nil)
	})

	// 6. Rotas
	r.GET("/", GetIndex)
	r.GET("/movie/:id", GetMovie)

	// 7. Iniciar Servidor
	r.Run(":8080")
}
