__author__ = 'Steve'

class TextDisplay:
    @staticmethod
    def print_full_unit(unit):
        print()
        print("Name: ", unit.name)
        print("Health: ", unit.curr_health, "/", unit.max_health)
        print("Armour: ", unit.armour)
        print("Damage: ", unit.damage)
        print("Attack Speed: ", unit.attack_speed)
        print()

    @staticmethod
    def print_unit_status(unit):
        print(unit.name + ": ", end='')
        print(unit.curr_health, "/", unit.max_health)

    @classmethod
    def print_combat_status(cls, combat):
        print("Current round: ", combat.round)
        cls.print_unit_status(combat.unit1)
        cls.print_unit_status(combat.unit2)
        print()

    @staticmethod
    def print_combat_winner(combat):
        winner = combat.return_winner()
        if isinstance(winner, bool):
            if winner:
                print("We have a draw!  Both units died.")
            else:
                print("Unexpected state: combat is not completed yet.")
        else:
            print(winner.name, "is the winner!")

