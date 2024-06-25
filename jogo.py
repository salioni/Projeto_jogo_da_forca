import desenhos as d
from random import choice 
import bd

# random é uma biblioteca do python com várias funções de sorteio
# choice é uma função de sorteio aleatório em uma lista

# usando lower para uma melhor leitura de dados futuros, deixando todos os caracteres minúsculos
# usando strip para evitar a possibilidade de haver espaços no início ou no final dos dados inseridos pelo usuário
# palavra = input("Digite uma palavra secreta: ").upper().strip()

# forma de sortear a palavra a ser adivinhada, dentro de uma lista
# a var arquivo, no cmd open, está usando r como read (seu modo de leituras dos dados do arq)
def jogar():
    lista_palavras = list()
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)
        
    palavra_sorteada = choice(lista_palavras)

    # usando o laço de repetição com espaços para esconder a informação da pergunta acima no terminal 
    for x in range(50):
        print()

    # criando listas para ir inserindo as letras da palavra a ser adivinhada
    digitadas = []
    acertos   = []
    erros     = 0
    
    nome = input('Quem está jogando?')

    # laço de repetição que vai até o jogador ganhar ou perder o jogo

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
        
        # * CONDIÇÃO DE VITÓRIA
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break
        
        # * TENTATIVAS
        # o continue vai fazer com que a execução volte para while true para ser possível digitar novamente
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou essa letra!')
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')
                

        # desenhando a forca:
        score = d.desenhar_forca(erros)
        
        # * CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta era {palavra_sorteada}.')
            break
        
    bd.inserir_dado(nome,score)

    # para salvar no banco de dados 
