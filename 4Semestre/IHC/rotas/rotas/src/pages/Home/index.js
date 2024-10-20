import { Link } from "react-router-dom";

import './Home.css'
import { Title } from "./styles";
import { Div } from "./styles";

function home() {
    return (

        <Div>
            <Title> Bem vindo à página HOME</Title>

            <br />
            <Link to='/sobre'>Sobre</Link>
            <br />
            <Link to='/contato'>Contato</Link>

        
        </Div>
    )
}

export default home;
