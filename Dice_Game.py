import random
import msvcrt


class Die:
    def __init__(self, name):
        self.value = None
        self.name = name

    def roll(self):
        self.value = random.randint(1, 6)

    def get_die_value(self):
        return self.value


class Player:
    def __init__(self, die, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.counter = 10
        self.die = die

    def get_name(self):
        return self.name

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1

    def roll_die(self):
        return self.die.roll()

    def get_counter(self):
        return self.counter

    def get_die_value_p(self):
        return self.die.get_die_value()

    def reset(self):
        self.counter = 10


class DiceGame:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round_counter = 1
        self.rounds = {}
        self.round_winner = None
        self.round_looser = None
        self.game_winner = None

    # Player Action Methods

        # Roll Die Methods

    def roll_die_p1(self):
        print(f'{p1.get_name()} Rolling Die...')
        return self.p1.roll_die()

    def roll_die_p2(self):
        print(f'{p2.get_name()} Rolling Die...')
        return self.p2.roll_die()

    def get_die_value_p1(self):
        return self.p1.get_die_value_p()

    def get_die_value_p2(self):
        return self.p2.get_die_value_p()

    def get_round_winner(self):
        return self.round_winner.get_name()

    def get_round_looser(self):
        return self.round_looser.get_name()

        # Counter Methods

    def update_counters(self):
        self.round_winner.decrement()
        self.round_looser.increment()

    # Game Progression Methods

    def announce_start(self):
        print("The Game Started")

    def increment_round(self):
        self.round_counter += 1

    def determine_round_winner_looser(self):
        if self.get_die_value_p1() > self.get_die_value_p2():
            self.round_winner = self.p1
            self.round_looser = self.p2
        else:
            self.round_winner = self.p2
            self.round_looser = self.p1

    def print_round_results(self):

        #Prints what each player rolled
        print(f"{self.p1.get_name()} rolled :{self.get_die_value_p1()}")
        print(f"{self.p2.get_name()} rolled :{self.get_die_value_p2()}")

        #Prints current counters of each player
        print(f"{self.p1.get_name()} counter is {self.p1.get_counter()}")
        print(f"{self.p2.get_name()} counter is {self.p2.get_counter()}")

    def announce_round_winner(self):
        print(f"Round winner is {self.get_round_winner()}")


    def update_round(self):
        self.rounds[self.round_counter] = {
            "Winner": self.get_round_winner,
            "Looser": self.get_round_looser,
        }

    def announce_new_round(self):
        print(f"round: {self.round_counter} started")

    def game_over(self):
        if self.p1.get_counter() == 0:
            print(f'Winner of the game is {self.p1.get_name()}')
        elif self.p2.get_counter() == 0:
            print(f'Winner of the game is {self.p2.get_name()}')

die1 = Die('Die 1')
die2 = Die('Die 2')

p1 = Player(die1, 'Tofa')
p2 = Player(die2, 'Computer', is_human = False)

game = DiceGame(p1, p2)

game.announce_start()

while p1.get_counter() != 0 and p2.get_counter() != 0:
    print('=' * 50)
    game.announce_new_round()
    print('Press any key to roll dice')
    msvcrt.getch()
    game.roll_die_p1()
    game.roll_die_p2()
    game.determine_round_winner_looser()
    game.update_counters()
    game.print_round_results()
    game.announce_round_winner()
    game.update_round()
    game.increment_round()
    print('=' * 50)

game.game_over()