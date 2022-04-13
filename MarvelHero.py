from Hero import Hero

class MarvelHero(Hero):

    def attack(self, enemy, attack_name):
        if type(enemy) == MarvelHero:
            print('Same hero type!!!')
        else:
            super(MarvelHero, self).attack(enemy, attack_name)


