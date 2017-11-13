class Character():
    def __init__(self, name, interests, attacks, health, **kwargs):
        self.name = name
        self.interests = interests
        self.attacks = attacks
        self.health = health
        self.effects = []
        self.__dict__.update(kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<name={}, interests={}, attacks=[{}], health={}>".format(
            self.name, self.interests, ', '.join(str(attack) for attack in self.attacks), self.health
        )