import styles from './Header.module.css';

function Header() {
    return (
        <>
            <h1 className={styles.titulo}>Eu sou o header</h1>
            <h2>Bem vindo(a) à SodaPop-Store</h2>
        </>
    )
}

export default Header;