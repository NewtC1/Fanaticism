class Mob:

   name = "Blah"
   damage = 3	#Damage per hit
   health = 3 	#Health of the mob
   infection = 0	#Infection level, from 1-10
   symbol = ':'	#Symbol displayed on string
   #infectedThisUpdate=0
   
   def __init(self, health=3):
      self.health = health
   
   def __str__(self):
      return self.symbol
   
   def getHealth(self):
      return self.health
   
   def getSymbol(self):
      return self.symbol
   
   def setSymbol(self, symbol):
      self.symbol=symbol

   def getInfection(self):
      return self.infection

   #used in standard infection, does not make fanatics
   def addInfection(self, level):
      if self.infection<9:
         self.infection+=level
         #after the update, check if priest is ready, and prep for disease spread
         if (self.infection>=9):
            self.infection=9
            self.setSymbol(self.getSymbol().lower())

   def setInfection(self, level):
      self.infection=level

   def getDamage(self):
      return self.damage

   def getName(self):
      return self.name

      #subtracts the damage from health.
   def takeDamage(self, damage):
      self.health-=damage

      #this mob attacks the target. Deals damage to health
   def attack(self, target):
         
      if (hasattr(target, "health")):
         target.takeDamage(self.damage)
         print target.getName() + " takes " + str(self.damage) +" damage."