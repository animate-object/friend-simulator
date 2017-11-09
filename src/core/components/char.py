from src.type_chart import STRONG_AGAINST, WEAK_AGAINST


class Character():
    def __init__(self, name, interests, attacks, health, **kwargs):
        self.name = name
        self.interests = interests
        self.attacks = attacks
        self.health = health
        self.effects = {}
        self.__dict__.update(kwargs)

    def attack(self, o, attack):
        o.take_damage(attack)

    def take_damage(self, attack):
        multiplier = 1
        for t in attack.types:
            for i in self.interests:
                if t in STRONG_AGAINST[i]:
                    multiplier *= 2.0
                if t in WEAK_AGAINST[i]:
                    multiplier *= 0.5
        self.health -= attack.base_damage * multiplier
