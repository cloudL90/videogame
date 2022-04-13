from __future__ import  annotations
import random

class Hero:

    def __init__(self, name, attacks, life_point, landing_probability):
        self.name = name
        self.attacks = attacks
        self.life_point = life_point
        self.landing_probability = landing_probability

    factors = ["Snowing", "Mal di pancia", "Indigestione di cozze"]

    def attack(self, enemy: Hero, attack_name):
        random_probability = self.landing_probability
        # print(random_probability)
        if random_probability * random.random() > 50 :
            attack = {}
            attack_ok = False
            for attack_dict in self.attacks:
                print(attack_dict)
                if attack_dict["name"] == attack_name:
                    attack = attack_dict['power'] * random.random()
                    print("%s ha abbassato l'attacco di %s a %i" % (Hero.factor(self.factors), enemy.name, attack))
                    enemy.life_point -= attack
                    attack_ok = True
                    if enemy.life_point < 0:
                        print("%s id dead!" % (enemy.name))
                    else:
                        print("%s life point decreased at %i" % (enemy.name, enemy.life_point))
                    return attack_ok
        else:
            print("Attack Failed!")
            return enemy

    def factor(factors):
        casuality = factors[random.randint(0, 2)]
        return casuality

    # print(factor(factors))