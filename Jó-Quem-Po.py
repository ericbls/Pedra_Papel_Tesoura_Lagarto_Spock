from random import randint
modo=int(input('digite 1 para 1 player e 2 para 2 players_'))
c1=0 #número de vitórias do jogador 1
c2=0 #número de vitórias do jogador 2 (CPU ou jogador humano)
n1=0 #numero de rodadas que o jogador 1 venceu dentro de uma partida (se vencer 3 rodadas, vence uma partida)
n2=0 #numero de rodadas que o jogador 2 venceu dentro de uma partida (se vencer 3 rodadas, vence uma partida)
while(modo==1): #jogo individual
    jogador1=input('digite sua jogada, jogador 1_')
    jogador2=randint(1,5)
    if(jogador2==1):
        jogador2='tesoura'
    elif(jogador2==2):
        jogador2='papel'
    elif(jogador2==3):
        jogador2='pedra'
    elif(jogador2==4):
        jogador2='spock'
    else:
        jogador2='lagarto'
    if(jogador1=='pedra' and jogador2=='tesoura'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='tesoura' and jogador2=='papel'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='papel' and jogador2=='pedra'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='pedra' and jogador2=='lagarto'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='lagarto' and jogador2=='spock'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='spock' and jogador2=='tesoura'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='tesoura' and jogador2=='lagarto'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='papel' and jogador2=='spock'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='pedra' and jogador2=='tesoura'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='lagarto' and jogador2=='papel'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='spock' and jogador2=='pedra'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador2=='pedra' and jogador1=='tesoura'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='tesoura' and jogador1=='papel'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='papel' and jogador1=='pedra'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='pedra' and jogador1=='lagarto'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='lagarto' and jogador1=='spock'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='spock' and jogador1=='tesoura'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='tesoura' and jogador1=='lagarto'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='papel' and jogador1=='spock'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='pedra' and jogador1=='tesoura'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='lagarto' and jogador1=='papel'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='spock' and jogador1=='pedra'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador1==jogador2):
        print('empatou')
        n1=0
        n2=0
    else:
        print('voce digitou algo invalido')
    if(n1==3):
        c1=c1+1
        print('jogador1 venceu a sua %i# partida'%(c1))
        mode=input('digite o modo de jogo 1 ou 2_')
    if(n2==3):
        c2=c2+1
        print('jogador2 venceu a sua %i# partida'%(c2))
        modo=input('digite o modo de jogo 1 ou 2_')
while(modo==2): #jogo de 2 jogadores
    jogador1=input('digite sua jogada, jogador 1_')
    jogador2=input('digite sua jogada, jogador 2_')
    if(jogador1=='pedra' and jogador2=='tesoura'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='tesoura' and jogador2=='papel'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='papel' and jogador2=='pedra'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='pedra' and jogador2=='lagarto'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='lagarto' and jogador2=='spock'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='spock' and jogador2=='tesoura'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='tesoura' and jogador2=='lagarto'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='papel' and jogador2=='spock'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='pedra' and jogador2=='tesoura'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='lagarto' and jogador2=='papel'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador1=='spock' and jogador2=='pedra'):
        print('jogador1 vence')
        n1=n1+1
        n2=0
    elif(jogador2=='pedra' and jogador1=='tesoura'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='tesoura' and jogador1=='papel'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='papel' and jogador1=='pedra'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='pedra' and jogador1=='lagarto'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='lagarto' and jogador1=='spock'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='spock' and jogador1=='tesoura'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='tesoura' and jogador1=='lagarto'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='papel' and jogador1=='spock'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='pedra' and jogador1=='tesoura'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='lagarto' and jogador1=='papel'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador2=='spock' and jogador1=='pedra'):
        print('jogador2 vence')
        n2=n2+1
        n1=0
    elif(jogador1==jogador2):
        print('empatou')
        n1=0
        n2=0
    else:
        print('voce digitou algo invalido')
    if(n1==3):
        c1=c1+1
        print('jogador1 venceu a sua %i# partida'%(c1))
        mode=input('digite o modo de jogo 1 ou 2_')
    if(n2==3):
        c2=c2+1
        print('jogador2 venceu a sua %i# partida'%(c2))
        modo=input('digite o modo de jogo 1 ou 2_')
if(modo!=1 and modo!=2):
    print('digite 1 ou 2')