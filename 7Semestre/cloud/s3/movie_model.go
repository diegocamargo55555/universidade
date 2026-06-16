package main

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type Movie struct {
	ID          uint   `gorm:"primaryKey" json:"id"`
	Title       string `json:"title"`
	Year        int    `json:"year"`
	Director    string `json:"director"`
	Description string `json:"description"`
	PosterURL   string `json:"poster_url"`
}

var DB *gorm.DB

func InitDB() {
	var err error
	DB, err = gorm.Open(sqlite.Open("horror.db"), &gorm.Config{})
	if err != nil {
		panic("falha ao conectar no banco de dados")
	}

	DB.AutoMigrate(&Movie{})
	SeedDB()
}

func SeedDB() {
	var count int64
	DB.Model(&Movie{}).Count(&count)
	if count > 0 {
		return
	}

	movies := []Movie{
		{
			Title:       "The Shining",
			Year:        1980,
			Director:    "Stanley Kubrick",
			Description: "Jack Torrance aceita um emprego como zelador de inverno em um hotel isolado, onde uma presença sinistra influencia Jack à violência.",
			PosterURL:   "https://image.tmdb.org/t/p/w500/x9Qv3S4S6M38Y5u7Xf5M2YmF1x6.jpg",
		},
		{
			Title:       "O Exorcista",
			Year:        1973,
			Director:    "William Friedkin",
			Description: "Quando uma adolescente é possuída por uma entidade misteriosa, sua mãe busca a ajuda de dois padres para salvá-la.",
			PosterURL:   "/exorcist.jpg",
		},
		{
			Title:       "Halloween",
			Year:        1978,
			Director:    "John Carpenter",
			Description: "Quinze anos após assassinar sua irmã, Michael Myers foge de um hospital psiquiátrico e retorna para matar novamente.",
			PosterURL:   "https://image.tmdb.org/t/p/w500/96fF6v8U7f5v7v7v7v7v7v7v7v7.jpg",
		},
		{
			Title:       "A Hora do Pesadelo",
			Year:        1984,
			Director:    "Wes Craven",
			Description: "Um assassino cruel persegue suas vítimas em seus sonhos. Se ele te matar no sonho, você morre na vida real.",
			PosterURL:   "https://image.tmdb.org/t/p/w500/6fF6v8U7f5v7v7v7v7v7v7v7v7v.jpg",
		},
		{
			Title:       "Psicose",
			Year:        1960,
			Director:    "Alfred Hitchcock",
			Description: "Uma secretária foge com dinheiro e se hospeda em um motel remoto administrado por um jovem sob o domínio de sua mãe.",
			PosterURL:   "https://image.tmdb.org/t/p/w500/8fF6v8U7f5v7v7v7v7v7v7v7v7v.jpg",
		},
	}

	DB.Create(&movies)
}
