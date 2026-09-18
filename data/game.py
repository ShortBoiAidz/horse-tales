# importing modules
import modules.player as player
import modules.characters as characters
import modules.objects as objects
import modules.sounds as sounds

# importing pygame shit
import pygame as pg
import sys
import os

WIDTH, HEIGHT = 800, 600
GAME_NAME = "Horse Tale"

def process_logic():
	pass

def draw_game():
	player.Player.draw(screen) # "missing required positional argument for screen" apparently

	pg.display.flip()

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

def init_pygame():
	pg.init()
	pg.mixer.init()
	pg.display.set_caption(GAME_NAME)
	screen = pg.display.set_mode((WIDTH, HEIGHT))

	return screen

screen = init_pygame(), sounds.init_assets()

while True:
	keys = pg.key.get_pressed()

	process_logic()
	draw_game()
	handle_input()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()