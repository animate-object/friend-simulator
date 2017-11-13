
class Attack():
    def __init__(self, types, base_damage, name, effects=None, cast=None, **kwargs):
        self.types = types
        self.base_damage = base_damage
        self.name = name
        self.cast = list(cast) if cast else ['{} appears to ' + name]
        self.effects = effects if effects else []
        self.__dict__.update(kwargs)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<name={}, base_damage={}, types={}, effects={}>".format(
            self.name, self.base_damage, self.types, self.effects
        )