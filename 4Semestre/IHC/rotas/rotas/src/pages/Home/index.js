import { Link } from "react-router-dom";
function home() {
    return(
        <div>
            <h1>Bem vindo à página HOME</h1>
            
            <br/>
            <Link to='/sobre'>Sobre</Link>
            <br/>
            <Link to='/contato'>Contato</Link>
        </div>
        
    )
}

export default home;
