

function Card({CardTitulo = "", CardDescricao = "", CardImagem = ""}) {
    return (
        <div>
            <h2>{CardTitulo}</h2>
            <img src={CardImagem} alt={CardTitulo} />
            <p>{CardDescricao}</p>
            <button>Saiba Mais</button>
        </div>
    )
}

export default Card;