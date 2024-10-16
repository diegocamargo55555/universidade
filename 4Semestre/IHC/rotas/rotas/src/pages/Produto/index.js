import { Link } from "react-router-dom";
import imagem from "../../assets/umb.png"
function Produto() {
    return (
        <div>

            <h1> Veja sobre o nossos produto </h1>
            <br />
            <Link to='/sobre'>Sobre</Link>
            <br />

            <img src={imagem} />

        </div>

    )
}

export default Produto;
