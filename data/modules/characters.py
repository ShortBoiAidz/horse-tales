import pygame as pg

class Prank:
	def __init__(self):
		self.image = pg.image.load("assets\textures\characters\daniel_prank\idle.png")
		self.x = 0
		self.y = 0

class Rooster:
	def __init__(self):
		self.image = pg.image.load("assets\textures\characters\riley_rooster\idle.png")
		self.x = 0
		self.y = 0

class Smirk:
	def __init__(self):
		self.image = pg.image.load("assets\textures\characters\carleighe_smirk\idle.png")
		self.image_shot = pg.image.load("assets\textures\characters\carleighe_smirk\shot.png")
		self.x = 0
		self.y = 0