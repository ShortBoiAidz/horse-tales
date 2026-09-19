import pygame as pg

class Player:
	def __init__(self, image):
		self.x = 800 // 2
		self.y = 600 // 2
		self.image = pg.image.load(image)
		self.rect = self.image.get_rect(center=(self.x, self.y))

	def move(self, dx, dy):
		pass

	def draw(self, screen):
		screen.blit(self.image, self.rect.topleft)