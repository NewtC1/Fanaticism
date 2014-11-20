from mob import Mob

class NPC(Mob):
   
   name=''
   
   #init
   def __init__(self, health = 3, name = "Sir Livingston"):
      self.health = health
      self.symbol = 'N'
      self.name=name
   
   def getName(self):
      return self.name
   
   def setName(self, name):
      self.name=name