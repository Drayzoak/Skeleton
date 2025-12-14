
import random
from turtle import width 

from PIL import Image
from Scripts.Utilities import utilities
from os.path import join
from memory_profiler import profile
from Scripts.Utilities.Maths import Booltile
from Scripts.World import tile
from Scripts.World.tile import Tile

class WFC():
	#@profile
	def __init__(self, height, width, seed):
		self.height = height
		self.width = width

		self.tiles = tile.settile();
		
		self.All = []
		for x in self.tiles.keys():
			self.All.append(x)
			

		grid = []
		for y in range(height):
			row = []
			for x in range(width):
				row.append("All")
			grid.append(row)
		
		self.worldtile = grid
		self.collapsedtile = []

		self.neighbourtile = []
		
		self.childneighbour = []
		self.noncollapsedtile = []
		self.leastposstiles = []
		self.leastposs = 12

				

		self.collapsedtilebool = Booltile(width,height,False)
		self.neighbourtilebool = Booltile(width,height,False)
		
		for y in range(height):
			for x in range(width):
				self.noncollapsedtile.append((x,y))	

		self.tilestype = dict()
		
		self.iscoll = None
		
		del grid
		random.seed(seed)
	#@profile
	def Start(self):
		print("_______________________________________________________________________________")
		print("Tiles :" )
		for x in self.tiles:
			print("\t", x , " : ", self.tiles[x].image)
			print("\t\t", self.tiles[x])
			for y in self.tiles[x].rules:
				print("\t\t", y , self.tiles[x].rules[y])
		
		
		print("_______________________________________________________________________________")
		print("Collapsed Tiles : ",self.collapsedtile)
		print("Collapsed Tiles Count : ", len(self.collapsedtile))
		print("_______________________________________________________________________________")
		print("Neighbourtile Tiles : ",sorted(self.neighbourtile, key=lambda x: (x[0], x[1])))
		print("\nNeighbourtile Tiles Count:",len(self.neighbourtile))
		print("_______________________________________________________________________________")
		print("Least Posibilities Tiles : ",self.leastposstiles)
		print("\nLeast Posibilities Count:",self.leastposs)
		print("_______________________________________________________________________________")
		print("World Tiles :")
		for x in self.worldtile:
			print(x)
		print("\nWorldTile Count", len(self.worldtile))

		for x in self.tilestype.keys():
			print(self.tilestype[x])
		"""
		print("\n Size Of Worldtile : ",utilities.get_size(self.worldtile)/1024,"MB")
		print("\n Size Of tiles : ",utilities.get_size(self.tiles)/1024, "MB")
		print("\n Size Of tile : ",utilities.get_size(self.tiles[14])/1024, "MB")
		print("_______________________________________________________________________________")
		"""
		self.collapsedtilebool.show()

#region GenerateWorld
	#@profile
	def genWorld(self):
		
		#for y in range(8100):
		while len(self.noncollapsedtile) != 0:
			print(len(self.collapsedtile))
			if self.iscoll == None :
				if len(self.leastposstiles) == 0 and len(self.neighbourtile) == 0:
					self.iscoll = utilities.getranGrid(self.noncollapsedtile)
					#print("selected 1", self.iscoll)
					if self.iscoll not in self.neighbourtile:
						self.neighbourtile.append(self.iscoll)
					self.Collapse()

				elif len(self.leastposstiles) > 0:
					#print("selected 2", self.iscoll)
					self.iscoll = random.choice(self.leastposstiles)
					self.leastposstiles.remove(self.iscoll)
					self.Collapse()
					
					
				elif len(self.neighbourtile) != 0:
					self.leastposs = 40
					#print("selected 3", self.iscoll)
					#print(self.childneighbour)
					for x in self.neighbourtile:
						if type(self.worldtile[x[0]][x[1]]) is list:
							if len(self.worldtile[x[0]][x[1]]) < self.leastposs and len(self.worldtile[x[0]][x[1]]) != 0:
								self.leastposs = len(self.worldtile[x[0]][x[1]])
								self.leastposstiles.append( x)
							elif len(self.worldtile[x[0]][x[1]])==self.leastposs:
								self.leastposstiles.append(x)
					continue

			for z in self.childneighbour:
				#print("\niteration in neighbourtile",z)
				
				k = self.setrule(z)
				
				#print(k)

				if k is False:
					for l in self.getnei(z,False):
						if l not in self.childneighbour :
							self.childneighbour.append(l)

			for x in self.childneighbour:
				if x not in self.neighbourtile and self.worldtile[x[0]][x[1]] != "All":
					self.neighbourtile.append(x)
			self.iscoll = None


	def Collapse(self):
		
		if self.worldtile[self.iscoll[0]][self.iscoll[1]] == str('All'):
			
			self.worldtile[self.iscoll[0]][self.iscoll[1]] = random.choice(list(self.tiles.values()))
		
		elif type(self.worldtile[self.iscoll[0]][self.iscoll[1]]) is not Tile and  self.worldtile[self.iscoll[0]][self.iscoll[1]] !=[]:
			
			choice = random.choice(self.worldtile[self.iscoll[0]][self.iscoll[1]])
			self.worldtile[self.iscoll[0]][self.iscoll[1]] = self.tiles[choice]

		self.collapsedtile.append(self.iscoll)
		if self.iscoll in self.noncollapsedtile:
			self.noncollapsedtile.remove(self.iscoll)

		self.neighbourtile.remove(self.iscoll)
		self.childneighbour = self.getnei(self.iscoll,False)
		#print(self.iscoll)
		#print(self.childneighbour)
		self.iscoll = None


	def getnei(self,pos,collapesed):
		x = pos[0]
		y = pos[1]
		
		pn = [(x-1, y ), (x+1, y), (x, y-1), (x, y+1)]

		if collapesed is False:
			for t in reversed(pn):
				if t[0] < 0 or t[1] < 0 or t[0] >= self.height or t[1] >= self.width or type(self.worldtile[t[0]][t[1]]) is Tile:
					pn.remove(t)
		
		elif collapesed is True:
			for t in reversed(pn):
				if t[0] < 0 or t[1] < 0 or t[0] >= self.height or t[1] >= self.width or type(self.worldtile[t[0]][t[1]]) is not Tile:
					pn.remove(t)
				
		return pn

	def getneia(self,pos):
		x = pos[0]
		y = pos[1]
		
		pn = [(x-1, y ), (x-1, y-1 ), (x+1, y-1 ), (x+1, y), (x+1, y-1), (x+1, y+1), (x, y-1), (x, y+1)]

		for t in reversed(pn):
			if t[0] < 0 or t[1] < 0 or t[0] >= self.height or t[1] >= self.width:
				pn.remove(t)
				
		return pn

	def setrule(self , y):
		tempn = self.getnei(y, True)
		tempr =[]
		boo = False
		if len(tempn) > 0:
			
			for x in tempn:
				tempr = utilities.intersect(tempr, self.getCollapsedRule(y,x))
			#if self.worldtile[y[0]][y[1]] != "All":
			#	tempr = utilities.intersect(tempr,self.worldtile[y[0]][y[1]])

			tempn = self.getnei(y, False)
			
			tempr1 = []
			for x in tempn:
				tempr1 = utilities.intersect(tempr1, self.getNeighbourRule(y,x))
			
			tempr = utilities.intersect(tempr1, tempr)

			self.worldtile[y[0]][y[1]] = tempr

			length = len(tempr)
			
			
			if length >= 30:
				tempr = "All"
				boo = True

			elif length == 0:
				boo = True

				recre = self.getneia(y)
				
				for x in recre:
					if x not in self.neighbourtile:
						self.neighbourtile.append(x)
						
					self.worldtile[x[0]][x[1]] = self.All
				for x in recre:
					self.setrule(x)

			elif self.worldtile[y[0]][y[1]] != tempr:
				self.worldtile[y[0]][y[1]] = tempr
			elif self.worldtile[y[0]][y[1]] == tempr:
				boo = True
			self.worldtile[y[0]][y[1]] = tempr
			

			if length < self.leastposs and length >0:
				self.leastposstiles = []
				self.leastposstiles.append(y)
				self.leastposs =length
			elif length == self.leastposs:
				if y not in self.leastposstiles:
					self.leastposstiles.append(y)
			
			return boo
		
		else: 
			tempn = self.getnei(y, False)
			
			for x in tempn:
				if self.worldtile[x[0]][x[1]] == "All":
					continue
				tempr = utilities.union(tempr,self.getNeighbourRule(y,x))

			#if self.worldtile[y[0]][y[1]] != "All":
			#	tempr = utilities.intersect(tempr,self.worldtile[y[0]][y[1]])
			
			length = len(tempr)
			if length >= 30:
				tempr = "All"
				boo = True
			elif length == 0:
				boo = True
			elif self.worldtile[y[0]][y[1]] != tempr:
				self.worldtile[y[0]][y[1]] = tempr
				boo = True


			if length < self.leastposs and length >0:
				self.leastposstiles = []
				self.leastposstiles.append(y)
				self.leastposs =length
			elif length == self.leastposs:
				if y not in self.leastposstiles:
					self.leastposstiles.append(y)
			
			return boo


	def getCollapsedRule(self, x, y):
		z = (x[0]- y[0], x[1] - y[1])
		if z == (0, -1):
			return self.worldtile[y[0]][y[1]].rules["Lf"]
				
		elif z == ( -1 , 0):
			return self.worldtile[y[0]][y[1]].rules["Up"]
				
		elif z == ( 0 , 1):
			return self.worldtile[y[0]][y[1]].rules["Rt"]
				
		elif z == ( 1 , 0):
			return self.worldtile[y[0]][y[1]].rules["Dn"]
		
		return []

	
	def getNeighbourRule(self, x, y):
		z = (x[0]- y[0], x[1] - y[1])
		tem = []
		
		if z == (0, -1):
			if self.worldtile[y[0]][y[1]] == "All":
				return self.All
			else:
				for x in self.worldtile[y[0]][y[1]]:
					tem = utilities.union(tem,self.tiles[x].rules["Lf"])
				return tem
		
		elif z == ( -1 , 0):
			if self.worldtile[y[0]][y[1]] == "All":
				return self.All
			else:
				for x in self.worldtile[y[0]][y[1]]:
					tem = utilities.union(tem,self.tiles[x].rules["Up"])
				return tem
				
		elif z == ( 0 , 1):
			if self.worldtile[y[0]][y[1]] == "All":
				return self.All
			else:
				for x in self.worldtile[y[0]][y[1]]:
					tem = utilities.union(tem,self.tiles[x].rules["Rt"])
				return tem
				
		elif z == ( 1 , 0):
			if self.worldtile[y[0]][y[1]] == "All":
				return self.All
			else:
				for x in self.worldtile[y[0]][y[1]]:
					tem = utilities.union(tem,self.tiles[x].rules["Dn"])
				return tem
		
		return []

	def getWorld(self):
		resW = 64 * self.width
		resH = 64 * self.height
		
		print(resW, resH)

		img = Image.new("RGBA", (resW, resH), (0,0,0,255))
		imaged = dict()
		for x in self.tiles:
			imaged[self.tiles[x].image] = loadimage(self.tiles[x].image)

		y = 0
		for row in self.worldtile:
			x = 0
			for tl in row:
				if type(tl) is Tile:

					img.paste(imaged[tl.image],(x,y))
				x += 64
			y += 64


		img.save(join("Assets","Map","gen.png"))
#endregion GenerateWorld

	def genfoliage(self):
		self.settilestype()
		
		for x in self.tilestype.keys():
			random.shuffle(self.tilestype[x])

	def settilestype(self):
		for x in range(9):
			self.tilestype[x] = [] 
		for y,j in enumerate(self.worldtile):
			for x,i in enumerate(j):
				if i.tiletype == 1:
					self.tilestype[1].append((x*64,y*64))
				elif i.tiletype == 2:
					self.tilestype[2].append((x*64,y*64))
				elif i.tiletype == 3:
					self.tilestype[3].append((x*64,y*64))

def loadimage(name):
	image = Image.open(join("Assets","SpriteSheet" ,"TileMap",name))
	return image
