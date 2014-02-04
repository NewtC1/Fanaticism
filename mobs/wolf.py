from mob import Mob

class Wolf(Mob):

   def __init__(self, health=6, symbol='W'):
      self.health=health
      self.symbol=symbol