import pygame as pg
import sys
import os

WIDTH, HEIGHT = 800, 600
GAME_NAME = "Horse Tale"

class Player:
	def __init__(self):
		self.x = 0
		self.y = 0

class Prank:
	def __init__(self):
		self.x = 0
		self.y = 0

class Rooster:
	def __init__(self):
		self.x = 0
		self.y = 0

class BlueCoin:
	def __init__(self):
		self.x = 0
		self.y = 0

class YellowCoin:
	def __init__(self):
		self.x = 0
		self.y = 0

class RedCoin:
	def __init__(self):
		self.x = 0
		self.y = 0

class Smirk:
	def __init__(self):
		self.x = 0
		self.y = 0

def init_assets():
	# Load images, sounds, etc.
	pass

def process_logic():
	# Update game state, handle collisions, etc.
	pass

def draw_game():
	# Draw all game elements
	pass

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

def init_pygame(): # Initialise
	pg.init()
	pg.mixer.init()
	pg.display.set_caption(GAME_NAME)
	screen = pg.display.set_mode((WIDTH, HEIGHT))

	return screen

screen = init_pygame()

while True: # Running loop
	keys = pg.key.get_pressed()

	process_logic()
	draw_game()
	handle_input()

	for event in pg.event.get(): # Quit function
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()