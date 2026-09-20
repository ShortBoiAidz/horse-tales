import pygame as pg

class BlueCoin:
	def __init__(self):
		self.image = pg.image.load("assets/textures/objects/coin_blue/idle.png")
		self.x = 0
		self.y = 0

class YellowCoin:
	def __init__(self):
		self.image = pg.image.load("assets/textures/objects/coin_yellow/idle.png")
		self.x = 0
		self.y = 0

class RedCoin:
	def __init__(self):
		self.image = pg.image.load("assets/textures/objects/coin_red/idle.png")
		self.x = 0
		self.y = 0