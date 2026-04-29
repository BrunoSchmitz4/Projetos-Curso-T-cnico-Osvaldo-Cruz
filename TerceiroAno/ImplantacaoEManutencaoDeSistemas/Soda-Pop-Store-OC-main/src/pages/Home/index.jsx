import Card from "../../components/Card";
import Header from "../../components/Header";
import Titulo from "../../components/Titulo";
import BotaoNavegacao from "../../components/BotaoNavegacao";

function Home() {
    return (
        <>
            <Header />
            <Titulo /> 
            <Card></Card>
            <BotaoNavegacao route={"/carrinho"} nome={"Carrinho"}/>
        </>
    )
}

export default Home;