import { Link } from "react-router-dom";
function erro() {
    return(
        <div>
            <h1>Bem vindo à página de erro tente acessar esses links: </h1>
            
            <br/>
            <Link to='/sobre'>Sobre</Link>
            <br/>
            <Link to='/contato'>Contato</Link>
        </div>
        
    )
}

export default erro;
