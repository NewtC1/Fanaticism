import copy
import Tkinter
import sys
import random

from random import randint
from mobs import *
from tile import tile

class world:
   
   actorList = []    # holds a list of all actors in the world
   
   actorList.append(player.player())
   emptyTile= tile(None)

   playerX = 0
   playerY = 0
   
   grid = []

   #init
   def __init__(self, size, playerX = 0, playerY = 0):
      self.buildWorld(size)
      print self.actorList[0]
      self.setActor(self.actorList[0], playerX, playerY)
      self.playerX = playerX
      self.playerY = playerY

   #returns the grid
   def getGrid(self):
      return self.grid
   
   #returns the array in a readable manner
   def __str__(self):
      
      debug=False
      
      self.updateWorld(0)
      
      string=""
      
      if(debug==False):
         for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[x])):
               string += self.grid[x][y].__str__()
            string +="\n"
      
      if(debug==True):
         for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid[x])):
               string += str(self.grid[x][y].getInfection())
            string+="\n"
         
      return string

   # allows the world to update by the amount of time given
   # Should also be called to update how many are dead
   # Will update the spread of the disease once per time
   # also updates movements
   def updateWorld(self, time = 0):
      
      for x in range(0, len(self.grid)):
         for y in range(0, len(self.grid[x])):
            if(self.grid[x][y].getHealth()<=0):
               self.grid[x][y]=self.emptyTile #cleans up dead actors at the start of the update

      #makes the npcs wander around, allows for different controls for each type
      def npcIdle(self):

         # walk through every NPC in the list and move it randomly 
         for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
               direction=random.randint(1,5)
               
               # move NPCs that have been infected
               if (self.grid[row][col].symbol == 'n'):
                  
                  if (direction==1):   #Go north
                     if (self.grid[row-1][col].getActor() is None):
                        self.setActor(self.grid[row][col], row-1, col)
                  if (direction==2): #Go west
                     if (self.grid[row][col+1].getActor() is None):
                        self.setActor(self.grid[row][col], row, col+1)
                  if (direction==3): #Go north
                     if (self.grid[row+1][col].getActor() is None):
                        self.setActor(self.grid[row][col], row+1, col)
                  if (direction==4): #Go east
                     if (self.grid[row][col-1].getActor() is None):
                        self.setActor(self.grid[row][col], row, col-1)
               

      #for each second in time, check every infected person, and spread the infection
      def updateInfection(time):
         for seconds in range(0, time):
            newlyInfected=[] #will not spread if in newly infected
            for rows in range(0, len(self.grid)):
               for cols in range(0, len(self.grid[rows])):
                  if (self.grid[rows][cols].getActor() is not None):
                     if (self.grid[rows][cols].getActor().getInfection()==9) and (self.grid[rows][cols].getActor() not in newlyInfected):
                        
                        if(rows+1<len(self.grid)): #spread down
                           if(self.grid[rows+1][cols].getInfection()!=9): # makes sure the infection isn't max
                              self.grid[rows+1][cols].addInfection(1)
                              if self.grid[rows+1][cols].getInfection()==9: # if it is max, don't do anything. Make sure it isn't updated again
                                 newlyInfected.append(self.grid[rows+1][cols].getActor())
                  
                        if(rows - 1 >= 0):  #spread up
                           if(self.grid[rows - 1][cols].getInfection() != 9):
                              self.grid[rows - 1][cols].addInfection(1)
                              if self.grid[rows-1][cols].getInfection() == 9:
                                 newlyInfected.append(self.grid[rows - 1][cols].getActor())
                           
                        if(cols + 1 < len(self.grid[rows])): #spread to the right
                           if(self.grid[rows][cols + 1].getInfection() != 9):
                              self.grid[rows][cols + 1].addInfection(1)
                              if self.grid[rows][cols + 1].getInfection() == 9:
                                 newlyInfected.append(self.grid[rows][cols+1].getActor())
                                 
                        if(cols-1>=0):  #spread to the left
                           if(self.grid[rows][cols-1].getInfection() != 9):
                              self.grid[rows][cols-1].addInfection(1)
                              if self.grid[rows][cols-1].getInfection() == 9:
                                 newlyInfected.append(self.grid[rows][cols - 1].getActor())

            del newlyInfected[:]

      updateInfection(time)

   #initializes a world, places NPCs at random in it
   def buildWorld(self, size):
      for rows in range(size):


         #create a new row 
         self.grid.append([])

         for cols in range(size):

            if random.randint(0,1) == 1:
              #add to the row
               self.grid[rows].append(tile(None))
            else:
               self.actorList.append(npc.NPC())
               self.grid[rows].append(tile(self.actorList[-1]))
            
   #registers a new actor with the world, and adds it to a tile
   def setActor(self, actor, x, y):
      if x < len(self.grid) and y <= len(self.grid):
         #make sure we're not adding a duplicate (causes movement)
         if actor not in self.actorList:
            self.actorList.append(actor)
         # if the actor being set is in the list, it is assumed to be moving. Remove the old pointer
         else:
            self.grid[actor.x][actor.y] = tile(None) # delete the Ronald Reagan

         self.grid[x][y] = tile(actor)
         actor.x = x
         actor.y = y

   #movement methods
   def playerDown(self):
      if (self.grid[self.playerX+1][self.playerY].getActor() is None):
         self.setActor(self.actorList[0], self.playerX+1, self.playerY)
         self.playerX+=1

   def playerLeft(self):
      if (self.grid[self.playerX][self.playerY-1].getActor() is None):
         self.setActor(self.actorList[0], self.playerX, self.playerY-1)
         self.playerY-=1

   def playerRight(self):
      if (self.grid[self.playerX][self.playerY+1].getActor() is None):
         self.setActor(self.actorList[0], self.playerX, self.playerY+1)
         self.playerY+=1

   def playerUp(self):
      if (self.grid[self.playerX-1][self.playerY].getActor() is None):
         self.setActor(self.actorList[0], self.playerX-1, self.playerY)
         self.playerX-=1

#test code

a = world(26, playerX=0, playerY=0)
generation = 0

a.updateWorld()

a.setActor(npc.NPC(), 0, 1)

print a
a.getGrid()[0][0].infectPriest(a.getGrid()[0][1])
print a

generation = 0
generationCount = 1
while (generation < 100):
   generation += generationCount
   a.updateWorld(generationCount)
   print a