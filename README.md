# Trabalho Final - Redes de Computadores 2017.1

## Professor Arthur Callado
## Membros da Equipe: Lucas da Silva Costa e Alex Sandro Alves de Sousa

### Tutorial

O jogo consiste basicamente em tentar acertar o número que será gerado aleatoriamente pelo servidor. O cliente no caso seleciona a dificuldade desejada e de acordo com essa dificuldade (Easy, Normal e Hard) o intervalo de 

possibilidades

 para o número gerado aleatoriamente pelo servidor aumenta. No modo Easy o intervalo do número fica entre 0 e 100, no modo Normal o intervalo do número fica entre 0 e 1000 e no modo Hard o intervalo do número fica entre 0 e 10000. O jogo ainda possui um limite de tentativas que também varia de acordo com a dificuldade selecionada pelo cliente. Para o modo Easy temos 20 tentativas, para o modo Normal temos 15 tentativas e para o modo Hard temos 10 tentativas.

Para a execução do jogo basta executar o arquivo servidor.py da pasta Servidor e informar a porta a ser utilizada no terminal. Em seguida basta executar o arquivo cliente.py da pasta Cliente e informar o IP e porta no terminal. Feito isso basta seguir as instruções informadas no jogo.
