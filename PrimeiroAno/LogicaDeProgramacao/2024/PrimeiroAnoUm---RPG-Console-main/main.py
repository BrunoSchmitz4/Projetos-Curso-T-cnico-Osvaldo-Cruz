# Imports
import os
import time

# Funções
def getClassePersonagem(opcoesClasse: list):
    x = 1
    for opcao in opcoesClasse:
        print(f"[{x}] - ", opcao)
        x += 1
        
def getInfoPersonagem():
    print("Infos de ", nome_p, f"\nVida: {hp_p} | Atk: {atk_p} | Mana: {mana}\nClasse: {opcao_classe}")
    
def getFuncPrincipais():
    print("[1] - Iniciar/Continuar Jogo\n[2] - Configurações\n[0] - Sair")

def getFuncConfiguracoes():
    print("[1] - Ver infos do personagem\n[2] - Guia\n[0] - <- Voltar")

def getFuncGuia():
    print("[1] - Atributos\n[2] - Nível e XP\n[3] - Batalhando\n[0] - <- Voltar")

# Características do personagem
poder = ""
cabelo_cor = ""
roupa_p = ""
nome_p  = ""
hp_p = 0
atk_p = 0
mana = 0
opcao_classe = ""
xp = 0
nivel = 1

# Características dos inimigos
nome_orc = "Orc Abissal"
hp_orc = 20
atk_orc = 5
xp_derrotar_orc = 10

nome_sli = "Slime"
hp_sli = 5
atk_sli = 10
xp_derrotar_slime = 20

# Funcionalidades e dados do jogo:
opcoesClasse = ['Guerreiro(a)', 'Mago(a)', 'Arqueiro(a)']
classe_escolhida = 0
opcao_func = 100 # Opção Funcionalidade

# Tela de Login
while(opcao_func != 0):
    while(nome_p == ""):
        print("|====================================|")
        print("|  Bem vindo(a) à Reino de Etéria!   |")
        print("|____________________________________|")
        nome_p = str(input("Nome do usuário: "))

        print("Personalize seu personagem: ")
        print("Qual será a cor do seu cabelo: ")
        cabelo_cor = str(input("Cor: "))
        roupa_p = str(input("Descreva a roupa do personagem: "))
    os.system("cls")
    getFuncPrincipais()
    opcao_func = int(input("Opção: "))
    
    if(opcao_func == 1):
        os.system("cls")
        print("Começar história") # Fazer introdução da 
        print("Muito bem! Vamos agora começar a sua história, ", nome_p, "!")
        print("O que você é?")
        getClassePersonagem(opcoesClasse)
        while (classe_escolhida < 1) or (classe_escolhida > 3):
            classe_escolhida = int(input("Eu sou um(a): "))
            if classe_escolhida == 1:
                opcao_classe = opcoesClasse[0]
                hp_p += 50
                atk_p += 30
                mana += 10
            elif classe_escolhida == 2:
                opcao_classe = opcoesClasse[1]
                hp_p += 20
                atk_p += 30
                mana += 40
            elif classe_escolhida == 3:
                opcao_classe = opcoesClasse[2]
                hp_p += 30
                atk_p += 50
                mana += 10
        getInfoPersonagem()
        print("Iniciando batalha: ")
        primeiro_hp_sli = hp_sli
        primeiro_atk_sli = atk_sli
        primeiro_xp_sli = xp_derrotar_slime
        while primeiro_hp_sli > 0:
            opcao_acao = 0
            print("Primeira batalha | Dica: Escolha uma ação!")
            while opcao_acao != 1:
                print("Ações: \n[1] - Atacar ")
                opcao_acao = int(input("Ação: "))
                if opcao_acao == 1:
                    primeiro_hp_sli -= atk_p
                    print("Muito bem! Atacando seus inimigos, você causará dano.\nMas cuidado! Eles também podem te atacar!")
                    print("Vida do inimigo:", primeiro_hp_sli)
                    print("O inimigo atacou você! Ele causou ", primeiro_atk_sli, " de dano!")
                    print("Sua vida: ", hp_p)
                    print("Cuidado em sua jornada! Quando sua vida chegar à zero é fim de jogo!")
        print("Muito bem! Você derrotou o seu primeiro inimigo!\n")
    elif(opcao_func == 2):
        opcao = 100
        while opcao != 0:
            getFuncConfiguracoes()
            opcao = int(input("Opção: "))
            if opcao == 1:
                getInfoPersonagem()
            elif opcao == 2:
                opcao_guia = 100
                while opcao_guia != 0:
                    getFuncGuia()
                    opcao_guia = int(input("Opção: "))
                    if opcao_guia == 1:
                        print("À fazer")
                    elif opcao_guia == 2:
                        print("Ao derrotar inimigos, você ganha XP. Ao subir de nível, seus atributos melhoram e você desbloqueia novas habilidades!")
                    elif opcao_guia == 3:
                        print("À fazer")
    elif(opcao_func == 100):
        os.system("cls")
        print("Fechando jogo") # Manter assim