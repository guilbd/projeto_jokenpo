# Jogo Pedra Papel Tesoura.

from random import randint
from time import sleep
from rich import print
from rich.progress import track
from time import sleep

pedra = papel = tesoura = vitoriasJogador = vitoriasComputador = empates = 0
jogador = reiniciar =  ''
nomeJogador = str(input('Digite seu nome: ')).strip().title()
computador = randint(0,2)

for step in track(range(10), description= ":man_technologist: [green_yellow] Carregando o jogo"):
    sleep(.2)
    step

while True:
    rodadas = int(input('Quantas rodadas deseja jogar? '))
    for i in range(rodadas): 
        jogador = int(input('''
        Digite:
        [0] para PEDRA \U0000270A
        [1] para PAPEL \U0000270B
        [2] para TESOURA \U0000270C
        '''))
        print(f'{nomeJogador} escolheu {jogador}')
        sleep(2)
        print(f'Computador escolheu {computador}')
        if computador == 0:
            if jogador == 0:
                empates += 1
                print('[blue]EMPATE')
            elif jogador == 1:
                vitoriasJogador += 1
                print(f' {nomeJogador}, você [yellow]VENCEU!!!')
            elif jogador == 2:
                vitoriasComputador += 1
                print(f'{nomeJogador}, você foi [red]DERROTADO...')
        if computador == 1:
            if jogador == 1:
                empates += 1
                print('[blue]EMPATE')
            elif jogador == 0:
                vitoriasJogador += 1
                print(f' {nomeJogador}, você [yellow]VENCEU!!!')
            elif jogador == 2:
                vitoriasComputador += 1
                print(f'{nomeJogador}, você foi [red]DERROTADO...')
        if computador == 2:
            if jogador == 2:
                empates += 1
                print('[blue]EMPATE')
            elif jogador == 0:
                vitoriasJogador += 1
                print(f' {nomeJogador}, [yellow]você VENCEU!!!')
            elif jogador == 1:
                vitoriasComputador += 1
                print(f'{nomeJogador}, você foi [red]DERROTADO...')
    reiniciar = input('Deseja jogar novamente? [S/N] ').upper().strip()[0]
    if reiniciar == 'N':
        break
            
print(f'''
ESTATÍSTICAS DO JOGO:

{nomeJogador} venceu {vitoriasJogador} vezes
Computador venceu {vitoriasComputador} vezes
Houveram {empates} empates.

''')
trofeu = ('''[yellow]
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
                    
''')
if vitoriasJogador > vitoriasComputador:
    print(f'''O grande campeão foi: {nomeJogador}
    {trofeu}''')
elif vitoriasJogador == vitoriasComputador:
    print('Não houve um campeão... [yellow]EMPATE!!!')
else:
    print(f'''O grande campeão foi: Computador
    {trofeu}''')


