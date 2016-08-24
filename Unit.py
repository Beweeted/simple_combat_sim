__author__ = 'Steve'


class Unit:
    def __init__(self, n="Default", ch=1, mh=1, a=0, d=1, sp=1, arp=False, rng=False,
                 dam_type=1, arm_type=1, cr_ch=0.0, cr_dm=1.5, pic=None, atkpic=None, **kwargs):
        self.name = n
        self.curr_health = ch
        self.max_health = mh
        self.armour = a
        self.damage = d
        self.speed = sp
        self.armour_piercing = arp
        self.ranged = rng
        self.damage_type = dam_type
        self.armour_type = arm_type
        self.critical_chance = cr_ch
        self.critical_damage = cr_dm
        self.picture = pic
        self.attack_picture = atkpic

    def wound(self, d=0, **kwargs):
        self.curr_health -= d

    def return_status(self):
        status = "Health: " + str(self.curr_health) + " / " + str(self.max_health) + "\n"
        status += "Damage: " + str(self.damage) + "\n"
        status += "Armour: " + str(self.armour) + "\n"
        status += "Speed: " + str(self.speed)
        return status

    def print_full_unit(self):
        print()
        print(self.name)
        print(self.curr_health)
        print(self.max_health)
        print(self.armour)
        print(self.damage)
        print(self.speed)
        print(self.armour_piercing)
        print(self.ranged)
        print(self.damage_type)
        print(self.armour_type)
        print(self.critical_chance)
        print(self.critical_damage)
        print(self.picture)
