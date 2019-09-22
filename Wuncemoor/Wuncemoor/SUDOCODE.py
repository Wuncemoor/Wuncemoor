class Party:
	def __init__(self, capacity):
		self.capacity = capacity
		self.crew = []

	def add_party_member(self, mercenary):
		results = []
		if len(self.crew) >= self.capacity:
			results.append({'ally_added': None, 'message': Message('Your party is already full!', libtcod.white)})
            
class Biome:
    def __init__(self, temperature, moisture, elevation):
    
class Personality:
    def __init__(self, brave_craven, avarice_generous, apathy_fervor, uncouth_refined)
        
        