import { Link } from "react-router-dom";

function Header() {
    return (
        <header>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"></link>
            <body>
                <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
                    <div class="container-fluid">
                        <Link class="navbar-brand" to='/'>Home</Link>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                                <li class="nav-item">
                                    <Link class="nav-link active" aria-current="page" to='/sobre'>Sobre</Link>
                                </li>
                                <li class="nav-item">
                                    <Link class="nav-link active" aria-current="page" to='/contato'>Contato</Link>
                                </li>
                                <li class="nav-item">
                                    <Link class="nav-link active" aria-current="page" to='/produto'>Produto</Link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </body>
        </header>

        
    )
}

export default Header;