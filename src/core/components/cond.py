from collections import Collection
from random import choice


class Condition():
    def __init__(
            self, name, affected=None, relieved=None, damage_dealt_mod=None, damage_taken_mod=None, dot=None, hot=None
    ):
        self.name = name
        self._damage_dealt_mod = damage_dealt_mod
        self.modifies_damage_dealt = bool(self._damage_dealt_mod)
        self._damage_taken_mod = damage_taken_mod
        self.modifies_damage_taken = bool(self._damage_taken_mod)
        self._dot = dot
        self.deals_dot = bool(self._dot)
        self._hot = hot
        self.deals_hot = bool(self._hot)
        self.affected = affected if affected else "{subject}" + "is {condition}".format(condition=self.name)
        self.relieved = relieved if relieved else "{subject}" + "is no longer {condition}".format(condition=self.name)

    def affected_msg(self, subject):
        affected_msg = self.affected if not isinstance(self.affected, Collection) else choice(self.affected)
        return affected_msg.format(subject=subject.get('name', str(subject)))

    def relieved_msg(self, subject):
        relieved_msg = self.relieved if not isinstance(self.relieved, Collection) else choice(self.relieved)
        return relieved_msg.format(subject=subject.get('name', str(subject)))

    def transform_damage_dealt(self, damage):
        return damage * self._damage_dealt_mod

    def transform_damage_taken(self, damage):
        return damage * self._damage_taken_mod

    def get_dot(self):
        return self._dot

    def get_hot(self):
        return self._hot

