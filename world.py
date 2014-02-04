from mobs import *

from tile import tile
import copy

class world:
   
   actorList = []    # holds a list of all actors in the world
   
   actorList.append(player.player())
   playerSpawnTile= tile(actorList[0])
   emptyTile= tile(None)
   
   grid = []

   #init
   def __init__(self, size):
      self.buildWorld(size)

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
   def updateWorld(self, time):
      
      for x in range(0, len(self.grid)):
         for y in range(0, len(self.grid[x])):
            if(self.grid[x][y].getHealth()<=0):
               self.grid[x][y]=self.emptyTile #cleans up dead actors at the start of the update
      #for each second in time, check every infected person, and spread the infection
      for seconds in range(0, time):
         newlyInfected=[] #will not spread if in newly infected
         for rows in range(0, len(self.grid)):
            for cols in range(0, len(self.grid[rows])):
               if (self.grid[rows][cols].getActor() is not None):
                  if (self.grid[rows][cols].getActor().getInfection()==9) and (self.grid[rows][cols].getActor() not in newlyInfected):
                     
                     if(rows+1<len(self.grid)): #spread down
                        if(self.grid[rows+1][cols].getInfection()!=9):
                           self.grid[rows+1][cols].addInfection(1)
                           if self.grid[rows+1][cols].getInfection()==9:
                              newlyInfected.append(self.grid[rows+1][cols].getActor())
               
                     if(rows-1>=0):  #spread up
                        if(self.grid[rows-1][cols].getInfection()!=9):
                           self.grid[rows-1][cols].addInfection(1)
                           if self.grid[rows-1][cols].getInfection()==9:
                              newlyInfected.append(self.grid[rows-1][cols].getActor())
                        
                     if(cols+1<len(self.grid[rows])): #spread to the right
                        if(self.grid[rows][cols+1].getInfection()!=9):
                           self.grid[rows][cols+1].addInfection(1)
                           if self.grid[rows][cols+1].getInfection()==9:
                              newlyInfected.append(self.grid[rows][cols+1].getActor())
                              
                     if(cols-1>=0):  #spread to the left
                        if(self.grid[rows][cols-1].getInfection()!=9):
                           self.grid[rows][cols-1].addInfection(1)
                           if self.grid[rows][cols-1].getInfection()==9:
                              newlyInfected.append(self.grid[rows][cols-1].getActor())

         del newlyInfected[:]
   #initializes a world of placeholders
   def buildWorld(self, size):
      for rows in range(0, size):
         self.actorList.append(npc.NPC(3,'Sir Livingston'))
         self.grid.append([tile(self.actorList[len(self.actorList)-1])])
         for cols in range(0, size):
            self.actorList.append(npc.NPC(3, 'Sir Livingston'))
            self.grid[rows].append(tile(self.actorList[len(self.actorList)-1]))
            
   #registers a new actor with the world, and adds it to a tile
   def setActor(self, actor, x, y=0):
      self.actorList.append(actor)
      self.grid[x][y].setActor(actor)
   

#test code
a = world(50)
a.setActor(player.player(), 0 , 0)
generation=0
a.getGrid()[0][0].getActor().infectPriest(a.getGrid()[25][25].getActor())

incrementBy=2
while(generation<200):
   a.updateWorld(incrementBy)
   print a
   generation+=incrementBy