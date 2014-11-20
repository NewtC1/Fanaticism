from mob import Mob

class player(Mob):

   def __init__(self, symbol = 'P', health = 20, damage = 3):
      self.symbol=symbol
      self.health=health
      self.damage=damage

   #set infection level to maximum, turning them into crusadors
   def infectFanatic(self, target):
      if (hasattr(target,"health")):
         target.setInfection(10)

   #set infection to one below. Pulse will bring it up by 1
   def infectPriest(self, target):
      if (hasattr(target, "health")):
         target.setSymbol(target.getSymbol().lower())
         target.setInfection(9)

   #redefined in world, applies this effect to all targets
   def pulse(self, target):
      if (hasattr(target, "health"))and(target.getInfection()==9):
         target.setInfection(10)
   
   def addInfection(self, amount):
      return 0