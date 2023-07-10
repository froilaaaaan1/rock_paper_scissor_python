""" this is the game rock, paper scissor using python """
from random import choice
from os import system
from sys import exit as ext
from art import tprint


class RockPaperScissor:
    """ this is the main game itself """
    choices = ['Rock', 'Paper', 'Scissor']
    user_score = 0
    computer_score = 0
    summary = []

    def __init__(self, name):
        self.name = name

    def clear_screen(self):
        """ this will clear the terminal """
        system('cls')

    def ask_user_main_menu(self):
        """ this will show on the first run only it is like a main menu """
        self.clear_screen()
        print('Welcome to Rock, Paper, and Scissor Game, ' + self.name)
        answer = input('Do you want to start? Y/N: \n')
        self.clear_screen()
        if answer.lower() == 'y':
            self.ask_user_choice()
        else:
            self.show_score()

    def ask_user_choice(self):
        """" this will ask the user for their desired choice wether rock paper or scissor """
        self.clear_screen()
        user_choice = int(input('0. Rock? \n1. Paper? \n2. Scissor?\n'))
        if user_choice not in [0, 1, 2]:
            try_again = input('Invalid choice. Try again? Y/N: ')
            if try_again.lower() == 'y':
                self.ask_user_choice()
            else:
                self.show_score()
        else:
            self.main_game(self.choices[user_choice])

    def main_game(self, user_choice):
        """ this is where the magic happens this
            will generate random choice among the rock paper
            and scissor every round and checks
            all the possible outcome that will
            happen and taking care of tracking score of both user and computer  
        """
        computer_chosen = choice(self.choices)
        print('Computers bet: ' + computer_chosen +
              '\nYou chose: ' + user_choice)
        if computer_chosen == user_choice:
            tprint("DRAW.", font='rnd-large')
            self.summary.append('Draw round')
        elif computer_chosen == 'Rock' and user_choice == 'Scissor':
            self.computer_score = self.computer_score + 1
            tprint("YOU LOSE.", font='rnd-large')
            self.summary.append('You losed this round.')
        elif computer_chosen == 'Paper' and user_choice == 'Scissor':
            self.user_score = self.user_score + 1
            tprint("YOU WIN.", font='rnd-large')
            self.summary.append('You won this round.')
        elif computer_chosen == 'Scissor' and user_choice == 'Paper':
            self.computer_score = self.computer_score + 1
            tprint("YOU LOSE.", font='rnd-large')
            self.summary.append('You losed this round.')
        elif computer_chosen == 'Rock' and user_choice == 'Paper':
            self.user_score = self.user_score + 1
            tprint("YOU WIN.", font='rnd-large')
            self.summary.append('You won this round.')
        elif computer_chosen == 'Paper' and user_choice == 'Rock':
            self.computer_score = self.computer_score + 1
            tprint("YOU LOSE.", font='rnd-large')
            self.summary.append('You losed this round.')
        elif computer_chosen == 'Scissor' and user_choice == 'Rock':
            self.computer_score = self.computer_score + 1
            tprint("YOU LOSE.", font='rnd-large')
            self.summary.append('You losed this round.')

        ask = input('Play again? Y/N \n')
        if ask.lower() != 'y':
            self.show_score()
        else:
            self.ask_user_choice()

    def show_score(self):
        """ this function act as printing the user and computer score """
        round_number = 0
        self.clear_screen()
        print('You got a score of ' + str(self.user_score) +
              ' and the computer score is ' + str(self.computer_score))
        if self.computer_score > self.user_score:
            print('You losed the game.')
        elif self.computer_score < self.user_score:
            print('You won the game.')
        else:
            print('The game is draw.')
        print('Summary of the game: ')
        for i in self.summary:
            round_number = round_number + 1
            print('Round ' + str(round_number) + ': ' + i)
        print('Thank you for playing.')
        ext(1)
