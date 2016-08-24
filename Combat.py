__author__ = 'Steve'


class Combat:
    def __init__(self, u1, u2):
        self.round = 0
        self.unit1 = u1
        self.unit2 = u2

    def ranged_attack(self):
        if self.unit1.ranged:
            self.unit2.defend(self.unit1.attack(), self.unit1.armour_piercing)
        if self.unit2.ranged:
            self.unit1.defend(self.unit2.attack(), self.unit2.armour_piercing)

    def do_round(self):
        self.round += 1
        self.unit1.defend(self.unit2.attack(), self.unit2.armour_piercing)
        self.unit2.defend(self.unit1.attack(), self.unit1.armour_piercing)

    def new_round(self):
        self.round += 1
        self.unit2.wound(self.unit1.new_attack(self.unit2))
        self.unit1.wound(self.unit2.new_attack(self.unit1))

    def is_complete(self):
        complete = False
        if self.unit1.curr_health <= 0 or self.unit2.curr_health <= 0:
            complete = True
        return complete

    def return_winner(self):
        if self.is_complete():
            if self.unit1.curr_health <= 0 and self.unit2.curr_health <= 0:
                return True
            else:
                if self.unit1.curr_health <= 0:
                    return self.unit2
                else:
                    return self.unit1
        else:
            return False