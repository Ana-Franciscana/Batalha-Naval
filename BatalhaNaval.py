import random


#criação dos tabuleiros
def criar_tabuleiro(Tabuleiro):
   for contador in range(10):
       Tabuleiro.append([ "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ "])


#Exibir Tabuleiro
def exibir_tabuleiro(tabuleiro,jogador):
   print(f"\n-Tabuleiro {jogador}-")
   for x in tabuleiro:
       print("".join(x))
   print()


#Posicionar Barcos do Computador
def posicionar_barcospc(Tabuleiro,Barcos):
   for chaves in Barcos:
       direcao = random.choice(["h", "v"])
       if direcao == "h":
           linha = random.randint(0, 9 )
           coluna = random.randint(0, 9 - chaves)


           if Tabuleiro[linha][coluna] != "= ":
               for contador in range(chaves):
                   Tabuleiro[linha][coluna + contador] = '= '
           else:
               while Tabuleiro[linha][coluna] == "= ":
                   linha = random.randint(0, 9)
                   coluna = random.randint(0, 9 - chaves)


                   for contador in range(chaves):
                       Tabuleiro[linha][coluna + contador] = '= '


       else:
           linha = random.randint(0, 9 - chaves)
           coluna = random.randint(0, 9 )


           if Tabuleiro[linha][coluna] != "= ":
               for contador in range(chaves):
                   Tabuleiro[linha + contador][coluna] = '= '
           else:
               while Tabuleiro[linha][coluna] == "= ":
                   linha = random.randint(0, 9 - chaves)
                   coluna = random.randint(0, 9)


                   for contador in range(chaves):
                       Tabuleiro[linha + contador][coluna] = '= '
   return Tabuleiro




#posicionar Barcos do Jogador
def posicionar_BarcosJogador(Tabuleiro,Barcos):
   exibir_tabuleiro(Tabuleiro, 'Jogador')
   for chaves in Barcos:
       print(f"Posicionando barco {chaves}")
       direcao = input("Digite a direção que deseja posicionar (h - Horizontal, v - Vertical): ")


       if direcao == "h":


           linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))
           while verificar_jogada(linha) == True:
                   linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))


           coluna = int(input("Digite a coluna que deseja posicionar (0 - 9): "))
           while verificar_jogada(coluna) == True:
               coluna = int(input("Digite a linha que deseja posicionar (0 - 9): "))


           if Tabuleiro[linha][coluna] != "= ":
               for contador in range(chaves):
                   Tabuleiro[linha][coluna + contador] = '= '
               exibir_tabuleiro(Tabuleiro, 'Jogador')


           elif Tabuleiro[linha][coluna] == "= ":
               while Tabuleiro[linha][coluna] == "= ":
                   print("O local escolhido já está ocupado, digite outro indice")


                   linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))
                   coluna = int(input("Digite a coluna que deseja posicionar (0 - 9): "))


                   for contador in range(chaves):
                       Tabuleiro[linha][coluna + contador] = '= '
                   exibir_tabuleiro(Tabuleiro, 'Jogador')
                   break




       else:
           linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))
           while verificar_jogada(linha) == True:
               linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))


           coluna = int(input("Digite a coluna que deseja posicionar (0 - 9): "))
           while verificar_jogada(coluna) == True:
               coluna = int(input("Digite a linha que deseja posicionar (0 - 9): "))


           if Tabuleiro[linha][coluna] != "= ":
               for contador in range(chaves):
                   Tabuleiro[linha + contador][coluna ] = '= '
               exibir_tabuleiro(Tabuleiro, 'Jogador')


           elif Tabuleiro[linha][coluna] == "= ":
               while Tabuleiro[linha][coluna] == "= ":
                   print("O local escolhido já está ocupado, digite outro indice")
                   linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))
                   coluna = int(input("Digite a coluna que deseja posicionar (0 - 9): "))


                   for contador in range(chaves):
                       Tabuleiro[linha + contador][coluna] = '= '
                   exibir_tabuleiro(Tabuleiro, 'Jogador')
                   break


   return Tabuleiro


def jogar(Tabuleiro, linha, coluna):
   if Tabuleiro[linha][coluna] == "= ":
       Tabuleiro[linha][coluna] = 'X '
       return True
   elif Tabuleiro[linha][coluna] == "~ ":
       Tabuleiro[linha][coluna] = 'O '
   return False




def verificar_jogada(dado):
   if dado < 0 or dado > 9:
       print("Digite um número válido")
       return True


   return False


def contar_navios(Tabuleiro):
   contagem = 0
   for linha in Tabuleiro:
       for elemento in linha:
           if elemento == "= ":
               contagem += 1


   return contagem




#jogo
Tabuleiro_jogador = []
Tabuleiro_computador = []
tabuleiro_visivelpc = []


#criar Tabuleiros
criar_tabuleiro(Tabuleiro_computador)
criar_tabuleiro(tabuleiro_visivelpc)
criar_tabuleiro(Tabuleiro_jogador)


#posicionamento dos barcos do jogador
Barcos = [1,2,3,4,5]
posicionar_BarcosJogador(Tabuleiro_jogador,Barcos)


#posicionar barcos do computador
posicionar_barcospc(Tabuleiro_computador,Barcos)
exibir_tabuleiro(Tabuleiro_computador,"visivel")


while True:
   print("---Jogo iniciado---")


   exibir_tabuleiro(Tabuleiro_jogador, "Jogador")
   exibir_tabuleiro(tabuleiro_visivelpc, "Computador")


   #jogada Jogador
   linha = int(input("Digite a linha que deseja jogar: (0 a 9)" ))
   while verificar_jogada(linha) == True:
       linha = int(input("Digite a linha que deseja posicionar (0 - 9): "))
   coluna = int(input("Digite a coluna que deseja jogar: (0 a 9)"))
   while verificar_jogada(coluna) == True:
       coluna = int(input("Digite a linha que deseja posicionar (0 - 9): "))
   verificar_acerto = jogar(Tabuleiro_computador, linha, coluna)


   exibir_tabuleiro(Tabuleiro_jogador, "Jogador")
   exibir_tabuleiro(tabuleiro_visivelpc, "Computador")


   if verificar_acerto == True:
       print("Você acertou um barco inimigo")
       tabuleiro_visivelpc[linha][coluna] = 'X '
   else:
       print("Você errou")
       tabuleiro_visivelpc[linha][coluna] = 'O '


   #Verificar se todos os navios do computador foram destruidos
   if contar_navios(Tabuleiro_computador) == 0:
       print("Parabéns, você venceu!")
       break


   #jogada computador
   print("O computador está fazendo sua jogada ...")
   linha_PC = random.randint(0,9 )
   coluna_PC = random.randint(0,9)
   verificar_acerto_PC = jogar(Tabuleiro_jogador, linha_PC, coluna_PC)


   exibir_tabuleiro(Tabuleiro_jogador, "Jogador")


   if verificar_acerto_PC == True:
       print("O computador acertou um barco inimigo")


   else:
       print("O computador errou")


   #Verificar se todos os navios do jogaodr foram destruidos
   if contar_navios(Tabuleiro_jogador) == 0:
       print("O computador venceu!")
       break











