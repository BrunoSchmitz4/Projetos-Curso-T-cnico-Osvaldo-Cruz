# Importações de pacotes
import os # Biblioteca System
import random # Biblioteca Aleatoriedade
import Entidades.protagonista
import Entidades.Inimigos

def iniciaHistoria():
    os.system("cls")
    print("_________________________________________\n\nBem vindo ao Reino Eirantel! Um reino já visto como a nação perfeita, onde a pobreza não existia e a segurança do povo era prioridade. Hoje em dia, infelizmente, esse título não condiz mais com a realidade, pois criaturas do abismo assolaram essas terras com triteza.")
    print("Sua missão, é derrotar todas as criaturas invassoras e seu lider, conhecido e venerado como 'A Tormenta'.")

# Personagem em jogo
protagonista = Entidades.protagonista

# Atributos do Protagonista
nome_p = "" # nome
nivel_p = 1
xp_p = 0 # pontos de experiência
hp_p = 0 # pontos de vida
atk_p = 0 # pontos de atk
mana_p = 0 # pontos de magia
opcao_classe = 0 # Classe do personagem

# Atributos dos Inimigos
nome_orc = "Orc Abissal"
hp_orc = 30
atk_orc = 5
xp_orc = 20

nome_esqArc = "Esqueleto Arqueiro"
hp_esqArc = 15
atk_esqArc = 10
xp_esqArc = 15

nome_sli = "Slime de Fogo"
hp_sli = 10
atk_sli = 20
xp_sli = 10
############################

# Tela de Login
opcao_init = 100

while(opcao_init != 0):
    # Ao iniciar jogo
    while(nome_p == ""):
        print("|====================================|")
        print("|Bem vindo(a) à Dungeons and Dragons!|")
        print("|____________________________________|")
        nome_p = str(input("Nome do usuário: "))
    print("\n\nSelecione seu personagem, ", nome_p,": \n (1) Guerreiro\n (2) Arqueiro\n (3) Mago")
    opcao_classe = int(input("opção:"))
    opcao_arma = 0
    if (opcao_classe == 1):
        hp_p = 250
        atk_p = 55
        mana_p = 75
        print("Escolha sua arma:\n(1) Espadão | (2) Martelo | (3) Katana")
        opcao_arma = int(input("Opção de arma: "))
        if(opcao_arma == 1):
            atk_p = atk_p + 40
            hp_p = hp_p + 50
        elif(opcao_arma == 2):
            atk_p = atk_p + 20
            hp_p = hp_p + 75
        else:
            atk_p = atk_p + 25
            hp_p = hp_p + 25
    elif (opcao_classe == 2):
        hp_p = 120
        atk_p = 100
        mana_p = 80
        print("Escolha sua arma:\n(1) Lança | (2) Arco | (3) Besta")
        opcao_arma = int(input("Opção de arma: "))
        if(opcao_arma == 1):
            atk_p = atk_p + 40
            hp_p = hp_p + 50
        elif(opcao_arma == 2):
            atk_p = atk_p + 20
            hp_p = hp_p + 75
        else:
            atk_p = atk_p + 25
            hp_p = hp_p + 25
    else: 
        hp_p = 110
        atk_p = 75
        mana_p = 250
        print("Escolha sua arma:\n(1) Cajado | (2) Varinha | (3) Talismã")
        opcao_arma = int(input("Opção de arma: "))
        if(opcao_arma == 1):
            atk_p = atk_p + 40
            hp_p = hp_p + 50
        elif(opcao_arma == 2):
            atk_p = atk_p + 20
            hp_p = hp_p + 75
        else:
            atk_p = atk_p + 25
            hp_p = hp_p + 25
    os.system("cls")
    
    # Ao manter jogo ligado
    print("[1] - Começar História\n[2] - Configurações\n[0] - Encerrar Jogo")
    opcao_init = int(input("O que desejas fazer?")) # Primeira escolha
    if opcao_init == 1:
        iniciaHistoria()
        print("Iniciando batalha contra primeiro inimigo:")
        print(nome_esqArc, "Vida: ", hp_esqArc, "Atk: ", atk_esqArc)
        hp_inimigo_atual = hp_esqArc
        while(hp_inimigo_atual > 0):
            opcao_atk = 0
            print("Deseja atacar? [1] - Sim")
            opcao_atk = int(input("Opção: "))
            while opcao_atk != 1:
                print("Deseja atacar? [1] - Sim")
                opcao_atk = int(input("Opção: "))
                if(opcao_atk == 1):
                    hp_esqArc -= atk_p
            if(hp_esqArc > 0):
                print("O inimigo te atacou! Ele causou: ", atk_esqArc, " de dano!")
                hp_p -= atk_esqArc
                print("Vida atual: ", hp_p)
    elif opcao_init == 2:
        os.system("cls")

        print("Personagem: ", nome_p, "\nStatus:\nNível XP: ", xp_p, "HP: ", hp_p, "\nATK: ", atk_p,"Mana: ", mana_p)
    else:
        os.system("cls")
        print("_________________________________________\n\nEncerrando jogo...")
        break
        
        
        