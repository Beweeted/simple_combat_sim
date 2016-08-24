#  General functionality
import copy
import time

import threading

#  GUI libraries
import tkinter as tk

#  Background Classes
from Unit import Unit
from Game import Game

class UnitFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.pack_propagate(False)
        self.configure(width="150", height="250")

        #  display the selected units
        self.display_name = tk.Label(self)
        self.display_img = tk.Label(self)
        self.display_lbl = tk.Label(self)

        self.display_name.pack(side="top")
        self.display_img.pack(side="top")
        self.display_lbl.pack(side="top")

        self.pic1 = tk.PhotoImage()
        self.pic2 = tk.PhotoImage()

    def display(self, unit=Unit()):
        self.pic1 = unit.picture
        self.pic2 = unit.attack_picture

        self.display_name.configure(text=unit.name)
        self.display_img.configure(image=self.pic1)
        self.display_lbl.configure(text=unit.return_status())

    def animate_attack(self):
        for t in range(2):
            self.display_img.configure(image=self.pic2)
            time.sleep(0.1)
            self.display_img.configure(image=self.pic1)
            time.sleep(0.1)


class Application2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.top_frame, self.bottom_frame = tk.Frame(), tk.Frame()
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="bottom")

        self.army_choice_frame = tk.Frame(self.bottom_frame)
        self.army_choice_frame.pack(side="bottom")
        self.left_unit = UnitFrame(self.top_frame)
        self.right_unit = UnitFrame(self.top_frame)
        self.left_unit.pack(side="left")
        self.right_unit.pack(side="right")

        self.menu_frame = tk.Frame(self.top_frame)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.configure(width="130", height="170")
        self.menu_frame.pack(side="bottom")

        # initialize_units
        self.serf = Unit(n="Serf", ch=354, mh=354, d=61, sp=8,
                         pic=tk.PhotoImage(file="unit_images/serf.png"),
                         atkpic=tk.PhotoImage(file="unit_images/serf_atk.png"))
        self.archer = Unit(n="Archer", ch=171, mh=171, d=107, sp=9, rng=True,
                           pic=tk.PhotoImage(file="unit_images/archer.png"),
                           atkpic=tk.PhotoImage(file="unit_images/archer_atk.png"))
        self.knight = Unit(n="Knight", ch=360, mh=360, a=29, d=136, sp=8,
                           pic=tk.PhotoImage(file="unit_images/knight.png"),
                           atkpic=tk.PhotoImage(file="unit_images/knight_atk.png"))
        self.sentry = Unit(n="Sentry", ch=225, mh=225, a=16, d=152, sp=8, arp=True,
                           pic=tk.PhotoImage(file="unit_images/sentry.png"),
                           atkpic=tk.PhotoImage(file="unit_images/sentry_atk.png"))
        self.soldier = Unit(n="Soldier", ch=398, mh=398, a=35, d=106, sp=7,
                            pic=tk.PhotoImage(file="unit_images/soldier.png"),
                            atkpic=tk.PhotoImage(file="unit_images/soldier_atk.png"))

        self.army_choices = [self.serf, self.archer, self.knight, self.sentry, self.soldier,]
        self.active_unit = self.serf
        self.first_unit, self.second_unit = Unit(), Unit()

        self.unit_buttons = [tk.Button(self.army_choice_frame, image=u.picture,
                                       compound="bottom", text=u.name, bg="#CCCCCC",
                                       command=lambda u=u: self.select_unit(u)) for u in self.army_choices]
        for button in self.unit_buttons:
            button.pack(side="left")

        #  menu buttons
        self.confirm_button = tk.Button(self.menu_frame, text="Select Unit", command=self.confirm_unit)
        self.fight_button = tk.Button(self.menu_frame, text="Fight!", state="disabled", command=self.fight_units)
        self.quit_button = tk.Button(self.menu_frame, text="QUIT", fg="red", command=root.destroy)
        self.confirm_button.pack()
        self.fight_button.pack()
        self.quit_button.pack(side="bottom")

    def select_unit(self, unit):
        self.active_unit = unit

        for b in self.unit_buttons:
            if b.cget("text") == unit.name:
                b.configure(bg="green")
            else:
                b.configure(bg="#CCCCCC")

    def confirm_unit(self):
        if self.first_unit.name == Unit().name:
            self.first_unit = copy.deepcopy(self.active_unit)
            self.first_unit.name = "Garret the " + self.first_unit.name
            self.left_unit.display(self.first_unit)
        else:
            self.second_unit = copy.deepcopy(self.active_unit)
            self.second_unit.name = "Rosa the " + self.second_unit.name
            self.right_unit.display(self.second_unit)

            self.confirm_button.configure(state="disabled")
            self.fight_button.configure(state="active")
            for b in self.unit_buttons:
                b.configure(state="disabled")

    def fight_units(self):
        self.fight_button.configure(state="disable")
        game = Game(first=copy.deepcopy(self.first_unit), second=copy.deepcopy(self.second_unit))

        def callback():
            while True:
                game.tick()
                self.attack(game)
                self.left_unit.display(game.first_unit)
                self.right_unit.display(game.second_unit)
                if game.check_for_winner():
                    print("Winner!")
                    break
                time.sleep(0.7)

        t = threading.Thread(target=callback)
        t.start()

    def attack(self, game=Game()):
        attacked = False
        if game.first_unit.speed % game.game_clock == 0:
            game.attack(attacker=game.first_unit, defender=game.second_unit)
            self.left_unit.animate_attack()
            print("First unit attacked!")
            attacked = True
        if game.second_unit.speed % game.game_clock == 0:
            game.attack(attacker=game.second_unit, defender=game.first_unit)
            self.right_unit.animate_attack()
            print("Second unit attacked!")
            attacked = True
        if attacked:
            print("First unit health:", game.first_unit.curr_health)
            print("Second unit health:", game.second_unit.curr_health)





root = tk.Tk()
app = Application2(master=root)
app.mainloop()

