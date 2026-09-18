import pygame as pg

class Player:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.image = pg.image.load("assets/textures/characters/player/idle.png") # THIS IS THE DANIEL PRANK SPRITE. PLEASE FIX LATER.
		self.rect = self.image.get_rect(center=(self.x, self.y))

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def draw(self, screen): # "missing required positional argument for screen" apparently
		screen.blit(self.image, self.rect.topleft)