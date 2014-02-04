from mob import Mob

class placeholder(Mob):
	
   symbol = '_'
   health = 1000

   def __init__(self, symbol):
      self.symbol = symbol

   #Shouldn't do anything, makes sure placeholders don't take damage
   def takeDamage(self, damage):
      return 0

   #can't infect the environment
   def addInfection(self, level):
      return 0
   
   def setInfection(self,level):
      return 0