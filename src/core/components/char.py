from src.type_chart import STRONG_AGAINST, WEAK_AGAINST


class Character():
    def __init__(self, name, interests, attacks, health, **kwargs):
        self.name = name
        self.interests = interests
        self.attacks = attacks
        self.health = health
        self.effects = {}
        self.__dict__.update(kwargs)
