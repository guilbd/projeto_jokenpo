# Jogo Pedra Papel Tesoura.

from random import randint
from time import sleep

pedra = papel = tesoura = vitoriasJogador = vitoriasComputador = empates = 0
papel = 0
tesoura = 0

jogador = ''
reiniciar = ''

nomeJogador = str(input('Digite seu nome: ')).strip().title()
computador = randint(0,2)

while True:
    rodadas = int(input('Quantas rodadas deseja jogar? '))
    for i in range(rodadas): 

        jogador = int(input('''
        Digite:
        [0] para PEDRA
        [1] para PAPEL
        [2] para TESOURA
        '''))
        print(f'{nomeJogador} escolheu {jogador}')
        sleep(2)
        print(f'Computador escolheu {computador}')
        if computador == 0:
            if jogador == 0:
                empates += 1
                print('EMPATE')
            elif jogador == 1:
                vitoriasJogador += 1
                print(f' {nomeJogador}, você VENCEU!!!')
            elif jogador == 2:
                vitoriasComputador += 1
                print(f'{nomeJogador}, você foi DERROTADO...')
        if computador == 1:
            if jogador == 1:
                empates += 1
                print('EMPATE')
            elif jogador == 0:
                vitoriasJogador += 1
                print(f' {nomeJogador}, você VENCEU!!!')
            elif jogador == 2:
                vitoriasComputador += 1
                print(f'{nomeJogador}, você foi DERROTADO...')
        if computador == 2:
            if jogador == 2:
                empates += 1
                print('EMPATE')
            elif jogador == 0:
                vitoriasJogador += 1
                print(f' {nomeJogador}, você VENCEU!!!')
            elif jogador == 1:
                vitoriasComputador += 1
                print(f'{nomeJogador}, você foi DERROTADO...')
    reiniciar = input('Deseja jogar novamente? [S/N] ').upper().strip()[0]
    if reiniciar == 'N':
        break
    

        
print(f'''
ESTATÍSTICAS DO JOGO:

{nomeJogador} venceu {vitoriasJogador} vez(es)
Computador venceu {vitoriasComputador} vez(es)
Houveram {empates} empates.

''')
trofeu = ('''
          ...                              ...          
        :=++==-                          -=+**+:        
       -+=::==+     .......::::::...    :+++.:=*-       
      .=- .-++-.:-----======+++++==++++-:=*+=. =+.      
      :+. -=:  =--::::---===++++=-===****  -+- :+:      
      .=. .--::::::::::--==--=++=-+=+***=-=+-. :+.      
       --    .:==::::::----==+++--+=****+-.    =-       
       .-:      .:::::::-====+++--==***:      :=.       
        .-.      :::::::--===+++=+++**+      :=.        
         .-.     ::::::::--==+++--==**=     :=.         
          .-:    .:::::::--==+++--==**-    :-.          
            ::   .:::::::--=++++=+++**-  .-:            
             .-. .:::::::--==+++-==+**: :=.             
               :-.::::::---==++=-=-+**:=:               
                .-::::::--===+++=+=***-.                
                 :------===+++*******+-                 
                 :..===++++++*******:::                 
                     :-++===++***=:                     
                       .---=+++*.                       
                        .-==+*+.                        
                          -=++                          
                          ::==                          
                      ..:-:-=++-..                      
                      #%%%%@@@@@@#                      
                   -*#@%%%%%%@@@@@#*-                   
                  :%%%%%%%%%%%@%%%%@@-                  
                  #%%%%%%%%%%@@%%%%@@%                  
                  %%%%+==+++++*+==%%@@                  
                  %%%%======++++--%%@@                  
                 =@%%%%#####%%%%##%%@@=                 
                 .=++**#########***++=:   
''')
if vitoriasJogador > vitoriasComputador:
    print(f'''O grande campeão foi: {nomeJogador}
    {trofeu}''')
elif vitoriasJogador == vitoriasComputador:
    print('Não houve um campeão... EMPATE!!!')
else:
    print(f'''O grande campeão foi: Computador
    {trofeu}''')


