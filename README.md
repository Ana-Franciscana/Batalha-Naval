# Batalha Naval em Python ⚓

Um jogo de Batalha Naval executado no terminal, desenvolvido individualmente em Python em 2024, durante o primeiro período da graduação em Análise e Desenvolvimento de Sistemas.

## Sobre o projeto

Este foi meu primeiro projeto de programação desenvolvido sozinha. Ele surgiu a partir de uma atividade extracurricular proposta pelo professor no primeiro período da faculdade. Naquele momento, eu estava tendo meus primeiros contatos com programação e com conceitos como listas, matrizes, funções e estruturas de repetição.

A proposta era desenvolver uma versão do clássico Batalha Naval para jogar contra o computador. O computador não utiliza inteligência artificial: ele segue as regras implementadas no programa e realiza escolhas aleatórias para posicionar seus barcos e fazer suas jogadas.

Desenvolvi a primeira versão por conta própria, sem utilizar inteligência artificial. Como foi um dos meus primeiros projetos, o código reflete o nível de conhecimento que eu tinha naquela etapa da graduação. Posteriormente, retomei o projeto para acrescentar validações e melhorar a experiência de quem joga, mantendo a estrutura simples da implementação original.

## Regras do jogo

O jogo utiliza dois tabuleiros de 10 × 10: um para o jogador e outro para o computador. Cada lado possui cinco barcos, com tamanhos diferentes:

- 1 barco de tamanho 1;
- 1 barco de tamanho 2;
- 1 barco de tamanho 3;
- 1 barco de tamanho 4;
- 1 barco de tamanho 5.

Os barcos devem ser posicionados horizontalmente ou verticalmente, ocupando casas consecutivas do tabuleiro. Eles não podem ultrapassar os limites do tabuleiro nem ocupar casas já utilizadas por outro barco.

Depois do posicionamento, o jogador e o computador realizam ataques às posições do adversário. As jogadas do computador são definidas aleatoriamente com a biblioteca `random`, do Python.

O jogo termina quando um dos lados tem todos os seus barcos destruídos.

## Símbolos do tabuleiro

| Símbolo | Significado |
|---|---|
| `=` | Parte de um barco do jogador, visível no próprio tabuleiro |
| `~` | Casa em que ainda não houve jogada |
| `X` | Acerto em uma casa ocupada por um barco |
| `O` | Jogada que não atingiu um barco |


## Tecnologias e conceitos utilizados

- **Python**
- Biblioteca padrão `random` para escolher posições e jogadas aleatórias
- Listas e matrizes para representar os tabuleiros
- Funções para organizar as operações do jogo
- Condicionais e estruturas de repetição
- Validação de entradas e verificação de posições

O projeto não utiliza bibliotecas externas, inteligência artificial, interface gráfica ou conexão com a internet.

## Como executar

É necessário ter o Python 3 instalado.

## Evolução do projeto

O histórico de commits registra duas etapas do meu aprendizado:

- **Versão inicial:** primeira implementação do jogo, preservando a forma como consegui resolver o desafio em 2024, com os conhecimentos que eu tinha naquele momento.
- **Versão revisada:** acréscimo de coordenadas no tabuleiro e de validações para tornar o jogo mais consistente, sem transformar o projeto em uma implementação avançada ou abandonar sua estrutura original.

Entre as melhorias da versão revisada estão:

- Exibição das linhas de `1` a `10` e das colunas de `A` a `J`.
- Verificação de entradas numéricas antes de convertê-las em inteiros.
- Validação da direção informada pelo jogador.
- Verificação de todas as casas de um barco antes de posicioná-lo, impedindo sobreposições e posições que ultrapassem o tabuleiro.
- Impedimento de ataques repetidos na mesma posição.
- Sorteio de outra posição quando o computador tenta atacar uma casa que já foi atingida.
- Ocultação do tabuleiro secreto do computador durante a preparação da partida.

## Aprendizados

Este projeto representa meu primeiro contato prático com a construção de um jogo em Python. Durante seu desenvolvimento, pratiquei a organização de um problema em etapas, o uso de matrizes, a criação de funções, as estruturas condicionais e de repetição e a geração de escolhas aleatórias. Ao revisitar o código, também pude identificar limitações da primeira versão e acrescentar validações para lidar melhor com entradas inválidas e posições não permitidas.


## Demonstração do jogo

### Início do jogo

Apresentação inicial do jogo antes do começo da partida.

![Tela inicial do jogo](imagens/InicioDeJogo.png)

### Tabuleiro do jogador

Visualização do tabuleiro do jogador antes das jogadas, com as posições ainda sem marcações.

![Tabuleiro do jogador limpo](imagens/TabuleiroJogadorLimpo.png)

### Execução da partida

Exemplo do jogo durante a partida, mostrando as jogadas realizadas.

![Execução da partida](imagens/Execucao-da-Partida.png)

### Jogo encerrado

Registro da tela apresentada ao término da partida.

![Jogo encerrado](imagens/JogoEncerrado.png)
