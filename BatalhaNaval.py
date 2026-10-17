
import random

colunas = "ABCDEFGHIJ"


#criação dos tabuleiros
def criar_tabuleiro(Tabuleiro):
   for contador in range(10):
       Tabuleiro.append([ "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ ", "~ "])


#Exibir Tabuleiro
def exibir_tabuleiro(tabuleiro,jogador):
   print(f"\n-Tabuleiro {jogador}-")
   print("    " + " ".join(colunas))
   contador = 1
   for x in tabuleiro:
       print(f"{contador:2}  " + "".join(x))
       contador += 1
   print()


#Posicionar Barcos do Computador
def posicionar_barcospc(Tabuleiro,Barcos):
   for chaves in Barcos:
       while True:
           direcao = random.choice(["h", "v"])

           if direcao == "h":
               linha = random.randint(0, 9)
               coluna = random.randint(0, 10 - chaves)
               ocupado = False

               for contador in range(chaves):
                   if Tabuleiro[linha][coluna + contador] != "~ ":
                       ocupado = True

               if ocupado == False:
                   for contador in range(chaves):
                       Tabuleiro[linha][coluna + contador] = '= '
                   break

           else:
               linha = random.randint(0, 10 - chaves)
               coluna = random.randint(0, 9)
               ocupado = False

               for contador in range(chaves):
                   if Tabuleiro[linha + contador][coluna] != "~ ":
                       ocupado = True

               if ocupado == False:
                   for contador in range(chaves):
                       Tabuleiro[linha + contador][coluna] = '= '
                   break

   return Tabuleiro




#posicionar Barcos do Jogador
def posicionar_BarcosJogador(Tabuleiro,Barcos):
   exibir_tabuleiro(Tabuleiro, 'Jogador')

   for chaves in Barcos:
       print(f"Posicionando barco {chaves}")
       direcao = input("Digite a direção que deseja posicionar (h - Horizontal, v - Vertical): ").strip().lower()

       while direcao != "h" and direcao != "v":
           print("Direção inválida, digite h ou v")
           direcao = input("Digite a direção que deseja posicionar (h - Horizontal, v - Vertical): ").strip().lower()

       while True:
           while True:
               linha = input("Digite a linha que deseja posicionar (1 - 10): ")

               if linha.isdigit():
                   linha = int(linha)

                   if verificar_jogada(linha - 1) == False:
                       linha = linha - 1
                       break
               else:
                   print("Entrada inválida, digite apenas números")

           while True:
               coluna = input("Digite a coluna que deseja posicionar (A - J): ").strip().upper()

               if len(coluna) == 1 and coluna in colunas:
                   coluna = colunas.index(coluna)
                   break
               else:
                   print("Digite uma letra válida de A até J")

           if direcao == "h":
               if coluna + chaves > 10:
                   print("O barco ultrapassa o limite do tabuleiro, escolha outra posição")

               else:
                   ocupado = False

                   for contador in range(chaves):
                       if Tabuleiro[linha][coluna + contador] != "~ ":
                           ocupado = True

                   if ocupado == False:
                       for contador in range(chaves):
                           Tabuleiro[linha][coluna + contador] = '= '

                       exibir_tabuleiro(Tabuleiro, 'Jogador')
                       break
                   else:
                       print("O local escolhido já está ocupado, digite outro índice")

           else:
               if linha + chaves > 10:
                   print("O barco ultrapassa o limite do tabuleiro, escolha outra posição")

               else:
                   ocupado = False

                   for contador in range(chaves):
                       if Tabuleiro[linha + contador][coluna] != "~ ":
                           ocupado = True

                   if ocupado == False:
                       for contador in range(chaves):
                           Tabuleiro[linha + contador][coluna] = '= '

                       exibir_tabuleiro(Tabuleiro, 'Jogador')
                       break
                   else:
                       print("O local escolhido já está ocupado, digite outro índice")

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
       print("Digite um número válido de 1 a 10")
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


while True:
   print("---Jogo iniciado---")

   exibir_tabuleiro(Tabuleiro_jogador, "Jogador")
   exibir_tabuleiro(tabuleiro_visivelpc, "Computador")


   #jogada Jogador
   while True:
       linha = input("Digite a linha que deseja jogar (1 a 10): ")

       if linha.isdigit():
           linha = int(linha)

           if verificar_jogada(linha - 1) == False:
               linha = linha - 1
               break
       else:
           print("Entrada inválida, digite apenas números")

   while True:
       coluna = input("Digite a coluna que deseja jogar (A a J): ").strip().upper()

       if len(coluna) == 1 and coluna in colunas:
           coluna = colunas.index(coluna)

           if tabuleiro_visivelpc[linha][coluna] == "~ ":
               break
           else:
               print("Você já jogou nessa posição, escolha outra")
       else:
           print("Digite uma letra válida de A até J")

   verificar_acerto = jogar(Tabuleiro_computador, linha, coluna)

   if verificar_acerto == True:
       print("Você acertou um barco inimigo")
       tabuleiro_visivelpc[linha][coluna] = 'X '
   else:
       print("Você errou")
       tabuleiro_visivelpc[linha][coluna] = 'O '

   exibir_tabuleiro(Tabuleiro_jogador, "Jogador")
   exibir_tabuleiro(tabuleiro_visivelpc, "Computador")


   #Verificar se todos os navios do computador foram destruidos
   if contar_navios(Tabuleiro_computador) == 0:
       print("Parabéns, você venceu!")
       break


   #jogada computador
   print("O computador está fazendo sua jogada ...")
   linha_PC = random.randint(0,9)
   coluna_PC = random.randint(0,9)

   while Tabuleiro_jogador[linha_PC][coluna_PC] == 'X ' or Tabuleiro_jogador[linha_PC][coluna_PC] == 'O ':
       linha_PC = random.randint(0,9)
       coluna_PC = random.randint(0,9)

   verificar_acerto_PC = jogar(Tabuleiro_jogador, linha_PC, coluna_PC)

   print(f"O computador atacou a posição {linha_PC + 1}{colunas[coluna_PC]}")

   exibir_tabuleiro(Tabuleiro_jogador, "Jogador")


   if verificar_acerto_PC == True:
       print("O computador acertou um barco inimigo")

   else:
       print("O computador errou")


   #Verificar se todos os navios do jogador foram destruidos
   if contar_navios(Tabuleiro_jogador) == 0:
       print("O computador venceu!")
       break
