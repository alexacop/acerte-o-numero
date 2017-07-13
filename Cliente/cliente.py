#coding: utf-8
import socket

print('Digite o IP do servidor.')
HOST = raw_input()
print
print('Digite a porta a ser utilizada.')
PORT = input()
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
try:
	tcp.connect(destino)
except Exception as e:
	print('Servidor desconhecido.')
	exit()

print
print('-----Bem-vindo ao jogo acerte o número-----')
print 
print('Pressione a dificuldade desejada: ')
print('e(Easy) - Intervalo de 0 a 100 | n(Normal) Intervalo de 0 a 1000 | h(Hard) - Intervalo de 0 a 10000.')

dificuldade = raw_input()
tcp.send(dificuldade)

print('Digite um chute inicial.')

mensagem = ''

while mensagem <> 'q':
	mensagem = raw_input()
	tcp.send(mensagem)
	mensagem_recebida = tcp.recv(1024)
	print(mensagem_recebida)

tcp.close()
