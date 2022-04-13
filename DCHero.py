from Hero import Hero

class DCHero(Hero):

    def attack(self, enemy, attack_name):
        if type(enemy) == DCHero:
            print('Same hero type!!!')
        else:
            super(DCHero, self).attack(enemy, attack_name)
