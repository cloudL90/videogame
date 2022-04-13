from DCHero import DCHero
from MarvelHero import MarvelHero
from termcolor import colored
from random import randint
import time

if __name__ == '__main__':

    attacks = [
        {'name': 'web',
         'power': 5},
        {'name': 'puch',
         'power': 8},
        {'name': 'kick',
         'power': 10},
    ]

    captain_america = DCHero("Captain America", attacks, 40, 100) # DC
    batman = DCHero("Batman", attacks, 40, 100) # DC
    iron_man = MarvelHero("Ironman", attacks, 40, 100) # Marvel
    spiderman = MarvelHero("Spiderman", attacks, 40, 100) # Marvel

    heroes_list = [captain_america, batman, iron_man, spiderman]
    heroes_name_list = [captain_america.name, batman.name, iron_man.name, spiderman.name]

    print("Choose an heroes!")
    for her in heroes_list:
        print("Name: {}".format(her.name))
    heroes = input()
    if heroes in heroes_name_list:
        print("Hai scelto ", heroes)
        index = heroes_name_list.index(heroes)
        heroes_name_list.pop(index)
        hero = heroes_list[index]
        heroes_list.pop(index)
    for her in heroes_list:
        print("Name: {}".format(her.name))
    print("Now choose an enemy")
    enemy = input()
    if enemy in heroes_name_list:
        print("Your enemy is:", enemy)
        index = heroes_name_list.index(enemy)
        heroes_name_list.pop(index)
        enemy = heroes_list[index]
        heroes_list.pop(index)

    while enemy.life_point > 0 and hero.life_point > 0:
            random_attack = attacks[randint(0, 2)]['name']
            # print("Choose an attack!")
            for atk in attacks:
                print("{}".format(atk))
            # hero_atk = input()
            print("%s attack with %s" % (hero.name, random_attack))
            hero.attack(enemy, random_attack)
            hero, enemy = enemy, hero
            time.sleep(1.5)

    # print(attacks[randint(0, 2)]['name'])

