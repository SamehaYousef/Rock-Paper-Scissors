#!/usr/bin/env python3

# """This program plays a game of Rock, Paper, Scissors, Spock,
# Lizard between two Players,and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# """The Player class is the parent class for all of the Players
# in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'lizard') or
            (one == 'lizard' and two == 'spock') or
            (one == 'spock' and two == 'scissors') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'lizard' and two == 'paper') or
            (one == 'paper' and two == 'spock') or
            (one == 'spock' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.count1 = 0
        self.p2.count2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        self.p2.learn(move1, move2)

        beat = beats(move1, move2)

        if (beat):
            print("\tPlayer1 WINS the round!")
            self.p1.count1 += 1

        elif (move1 == move2):
            print("\tIts a DRAW!")

        else:
            print("\tPlayer2 WINS the round!")
            self.p2.count2 += 1

        print(f"""Player1 score: {self.p1.count1}\n
Player2 score: {self.p2.count2}\n""")

    def play_game(self):

        print("Game start!")
        for round in range(50):
            print(f"Round {round}:")
            self.play_round()
            if (self.p1.count1 == 3 or self.p2.count2 == 3):
                break
        print("\u001b[1m \u001b[4m GAME OVER! \n")
        print(f"""Player1 score: {self.p1.count1}\n
Player2 score: {self.p2.count2}\n""")
        if (self.p1.count1 > self.p2.count2):
            print("\u001b[4m Player1 WINS!! \n")
        elif (self.p1.count1 == self.p2.count2):
            print("\u001b[4m It's a Draw!! \n")
        else:
            print(f"\u001b[4m Player2 WINS!! \n")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while(True):
            choice = input("Rock, paper, scissors, lizard, spock? > ").lower()
            if (choice in moves):
                return choice


class ReflectPlayer(Player):
    def __init__(self):
        self.turn = 0

    def move(self):
        if (self.turn == 0):
            self.turn += 1
            return random.choice(moves)

        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = my_move
        return my_move


class CyclePlayer(Player):
    def __init__(self):
        self.position = 0

    def move(self):
        if (self.position == 3):
            self.position = 0
        choice = moves[self.position]
        self.position += 1
        return choice


if __name__ == '__main__':
    while(True):
        print("\u001b[37;1m")
        print("\u001b[44;1m")
        choice = input("""Please enter your choice (random, player,
cycle, reflector, human-human, random-random): """).lower()
        if (choice == 'random'):
            game = Game(HumanPlayer(), RandomPlayer())
            break
        elif (choice == 'cycle'):
            game = Game(HumanPlayer(), CyclePlayer())
            break
        elif (choice == 'reflector'):
            game = Game(HumanPlayer(), ReflectPlayer())
            break
        elif (choice == 'player'):
            game = Game(Player(), Player())
            break
        elif (choice == 'human-human'):
            game = Game(HumanPlayer(), HumanPlayer())
            break
        elif (choice == 'random-random'):
            game = Game(RandomPlayer(), RandomPlayer())
            break

    game.play_game()
