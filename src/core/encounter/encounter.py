from src.core.encounter.conversation import Conversation


class Encounter():
    def __init__(self, posse_1, posse_2):
        self.posse_1 = posse_1
        self.posse_2 = posse_2

    def next_conversation(self, partner_1, partner_2):
        if ((partner_1 in self.posse_1 and partner_1.health > 0) and
            (partner_2 in self.posse_2 and partner_2.health > 0)):
            return Conversation(partner_1, partner_2)
        else:
            return None


    def get_winner(self):
        if not any(member for member in self.posse_1 if member.health > 0):
            return 1
        elif not any(member for member in self.posse_2 if member.health > 0):
            return 2
        else:
            return 0