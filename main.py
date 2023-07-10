""" this is the python file responsible for running the game """
from os import system
from game import RockPaperScissor

ASK_USER_NAME = ''

while ASK_USER_NAME == '':
    ASK_USER_NAME = input('Before we begin what is your name? ')
    system('cls')


game_instance = RockPaperScissor(ASK_USER_NAME)
game_instance.ask_user_main_menu()
