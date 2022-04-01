#!/bin/python

class _board:
    def __init__(self):
        self.board = {
            '1': ' ',
            '2': ' ',
            '3': ' ',
            '4': ' ',
            '5': ' ',
            '6': ' ',
            '7': ' ',
            '8': ' ',
            '9': ' ',
        }

    def printboard(self):
        print(
            f"""
 {self.board['7']} | {self.board['8']} | {self.board['9']}     7 | 8 | 9
———|———|———   ———|———|———
 {self.board['4']} | {self.board['5']} | {self.board['6']}     4 | 5 | 6
———|———|———   ———|———|———
 {self.board['1']} | {self.board['2']} | {self.board['3']}     1 | 2 | 3
            """
        )

    def limpiar(self):
        for i in self.board:
            self.board[i] = ' '
