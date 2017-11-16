from src.core.components.attack import Attack
from src.core.components.char import Character


class Conversation:
    def __init__(self, partner_1: Character, partner_2: Character):
        self.p1 = partner_1
        self.p2 = partner_2
        self.winner = None


    def play_turn(self, p1_move, p2_move):
        turn_events = []
        moves = { self.p1: p1_move, self.p2: p2_move }
        for p in self._get_turn_order():
            o = self.p2 if p is self.p1 else self.p1
            if moves[p] == 'QUIT':
                turn_events.append({'subject': p, 'action': 'QUIT'})
                break

            if isinstance(moves[p], Attack):
                turn_events += (self._attack(p, o, moves[p]))
                if o.health <= 0:
                    self.winner = p
                    turn_events.append({'subject': o, 'action': 'DIES'})
                    break
            # elif isinstance(moves[p], Item)

            # if p.condition and p.condition.has_recurring_effect
            #     turn_events.append(_apply_recurring_condition(p, p.condition))

        return turn_events

    def _get_turn_order(self):
        return sorted([self.p1, self.p2], key=lambda p: p.health)

    def _attack(self, attacker, target, attack):
        damage = self._calculate_damage(attack, attacker, target)
        target.health -= damage
        attacks = {'subject': attacker, 'action': attack, 'object': target}
        takes_damage = {'subject': target, 'action': 'HEALTH_REDUCED', 'new_health': target.health}
        return [attacks, takes_damage]

    def _calculate_damage(self, attack, attacker, target):
        damage = attack.base_damage

        # TODO fix up naive impl to account for conditions
        # if attacker.condition and attacker.condition.modifies_attack:
        #    damage = condition.modify_attack(damage)
        # if target.condition and target.condition.modifies_damage:
        #    damage = condition.modify_damage(damage)

        return damage
