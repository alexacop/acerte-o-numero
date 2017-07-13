#coding: utf-8
from random import *
import socket

HOST = ''     
print('Digite a porta a ser utilizada.')
PORT = input()
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)

try:
    tcp.bind(origem)
except Exception as e:
    print('Falha ao conectar.')
    exit()

tcp.listen(1)

num_rand100 = randint(0, 100)
num_rand1000 = randint(0, 1000)
num_rand10000 = randint(0, 10000)

qtdTentivas = 0

while True:
    conn, cliente = tcp.accept()
    print(cliente)

    num_rand = 0

    dificuldade = conn.recv(1024)
    if(dificuldade == 'e'):
        num_rand = num_rand100
        qtdTentivas = 20
    elif(dificuldade == 'n'):
        num_rand = num_rand1000
        qtdTentivas = 15 
    elif(dificuldade == 'h'):
        num_rand10000
        qtdTentivas = 10

    while True: 
        mensagem = conn.recv(1024)
        
        if(not mensagem): 
            break
        else:
            mensagem = int(mensagem)

            if(qtdTentivas == 0):
                conn.send('Que pena, você atingiu o limite de tentativas. ')
                conn.send('Pressione q para sair.')
                break
            if(mensagem > num_rand100):
            	conn.send('O número procurado é menor que o número inserido. ')
                qtdTentivas = qtdTentivas - 1
                qtdTentivas = str(qtdTentivas)
                conn.send('Quantidade de tentivas restantes: ' + qtdTentivas)
                qtdTentivas = int(qtdTentivas)
            elif(mensagem < num_rand100):
            	conn.send('O número procurado é maior que o número inserido. ')
                qtdTentivas = qtdTentivas - 1
                qtdTentivas = str(qtdTentivas)
                conn.send('Quantidade de tentivas restantes: ' + qtdTentivas)
                qtdTentivas = int(qtdTentivas)
            else:
            	conn.send('Parabéns, você acertou.')
                conn.send('Pressione q para sair.')
                break

    print 'Conexão com o cliente encerrada', cliente
    conn.close()
    num_rand100 = randint(0, 100)
    num_rand1000 = randint(0, 1000)
    num_rand10000 = randint(0, 10000)
