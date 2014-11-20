import copy
from mobs import *
import weakref

class tile:

   actor = None

   #init
   def __init__(self, actor):
      if actor!=None:
         self.actor = weakref.ref(actor)

   def __str__(self):
      if self.actor is not None:
         return self.actor().__str__()
      elif self.actor is None:
         return '_'

   def getActor(self):
      if self.actor is not None:
         return self.actor()
      else:
         return self.actor
   
   def addInfection(self, level):
      if self.actor is not None:
         self.actor().addInfection(level)
         return 1
      else:
         return 0

   def getHealth(self):
      if self.actor is not None:
         return self.actor().getHealth()
   
   def setActor(self, actor):
      if self.actor is not None:
         self.actor = weakref.ref(actor)
   
   def getInfection(self):
      if self.actor is not None:
         return self.actor().getInfection()
      else:
         return 'n'

   def takeDamage(self, damage):
      if self.actor is not None:
         self.actor().takeDamage(damage)
   
   # target is a target tile
   def infectPriest(self, target):
      if self.actor is not None and target is not None:
         if self.actor().getSymbol() == 'P':
            self.actor().infectPriest(target.getActor())

   #simplifies the attack order
   def attack(self, target):
      if (hasattr(target, "actor")):
         target.takeDamage(self.actor().getDamage())