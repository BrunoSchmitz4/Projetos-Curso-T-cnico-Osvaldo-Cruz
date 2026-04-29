import { Link } from "react-router-dom";

function BotaoNavegacao({route, nome}) {
    return (
        <Link to={route}>{nome}</Link>
    )
}

export default BotaoNavegacao