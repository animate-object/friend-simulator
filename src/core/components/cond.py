from collections import Collection
from random import choice
from enum import Enum


class Duration(Enum):
    BATTLE=1        # lasts until battle is over
    DEATH=2         # lasts until your health drops to 0
    INDEFINITE=3    # lasts until cured by specific means

class Condition():
    def __init__(
            self, name, duration, affected=None, relieved=None, damage_dealt_mod=None, damage_taken_mod=None, dot=None, hot=None
    ):
        self.name = name
        self.duration = duration
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

    def get_dot(self, health):
        return self._dot * health

    def get_hot(self, health):
        return self._hot * health


FRIENDLY = Condition(
    "Friendly",
    Duration.BATTLE,
    affected=[
        "{subject} is feeling friendly!"
    ],
    relieved=[
        "{subject} is no longer feeling friendly."
    ],
    damage_taken_mod=1.5
)

EMOTIONALLY_UNAVAILABLE = Condition(
    "Emotionally Unavailable",
    Duration.DEATH,
    affected=[
        "{subject} is emotionally unavailable.",
        "{subject} isn't very in touch with {subject_ppn} emotions right now.",
        "{subject} has lost touch with {subject_ppn} emotions."
    ],
    relieved=[
        "{subject} is no longer emotionally unavailable.",
        "{subject} is ready to feel again."
    ],
    damage_taken_mod=0.5
)

ON_FIRE = Condition(
    "On Fire",
    Duration.BATTLE,
    affected=[
        "{subject} is on fire!",
        "{subject} is firing on *all* cylinders."
        "{subject} is hot right now."
    ],
    relieved=[
        "{subject} is cooling down.",
    ],
    damage_dealt_mod=1.5
)

ICE_COLD = Condition(
    "Ice Cold",
    Duration.BATTLE,
    affected=[
        "{subject} is ice cold.",
        "{subject} is a little off {subject_ppn} game right now."
    ],
    relieved=[
        "{subject} is finding {subject_ppn} mojo again."
    ],
    damage_dealt_mod=0.5
)

CONFUSED = Condition(
    "Confused",
    Duration.BATTLE,
    affected=[
        "{subject} is confused.",
        "{subject} is getting mixed signals.",
        "{subject} has no idea what's going on."
    ],
    relieved=[
        "{subject} is no longer confused.",
        "{subject} is back on the level."
    ]
)

BLUE = Condition(
    "Blue",
    Duration.INDEFINITE,
    affected=[
        "{subject} is feeling a little blue.",
    ],
    relieved=[
        "{subject} is no longer blue"
    ],
    hot=.05
)

WOKE = Condition(
    "Woke",
    Duration.INDEFINITE,
    affected=[
        "{subject} is woke.",
        "{subject} opens their eyes."
    ],
    relieved=[
        "{subject} is no longer woke."
    ]
)
