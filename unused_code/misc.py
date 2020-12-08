@property
def leadership(self):
    """Used to determine formations, designated leader gives aura buffs"""
    captain = self.attributes.coordination + self.attributes.charisma
    return captain