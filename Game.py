from Unit import Unit

__author__ = 'Steve'

class Game:
    def __init__(self, first=Unit(), second=Unit()):
        self.first_unit = first
        self.second_unit = second
        self.game_clock = 0

    def tick(self):
        self.game_clock += 1

    def attack(self, attacker=Unit(), defender=Unit()):
        defender.curr_health -= attacker.damage

    def check_for_winner(self):
        fuc, suc = self.first_unit.curr_health, self.second_unit.curr_health
        is_winner = False

        if fuc <= 0 and suc <= 0:
            is_winner = True
        elif fuc <= 0:
            is_winner = True
        elif suc <= 0:
            is_winner = True

        return is_winner