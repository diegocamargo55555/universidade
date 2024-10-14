import React, { Component } from "react";
import './assets/estilo.css';

import biscoito from './assets/biscoito.png';
import logo from './assets/logo.png';

import rust from './assets/rs.png';
import umbrella from './assets/umb.png';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      imagem: ''

    };
    this.quebrarBiscoito = this.quebrarBiscoito.bind(this);

    this.imagens = [
      rust,
      umbrella,
      biscoito,
      logo
    ];
  }

  quebrarBiscoito() {
    let state = this.state;
    let numeroAleatorio = Math.floor(Math.random() * this.imagens.length);
    state.imagens = this.imagens[numeroAleatorio];
    this.setState(state);

  }
  render() {
    return (
      <div className="container">
        <img src={biscoito} className="img"></img>
        <Botao acao={this.quebrarBiscoito} nome={'Abrir Biscoito'} />
        <h3 className="textoFrase">{this.state.textoFrase}
        
          <img src={this.state.imagens} className="img"></img>

        </h3>
      </div>
    );
  }
}

class Botao extends Component {
  render() {
    return (
      <div>
        <button onClick={this.props.acao}>{this.props.nome}</button>
      </div>

    )
  }
}



export default App;