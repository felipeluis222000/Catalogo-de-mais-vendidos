#################################
# Mini Projeto feito por        #
# Luis Felipe da Silva Santiago #
# Klara Rodrigues da Rocha      #
#################################

import time

'''NOME_PRODUTOS = []
UNIDADES_VENDIDAS = []
ANOTANDO = True

def Linhas():
    print("================================================")

def ShellSort(produtos, quantidade_vendida):
    marcador = 1
    tamanho_vendas = len(quantidade_vendida)

    while marcador > 0:

        for indice in range(marcador, tamanho_vendas):
            vendas = quantidade_vendida[indice]
            nome_produto = produtos[indice]
            marcador2 = indice

            while marcador2 >= marcador and vendas > quantidade_vendida[marcador2 - marcador]:
                quantidade_vendida[marcador2] = quantidade_vendida[marcador2-marcador]
                produtos[marcador2] = produtos[marcador2-marcador]
                marcador2 = marcador2 - marcador
                quantidade_vendida[marcador2] = vendas
                produtos[marcador2] = nome_produto
        marcador = 0

    return (produtos, quantidade_vendida)

def Ranking_Vendas():
    pass

while ANOTANDO:
    Linhas()
    nome_produto = input("Qual o nome do produto?\n")
    NOME_PRODUTOS.append(nome_produto)

    while True:

        try:
            Linhas()
            unidades_vendidas = int(input("Quantas unidades foram vendidas?\n"))
            break

        except:
            print("utilizar somente valores inteiros!!!")

    UNIDADES_VENDIDAS.append(unidades_vendidas)
    while True:
        Linhas()
        resposta = input("Quer adicionar um novo produto?\n1-Sim\n2-Nao\n")

        if resposta == "1":
            pass
            break

        elif resposta == "2":
            Linhas()
            ANOTANDO = False
            break

        else:
            print("Utilizar apenas as respostas sugeridas!!!")

NOME_PRODUTOS, UNIDADES_VENDIDAS = ShellSort(NOME_PRODUTOS, UNIDADES_VENDIDAS)'''

lista = ["A", "B", "C", "D"]
# FAÇA A ANIMAÇÃO DO RANKING