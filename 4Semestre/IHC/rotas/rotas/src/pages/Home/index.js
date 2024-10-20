import { Link } from "react-router-dom";

import './Home.css'
import { Title } from "./styles";
import { Div } from "./styles";

function home() {
    return (

        <div>
            <Title> Bem vindo à página HOME</Title>

            <Div>


                <p>dadwadawd </p>

                <br />
                <Link to='/sobre'>Sobre</Link>
                <br />
                <Link to='/contato'>Contato</Link>

            </Div>






        </div>

    )
}

export default home;
