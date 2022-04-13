from DCHero import DCHero
from MarvelHero import MarvelHero
from termcolor import colored

if __name__ == '__main__':

    attacks = [
        {'name': 'web',
         'power': 5},
        {'name': 'puch',
         'power': 8},
        {'name': 'kick',
         'power': 10},
    ]

    captain_america = DCHero("Captain America", attacks, 30, 100) # DC
    batman = DCHero("Batman", attacks, 40, 155) # DC
    iron_man = MarvelHero("Ironman", attacks, 30, 80) # Marvel
    spiderman = MarvelHero("Spiderman", attacks, 30, 60) # Marvel

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
            print("Choose an attack!")
            for atk in attacks:
                print("{}".format(atk))
            hero_atk = input()
            print("%s attack with %s" % (heroes, hero_atk))
            hero.attack(enemy, hero_atk)
            hero, enemy = enemy, hero

