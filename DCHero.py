from Hero import Hero

class DCHero(Hero):
    def __init__(self, name, attack, life_point, landing_probability):
        super().__init__(name, attack, life_point, landing_probability)
