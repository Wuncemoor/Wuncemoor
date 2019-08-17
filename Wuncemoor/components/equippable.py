class Equippable:
	def __init__(self, slot, power_bonus=0, defence_bonus=0, max_hp_bonus=0):
		self.slot = slot
		self.power_bonus = power_bonus
		self.defence_bonus = defence_bonus
		self.max_hp_bonus = max_hp_bonus