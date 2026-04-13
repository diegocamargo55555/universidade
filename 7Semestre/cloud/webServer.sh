#!/bin/bash

# Atualiza os pacotes e instala o Apache
yum update -y
yum install -y httpd

# Inicia e habilita o serviço do Apache
systemctl start httpd
systemctl enable httpd

# Cria o arquivo index.html
cat > /var/www/html/index.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arquivo do Rock | Bandas Clássicas</title>
    <style>
        /* Estilos Gerais */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }

        /* Cabeçalho */
        header {
            background-color: #1a1a1a;
            color: #fff;
            padding: 2rem 0;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        header h1 {
            margin: 0;
            font-size: 2.5rem;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        header p {
            margin-top: 10px;
            font-size: 1.1rem;
            color: #bbb;
        }

        /* Contêiner Principal */
        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }

        /* Grid de Bandas */
        .bands-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        /* Card da Banda */
        .band-card {
            background-color: #fff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .band-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        /* Imagem da Banda (Placeholder) */
        .band-image {
            width: 100%;
            height: 200px;
            background-color: #ddd;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #888;
            font-style: italic;
            font-size: 0.9rem;
        }

        /* Degradê para os placeholders simulando imagens */
        .img-beatles { background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); }
        .img-queen { background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%); }
        .img-nirvana { background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%); }
        .img-floyd { background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); }

        /* Informações da Banda */
        .band-info {
            padding: 20px;
        }

        .band-info h2 {
            margin: 0 0 10px 0;
            font-size: 1.5rem;
            color: #222;
        }

        .genre {
            display: inline-block;
            background-color: #e53935;
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .band-info p {
            line-height: 1.6;
            color: #666;
            margin: 0 0 20px 0;
            font-size: 0.95rem;
        }

        /* Botão */
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #1a1a1a;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        .btn:hover {
            background-color: #e53935;
        }

        /* Rodapé */
        footer {
            text-align: center;
            padding: 20px;
            background-color: #1a1a1a;
            color: #777;
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <header>
        <h1>Arquivo do Rock</h1>
        <p>Descubra os gigantes que moldaram a história da música</p>
    </header>

    <div class="container">
        <div class="bands-grid">
            
            <div class="band-card">
                <div class="band-image img-beatles">[Imagem: The Beatles]</div>
                <div class="band-info">
                    <h2>The Beatles</h2>
                    <span class="genre">Rock Clássico</span>
                    <p>Banda britânica formada em Liverpool em 1960. Reconhecida como a banda mais influente de todos os tempos, revolucionou a música e a cultura pop na década de 1960.</p>
                    <a href="#" class="btn">Ouvir Agora</a>
                </div>
            </div>

            <div class="band-card">
                <div class="band-image img-queen">[Imagem: Queen]</div>
                <div class="band-info">
                    <h2>Queen</h2>
                    <span class="genre">Hard Rock</span>
                    <p>Liderada pelo icônico Freddie Mercury, a banda britânica inovou ao misturar rock com ópera e elementos teatrais, criando hinos eternos como "Bohemian Rhapsody".</p>
                    <a href="#" class="btn">Ouvir Agora</a>
                </div>
            </div>

            <div class="band-card">
                <div class="band-image img-nirvana">[Imagem: Nirvana]</div>
                <div class="band-info">
                    <h2>Nirvana</h2>
                    <span class="genre">Grunge</span>
                    <p>Símbolo da geração X e pioneiros do movimento grunge de Seattle nos anos 90. Seu álbum "Nevermind" mudou drasticamente o cenário musical da época.</p>
                    <a href="#" class="btn">Ouvir Agora</a>
                </div>
            </div>

            <div class="band-card">
                <div class="band-image img-floyd">[Imagem: Pink Floyd]</div>
                <div class="band-info">
                    <h2>Pink Floyd</h2>
                    <span class="genre">Rock Progressivo</span>
                    <p>Famosos por suas composições complexas, letras filosóficas e shows visuais grandiosos. Álbuns como "The Dark Side of the Moon" são marcos na história da música.</p>
                    <a href="#" class="btn">Ouvir Agora</a>
                </div>
            </div>

        </div>
    </div>

    <footer>
        <p>&copy; 2026 Arquivo do Rock. Desenvolvido para amantes da música.</p>
    </footer>

</body>
</html>
EOF