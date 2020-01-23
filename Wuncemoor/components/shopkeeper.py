class ShopKeeper:
    
    def __init__(self, name='shopkeeper', node_power=0, shop_type=None, dialogue=None):
        self.node_power = node_power
        self.shop_type = shop_type
        self.dialogue = dialogue
        self.name = name
        
        
class Dialogue:

    def __init__(self):
        self.conversation = self.conversation()
        
    def conversation(self):
    
        greeting = 'Whats up?'
        
        responses = ['Show me your wares.', 'Not much.']
        
        return responses
        