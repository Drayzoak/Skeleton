import pygame

from os.path import join

from Scripts.World.WorldGenerator import WFC

class World():
	def __init__(self, worldsize):
		
		self.treecount = 60
		self.grasscount = 120
		self.worldsize = worldsize
		self.gen = WFC(self.worldsize,self.worldsize, 8391094)


	def Start(self,SIZE):
		
		self.gen.genWorld()
		self.gen.genfoliage()
		self.gen.getWorld()

		self.gen.Start()
		
		self.Size = SIZE

		self.image = pygame.image.load(join("Assets","Map" ,"gen.png")).convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.worldsize*64*SIZE,self.worldsize*64*SIZE))
		
		self.grass = pygame.image.load(join("Assets","SpriteSheet","Foliage","grass","01.png")).convert_alpha()
		self.grass = pygame.transform.scale(self.grass, (32*SIZE,32*SIZE))
		
		self.grasstile = self.gen.tilestype[3][:self.grasscount]
		self.grasstile = sorted(self.grasstile, key=lambda x: (x[0], x[1]))

		self.Tree = pygame.image.load(join("Assets","SpriteSheet","Foliage","grass","Tree_01.png")).convert_alpha()
		self.Tree = pygame.transform.scale(self.Tree, (128*SIZE,320*SIZE))

		self.Treetile = self.gen.tilestype[1][:self.treecount]
		self.Treetile = sorted(self.Treetile, key=lambda x: (x[0], x[1]))

		
	
	def Update(self,window,pos):
		
		window.blit(self.image,pos)
		
		for x in self.grasstile:
			window.blit(self.grass,((x[0]*self.Size + pos[0]),(x[1]*self.Size + pos[1])))

		for x in self.Treetile:
			window.blit(self.Tree,((x[0]*self.Size + pos[0] - 0 *self.Size),(x[1]*self.Size + pos[1]- 256 * self.Size)))