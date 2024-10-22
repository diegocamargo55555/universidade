import React, { useEffect, useState } from 'react';

function App() {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    // Função para buscar o arquivo JSON
    const fetchData = async () => {
      try {
        const response = await fetch('./paises-array.json'); // Caminho relativo ao public
        const data = await response.json(); // Converte a resposta para JSON
        setDados(data); // Armazena os dados no estado
      } catch (error) {
        console.error('Erro ao buscar os dados:', error);
      }
    };

    fetchData(); // Chama a função para buscar os dados
  }, []); // O array vazio garante que a função seja chamada apenas uma vez

  return (
        
    <div>
      <h1>Dados do JSON</h1>
      <h2>Nome dos paises</h2>

      <div>

        {dados.map((item, index) => (
          <strong className="titulo">{item.nome}<br /></strong>

        ))}

      </div>
      <br />
      <ul>
        {dados.map((item, index) => (
          <li key={index}>{JSON.stringify(item)}</li> // Exibe os dados
        ))}
      </ul>
    </div>
  );
}
export default App;


