from __future__ import  annotations
import random

class Hero:

    def __init__(self, name, attacks, life_point, landing_probability):
        self.name = name
        self.attacks = attacks
        self.life_point = life_point
        self.landing_probability = landing_probability

    def attack(self, enemy: Hero, attack_name):
        random_probability = self.landing_probability
        # print(random_probability)
        if random_probability > 50:
            attack = {}
            attack_ok = False
            for attack_dict in self.attacks:
                print(attack_dict)
                if attack_dict["name"] == attack_name:
                    attack = attack_dict
                    enemy.life_point -= attack['power'] * random.random()
                    attack_ok = True
                    print("%s life point decreased at %i" % (enemy.name, enemy.life_point))
                    return attack_ok
        else:
            print("Attack Failed!")
            return enemy