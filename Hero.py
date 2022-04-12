import random
class Hero:

    def __init__(self, name, attack, life_point, landing_probability):
        self.name = name
        self.attacks = attack
        self.life_point = life_point
        self.landing_probability = landing_probability

    def attack(self, hero_type, enemy, attack_name):
        if self.check_attack(hero_type, enemy):
            random_probability = self.landing_probability
            # print(random_probability)
            if random_probability > 50:
                attack = {}
                for attack_dict in self.attacks:
                    if attack_dict["name"] == attack_name:
                        attack = attack_dict
                        enemy.life_point -= attack['power'] * random.random()
                        print("Enemy Lifepoints {}".format(enemy.life_point))
                        return enemy
                    else:
                        return
            else:
                print("Attack Failed!")
                return enemy
        else:
            print('Same hero type!!!')
            return enemy

    def check_attack(self, hero_type, enemy ):
        return hero_type != type(enemy)

    """def get_Life_Point(self, enemy, attack):
        enemy.life_point -= attack.power * random.random()
        return enemy.life_point"""
