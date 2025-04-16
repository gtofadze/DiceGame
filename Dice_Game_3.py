import random
import msvcrt
import time

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

    def get_die_value(self):
        return self.die.get_die_value()

    def reset(self):
        self.counter = 10


class DiceGame:
    def __init__(self, p1, p2):
        self.players = (p1, p2)  # Tuple of all players
        self.round = {
            p: {"D": None, "C": None} for p in self.players
        }  # Die "D" and Counter "C" values of each player after roll in a current round
        self.rounds = {}  # Info of all previous rounds
        self.round_wl = {"W": None, "L": None}  # Winner and a looser in a current round
        self.round_counter = 1
        self.game_winner = None
        self.is_tie = False

    # Player Action Methods

    # Roll Die Methods

    def roll_dice(self):
        print("Rolling dice...")
        players = self.players
        for p in players:
            p.roll_die()

    def det_dice_values(self):
        r = self.round
        for p in r:
            value = p.get_die_value()
            r[p]["D"] = value

    def det_round_wl(self):
        r = self.round
        r_wl = self.round_wl

        if r[p1]['D'] != r[p2]['D']:
            self.is_tie = False

            # Determine Round Winner and a Looser
            w = max(r, key=lambda x: r[x]['D'])
            l = min(r, key=lambda x: r[x]['D'])

            # Update Counters
            w.decrement()
            l.increment()

            # Update Winner/Looser Dictionary
            r_wl['W'] = w
            r_wl['L'] = l

            # Update Counter Values
            r[w]['C'] = w.get_counter()
            r[l]['C'] = l.get_counter()
        else:
            self.is_tie = True

    # Game Progression Methods

    def announce_start(self):
        print("The Game Started")

    def increment_round(self):
        self.round_counter += 1

    def print_round_results(self):
        r = self.round

        # Prints what each player rolled
        print(" ")
        for p in r:
            name = p.get_name()
            value = r[p]['D']
            print(f"{name} rolled {value}")
        print(" ")

        # Prints current counters of each player
        print(" ")
        for p in r:
            name = p.get_name()
            counter = r[p]['C']
            print(f"{name}'s counter is {counter}")
        print(" ")

    def announce_round_winner(self):
        if not self.is_tie:
            r_wl = self.round_wl
            winner = r_wl["W"].get_name()
            print(f"Round winner is {winner}")
        else:
            print("It's a tie")

    def update_round(self):
        r = self.round_wl
        self.rounds[self.round_counter] = {
            "Winner": r["W"],
            "Looser": r["L"],
        }

    def announce_new_round(self):
        print(f"round: {self.round_counter} started")

    def game_over(self):
        R = self.round
        for p in R:
            if p.get_counter() == 0:
                name = p.get_name()
                print(f"Winner of the game is {name}")


# Defining dies
die1 = Die("Die 1")
die2 = Die("Die 2")

# Defining players
p1 = Player(die1, "Tofa")
p2 = Player(die2, "Computer", is_human=False)

# Defining DiceGame
game = DiceGame(p1, p2)

# Game Progression
game.announce_start()

while min(p1.get_counter(), p2.get_counter()) != 0:
    print("=" * 50)
    game.announce_new_round()
    print("Press any key to roll dice")
    msvcrt.getch()
    time.sleep(0.5)
    game.roll_dice()
    game.det_dice_values()
    game.det_round_wl()
    game.print_round_results()
    game.announce_round_winner()
    game.update_round()
    game.increment_round()

game.game_over()
