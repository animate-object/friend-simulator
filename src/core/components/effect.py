from random import random, seed


class Effect():
    def __init__(self, name, text, chance=None, custom_function=None):
        seed()
        self.chance = chance
        self.custom_function = custom_function
        self.has_custom = bool(custom_function)

    def does_effect_happen(self, **inputs):
        if self.custom_function:
            return self.custom_function(**inputs)
        return random() < self.chance
