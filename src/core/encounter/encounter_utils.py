from pprint import pprint
from random import choice

from src.core.components.attack import Attack
from src.core.encounter.encounter import Encounter


def format_cast(cast, caster, target):
    try:
        return cast.format(
            caster = getattr(caster,'name', 'Caster'),
            caster_pn = getattr(caster,'pn', 'it'),
            caster_ppn = getattr(caster,'ppn', 'its'),
            caster_opn = getattr(caster,'opn', 'it'),
            target = getattr(target, 'name', 'Target'),
            target_pn = getattr(target,'pn', 'it'),
            target_ppn = getattr(target,'ppn', 'its'),
            target_opn = getattr(target,'opn', 'it')
        )
    except:
        return cast




def text_encounter(posse_1, posse_2):
    encounter = Encounter(posse_1, posse_2)
    conversation = encounter.next_conversation(posse_1[0], posse_2[0])
    while not encounter.get_winner():
        p_1_move = prompt_for_attack(conversation.p1)
        p_2_move = prompt_for_attack(conversation.p2)

        turn_events = conversation.play_turn(p_1_move, p_2_move)

        display_turn(turn_events)

    print(encounter.get_winner())

def display_turn(turn_events):
    for event in turn_events:
        if isinstance(event['action'], Attack):
            print(format_cast(choice(event['action'].cast), event['subject'], event['object']))
        else:
            subject = event.pop('subject')
            print("{} -- {}".format(str(subject), event))

def prompt_for_attack(partner):
    prompt = "Pick {}'s attack!\n".format(str(partner))
    prompt += '\n'.join(['{}. {}'.format(i, attack) for i, attack in enumerate(partner.attacks)])
    while True:
        print(prompt)
        ip = input()
        if ip.isdigit() and int(ip) < len(partner.attacks):
            return partner.attacks[int(ip)]