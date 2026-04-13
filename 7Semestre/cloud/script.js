const bands = [
    {
        name: "Queen",
        genre: "Rock / Opera Rock",
        description: "Uma das bandas mais icônicas de todos os tempos, liderada por Freddie Mercury.",
        image: "https://images.unsplash.com/photo-1526218626217-dc65a29bb444?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
    },
    {
        name: "Pink Floyd",
        genre: "Rock Progressivo",
        description: "Conhecidos por suas composições filosóficas e shows elaborados.",
        image: "https://images.unsplash.com/photo-1459749411177-042180ce673c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
    },
    {
        name: "Led Zeppelin",
        genre: "Hard Rock",
        description: "Pioneiros do hard rock e heavy metal com solos memoráveis.",
        image: "https://images.unsplash.com/photo-1511735111819-9a3f7709049c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
    },
    {
        name: "Nirvana",
        genre: "Grunge",
        description: "A banda que definiu a geração dos anos 90 com Kurt Cobain.",
        image: "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
    },
    {
        name: "The Beatles",
        genre: "Pop / Rock",
        description: "A maior banda de todos os tempos, revolucionando a música moderna.",
        image: "https://images.unsplash.com/photo-1493225255756-d9584f8606e9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
    },
    {
        name: "Iron Maiden",
        genre: "Heavy Metal",
        description: "Lendas do heavy metal britânico com seu mascote Eddie.",
        image: "https://images.unsplash.com/photo-1466096115632-4499298a2419?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"
    }
];

const bandGrid = document.getElementById('bandGrid');
const bandSearch = document.getElementById('bandSearch');

function displayBands(filteredBands) {
    bandGrid.innerHTML = '';
    
    filteredBands.forEach(band => {
        const card = document.createElement('div');
        card.className = 'band-card';
        
        card.innerHTML = `
            <div class="band-img" style="background-image: url('${band.image}')"></div>
            <div class="band-info">
                <span class="genre">${band.genre}</span>
                <h2>${band.name}</h2>
                <p>${band.description}</p>
            </div>
        `;
        
        bandGrid.appendChild(card);
    });
}

bandSearch.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const filteredBands = bands.filter(band => 
        band.name.toLowerCase().includes(searchTerm) || 
        band.genre.toLowerCase().includes(searchTerm)
    );
    displayBands(filteredBands);
});

// Inicializar a grade
displayBands(bands);
