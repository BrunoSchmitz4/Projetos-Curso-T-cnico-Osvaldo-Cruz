import os

# Código do Protagonista

# Atributos Base do Protagonista
# nome_p = "" # nome
# nivel_p = 1
# xp_p = 0.0 # pontos de experiência
# hp_p = 0.0 # pontos de vida
# atk_p = 0.0 # pontos de atk
# mana_p = 0.0 # pontos de magia
# opcao_classe = 0 # Classe do personagem

# Atributos do Protagonista Atual
nome_p = "" # nome
nivel_p = 1
xp_p = 0.0 # pontos de experiência
hp_p = 0.0 # pontos de vida
atk_p = 0.0 # pontos de atk
mana_p = 0.0 # pontos de magia
opcao_classe = 0 # Classe do personagem

def getNomeP():
    return nome_p

def getNivelP():
    return nivel_p

def getXpP():
    return xp_p

def getHpP():
    return hp_p

def getAtkP():
    return atk_p

def getManaP():
    return mana_p

def getOpcaoClasse():
    return opcao_classe

def setPersonagem():
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

    print("Personagem: ", nome_p, "\nStatus:\nNível XP: ", xp_p, "HP: ", hp_p, "\nATK: ", atk_p,"Mana: ", mana_p)
        
    # Arma personagem
    # Guerreiro: Espadão, Martelo e Katana
    # Arqueiro: Lança, Arco e Besta
    # Mago: Cajado, Varinha, Talismã (Livro da academia de magia)