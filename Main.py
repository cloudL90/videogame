from DCHero import DCHero
from MarvelHero import MarvelHero

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

    print("Choose an attacks!")
    for atk in attacks:
        print("{}".format(atk))
    choose_atk = input()
    print("You choose {}".format(choose_atk))
    """for elem in attacks:
        attack_dict = elem
        if attack_dict["name"] == choose_atk:
            print(attack_dict["power"])"""
    enemy = hero.attack(type(hero), enemy, choose_atk)

    """for atk in attacks:
        print("{}".format(atk))

    choose_atk = input()
    attack = {}
    for attack_dict in attacks:
        if attack_dict["name"] == choose_atk:
            attack = attack_dict
            print(attack['power'])
        else:
            print("non ci siamo")"""







