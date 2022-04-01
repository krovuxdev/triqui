import config.Board as Board
import random, time, os, sys
b = Board._board()

class colorprint:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[01m'
    END = '\033[0m'


class player:
    
    def __init__(self, players=None):
        self.p1_name = players
        self.triqui = '''
▀█▀ █▀▄ ▀█▀ ▄▀▀▄ █░░█ ▀█▀
░█░ █▀▄ ░█░ █░▄█ █░░█ ░█░
░▀░ ▀░▀ ▀▀▀ ░▀▀▀ ░▀▀░ ▀▀▀    

        '''

    def Carga(self):
        self.c = [
        '⚪ ◉ ◉',
        '◉ ⚪ ◉',
        '◉ ◉ ⚪',
        '⚪ ◉ ◉',
        '◉ ⚪ ◉',
        '◉ ◉ ⚪',
        '⚪ ◉ ◉',
        '◉ ⚪ ◉',
        '◉ ◉ ⚪',
        '⚪ ◉ ◉',
        '◉ ⚪ ◉',
        '◉ ◉ ⚪',
        ]
        for i in self.c:
            print(i, end='\r')
            time.sleep(.3)
    def win(self, num):
        global won, your
        if num == f'{colorprint.GREEN}x{colorprint.END}':
            if b.board['7']==b.board['5']==b.board['3']==num or b.board['9']==b.board['5']==b.board['1']== num:
                won = True
                nam = player(your)
                b.printboard()
                print(f'{colorprint.GREEN} Ganaste x felicitacion {nam.p1_name} {colorprint.END}')
                time.sleep(5)
            elif b.board['7']==b.board['4']==b.board['1']== num or b.board['8']==b.board['5']==b.board['2']==num or b.board['9']==b.board['6']==b.board['3']== num:
                won = True
                b.printboard()
                nam = player(your)
                print(f'{colorprint.GREEN} Ganaste x felicitacion {nam.p1_name} {colorprint.END}')
                time.sleep(5)
            elif b.board['7']==b.board['8']==b.board['9']== num or b.board['4']==b.board['5']==b.board['6']==num or b.board['1']==b.board['2']==b.board['3']== num:
                won = True
                nam = player(your)
                b.printboard()
                print(f'{colorprint.GREEN} Ganaste x felicitacion {nam.p1_name} {colorprint.END}')
                time.sleep(5)

        elif num == f'{colorprint.RED}o{colorprint.END}':
            if b.board['7']==b.board['5']==b.board['3']==num or b.board['9']==b.board['5']==b.board['1']== num:
                won = True
                b.printboard()
                print(f'{colorprint.RED} Perdiste el gano computador {num} {colorprint.END}')
                time.sleep(5)
            elif b.board['7']==b.board['4']==b.board['1']== num or b.board['8']==b.board['5']==b.board['2']==num or b.board['9']==b.board['6']==b.board['3']== num:
                won = True
                b.printboard()
                print(f'{colorprint.RED} Perdiste el gano computador {num} {colorprint.END}')
                time.sleep(5)
            elif b.board['7']==b.board['8']==b.board['9']== num or b.board['4']==b.board['5']==b.board['6']==num or b.board['1']==b.board['2']==b.board['3']== num:
                won = True
                b.printboard()
                print(f'{colorprint.RED} Perdiste el gano computador {num} {colorprint.END}')
                time.sleep(5)
    def clear(self):
        self.cls = 'cls' if sys.platform.startswith("windows") else 'clear'
        os.system(self.cls)
    def Games(self):
        global count, turno_player, won
        won = False
        turno_player = True
        count = 0
        while count != 9 and True != won:
            try:
                player(self.p1_name).condicion()
            except ValueError as e:
                print(e)

    def condicion(self):
        global count, turno_player, readnum
        if turno_player:
            b.printboard()
            print(f'su turno {self.p1_name}')
            pl = input('x: ')
            if int(pl) > 9:
                print('No, debe tener 0 hasta 9 ')
            elif b.board[pl] == ' ':
                b.board[pl] = f'{colorprint.GREEN}x{colorprint.END}'
                count += 1
                x = f'{colorprint.GREEN}x{colorprint.END}'
                player().clear()
                player().win(x)
                readnum.remove(pl)
                turno_player = False
            else:
                print(f'\n{colorprint.RED}ops, ya ha cogido antes{colorprint.END}')
        else:
            b.printboard()
            print(f'Su turno Computador inteligencia')
            rv = random.choice(readnum)
            player().Carga()
            if b.board[rv] == ' ':
                b.board[rv] = f'{colorprint.RED}o{colorprint.END}'
                count += 1
                o = f'{colorprint.RED}o{colorprint.END}'
                player().clear()
                player().win(o)
                readnum.remove(rv)
                turno_player = True

    def yours(self):
        opcion= input('Quiere poner su nombres: Si/no: ')
        if  opcion == 'si':
            nombres = input('Por favor escriba su nombre: ')
            self.pase= str(nombres)
            time.sleep(.5)
            player().clear()
        else:
            self.pase= None
    def Repetir(self):
        print('Quiere jugar otra vez? Si/No')
        opcion = input()
        if  opcion == 'si':
            player().clear()
            player().jugar()
    def jugar(self):
        global readnum, your, intro
        print('Bienvenido a nuestro proyecto triqui')
        print(colorprint.GREEN)
        print(self.triqui)
        print(colorprint.END)
        time.sleep(3)
        player().clear()

        readnum = ['1','2','3','4','5','6','7','8','9']
        b.limpiar()
        self.name = player()
        self.name.yours()
        your = self.name.pase
        self.game = player(your)
        self.game.Games()
        player().Repetir()


if __name__ == '__main__':
    player().jugar()
    print('Gracias por jugar :)')






