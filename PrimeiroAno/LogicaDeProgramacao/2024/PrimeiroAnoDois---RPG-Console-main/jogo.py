# Imports
import os
import random
import time

# Funções
def showInitOption(): # Mostra opções iniciais
    x = 1
    for opcaoInit in opcoes_init:
        print(f"[{x}] - {opcaoInit}\n")
        x +=1
        
def showClassesOption():
    x = 1
    for optClasse in opcoes_classe:
        print(f"[{x}] - {optClasse}")
        x += 1

def showGuerreiroArmasOptions():
    x = 1
    for arma in opcoes_armas_guerreiro:
        print(f"[{x}] - {arma}\n")
        x += 1
        
def showArqueiroArmasOptions():
    x = 1
    for arma in opcoes_armas_arqueiro:
        print(f"[{x}] - {arma}\n")
        x += 1
        
def showMagoArmasOptions():
    x = 1
    for arma in opcoes_armas_mago:
        print(f"[{x}] - {arma}\n")
        x += 1
        
def showConfigOptions():
    x = 1
    for opcao in opcoes_config:
        print(f"[{x}] - {opcao}\n")
        x += 1
        
def showInfoJogador():
    print(f"{nome_p} | Level: {nivel_p} | Xp: {xp_p}")
    print(f"Atributos:\nHP: {hp_p} | ATK: {atk_p} | Mana: {mana_p}")
    print(f"Infos adicionais:\nClasse: {nome_classe} | Arma: {nome_arma}")

def iniciaHistoria():
    os.system("cls")
    print("_________________________________________\n\nBem vindo ao Reino Eirantel! Um reino já visto como a nação perfeita, onde a pobreza não existia e a segurança do povo era prioridade. Hoje em dia, infelizmente, esse título não condiz mais com a realidade, pois criaturas do abismo assolaram essas terras com triteza.")
    print("Sua missão, é derrotar todas as criaturas invassoras e seu lider, conhecido e venerado como 'A Tormenta'.")

def opcoesBatalha():
    print()
# Atributos do jogador
nome_p = "" # nome
nivel_p = 1
xp_p = 0.0 # pontos de experiência
hp_p = 0.0 # pontos de vida
atk_p = 0.0 # pontos de atk
mana_p = 0.0 # pontos de magia
opcao_classe = 0 # Classe do personagem
nome_classe = ""
opcao_arma = 0
nome_arma = ""
# Atributos dos inimigos
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

# Variáveis de controle do jogo
opcao_init = 100
opcoes_init = ['Continuar Jogo', 'Novo jogo', 'Configurações']
opcoes_classe = ['Guerreiro', 'Arqueiro', 'Mago']
opcoes_armas_guerreiro = ['Espadão', 'Martelo', 'Katana']
opcoes_armas_arqueiro = ['Lança', 'Arco', 'Besta']
opcoes_armas_mago = ['Cajado', 'Varinha', 'Talismã']
opcoes_config = ['Info Jogador', 'Guia de Jogo']
opcoes_batalha = ['Atacar', 'Habilidades', 'Mochila', 'Fugir']
while opcao_init != 0:
    showInitOption()
    print('[0] - Sair')
    opcao_init = int(input("Opção: "))
    if opcao_init == 1:
        if nome_p == "":
            print("Não existe jogo salvo")
        else:
            print("À fazer")
    # Iniciar jogo e história
    elif opcao_init == 2:
        print("|====================================|")
        print("|Bem vindo(a) à Dungeons and Dragons!|")
        print("|____________________________________|")
        nome_p = str(input("Nome do usuário: "))
        print("Selecione seu personagem: ")
        showClassesOption()
        while opcao_classe == 0 or opcao_classe > len(opcoes_classe):
            opcao_classe = int(input("Opção:"))
        if opcao_classe == 1:
            nome_classe = opcoes_classe[0]
            hp_p = 250
            atk_p = 55
            mana_p = 75
            showGuerreiroArmasOptions
            print("Selecione sua arma inicial: ")
            while opcao_arma == 0 or opcao_arma > len(opcoes_armas_guerreiro):
                opcao_arma = int(input("Opção de arma: "))
            if(opcao_arma == 1):
                nome_arma = opcoes_armas_guerreiro[0]
                atk_p = atk_p + 40
                hp_p = hp_p + 50
            elif(opcao_arma == 2):
                nome_arma = opcoes_armas_guerreiro[1]
                atk_p = atk_p + 20
                hp_p = hp_p + 75
            else:
                nome_arma = opcoes_armas_guerreiro[2]
                atk_p = atk_p + 25
                hp_p = hp_p + 25
        elif opcao_classe == 2:
            nome_classe = opcoes_classe[1]
            hp_p = 120
            atk_p = 100
            mana_p = 80
            showArqueiroArmasOptions
            print("Selecione sua arma inicial: ")
            while opcao_arma == 0 or opcao_arma > len(opcoes_armas_arqueiro):
                opcao_arma = int(input("Opção de arma: "))
            if(opcao_arma == 1):
                nome_arma = opcoes_armas_arqueiro[0]
                atk_p = atk_p + 40
                hp_p = hp_p + 50
            elif(opcao_arma == 2):
                nome_arma = opcoes_armas_arqueiro[1]
                atk_p = atk_p + 20
                hp_p = hp_p + 75
            else:
                nome_arma = opcoes_armas_arqueiro[2]
                atk_p = atk_p + 25
                hp_p = hp_p + 25
        elif opcao_classe == 3:
            nome_classe = opcoes_classe[2]
            hp_p = 110
            atk_p = 75
            mana_p = 250
            showMagoArmasOptions()
            print("Selecione sua arma inicial: ")
            while opcao_arma == 0 or opcao_arma > len(opcoes_armas_mago):
                opcao_arma = int(input("Opção de arma: "))
            if(opcao_arma == 1):
                nome_arma = opcoes_armas_mago[0]
                atk_p = atk_p + 40
                hp_p = hp_p + 50
            elif(opcao_arma == 2):
                nome_arma = opcoes_armas_mago[1]
                atk_p = atk_p + 20
                hp_p = hp_p + 75
            else:
                nome_arma = opcoes_armas_mago[2]
                atk_p = atk_p + 25
                hp_p = hp_p + 25
        else:
            print(f"Essa opção de classe ({opcao_classe}) não existe")
        iniciaHistoria()
        print("Parece que um inimigo apareceu! A batalha se inicia!")
        print(nome_esqArc, "Vida: ", hp_esqArc, "Atk: ", atk_esqArc)
        hp_inimigo_atual = hp_esqArc
        while hp_inimigo_atual > 0 and hp_p > 0:
            option_batalha = 0
            print("Deseja atacar? [1] - Sim")
            opcao_atk = int(input("Opção: "))
            if(opcao_atk == 1):
                hp_esqArc -= atk_p
            if(hp_esqArc > 0):
                print("O inimigo te atacou! Ele causou: ", atk_esqArc, " de dano!")
                hp_p -= atk_esqArc
                print("Vida atual: ", hp_p)
    elif opcao_init == 3:
        opcao_config = 100
        while opcao_config != 0:
            print("Escolha uma opção: ")
            showConfigOptions()
            print('[0] - Voltar')
            opcao_config = int(input("Opção: "))
            if opcao_config == 1:
                if nome_p == "":
                    print("É preciso iniciar o jogo antes!")
                else:
                    showInfoJogador()
            elif opcao_config == 2:
                print('À fazer')
    elif opcao_init == 0:
        print("Fechando jogo...")
    else:
        print("Opção inexistente!")