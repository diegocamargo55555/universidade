import matplotlib.pyplot as plt
import geopandas as gpd


# Dados das cidades brasileiras


cities = [
    ((-49.27, -25.43), "Python", "Curitiba"),
    ((-46.63, -23.55), "Java", "São Paulo"),
    ((-43.20, -22.90), "R", "Rio de Janeiro"),
    ((-38.50, -12.97), "Python", "Salvador"),
    ((-34.88, -8.05), "Java", "Recife"),
    ((-60.02, -3.10), "R", "Manaus"),
]


# Estruturas do gráfico


plots = {
    "Java": ([], []),
    "Python": ([], []),
    "R": ([], [])
}

markers = {
    "Java": "o",
    "Python": "s",
    "R": "^"
}

colors = {
    "Java": "red",
    "Python": "blue",
    "R": "green"
}


# Organiza os pontos


for (longitude, latitude), language, city in cities:
    plots[language][0].append(longitude)
    plots[language][1].append(latitude)


# Carrega mapa do Brasil


url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/brazil-states.geojson"

brazil = gpd.read_file(url)


# Cria figura

fig, ax = plt.subplots(figsize=(12, 12))

# Desenha mapa
brazil.plot(
    ax=ax,
    color="white",
    edgecolor="black"
)


# Desenha os pontos


for language, (x, y) in plots.items():

    ax.scatter(
        x,
        y,
        color=colors[language],
        marker=markers[language],
        label=language,
        s=120,
        zorder=5
    )


# Escreve nomes das cidades


for (longitude, latitude), language, city in cities:

    ax.text(
        longitude + 0.5,
        latitude + 0.5,
        city,
        fontsize=10
    )


# Destaque especial para Guarapuava


guarapuava_lon = -51.46
guarapuava_lat = -25.39

ax.scatter(
    guarapuava_lon,
    guarapuava_lat,
    color="black",
    s=200,
    marker="*",
    zorder=10
)

ax.text(
    guarapuava_lon - 10.5,
    guarapuava_lat,
    "Guarapuava",
    fontsize=12,
    fontweight="bold",
    color="black"
)


# Configurações


plt.title("Linguagens de Programação Favoritas no Brasil")

plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.legend()

plt.grid(True)


# Exibe


plt.show()