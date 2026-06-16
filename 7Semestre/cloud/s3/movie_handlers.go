package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func GetIndex(c *gin.Context) {
	var movies []Movie
	DB.Find(&movies)
	c.HTML(http.StatusOK, "index.html", gin.H{
		"movies": movies,
	})
}

func GetMovie(c *gin.Context) {
	id := c.Param("id")
	var movie Movie
	if err := DB.First(&movie, id).Error; err != nil {
		c.HTML(http.StatusNotFound, "404.html", nil)
		return
	}
	c.HTML(http.StatusOK, "movie.html", gin.H{
		"movie": movie,
	})
}
