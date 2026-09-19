# importing modules
from modules import player, characters, objects, sounds, maps, enemies, cutscenes

# importing pygame shit
import pygame as pg
import sys

WIDTH, HEIGHT = 800, 600
GAME_NAME = "Horse Tale"

def init_pygame():
	screen = pg.display.set_mode((WIDTH, HEIGHT))

	pg.init()
	pg.display.set_caption(GAME_NAME)

	characters.Smirk.draw(screen)

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

		if event.type == pg.KEYDOWN and pg.K_ESCAPE:
			characters.Smirk.draw_shot(screen)

def process_logic():
	pass

def draw_game():
	pg.display.flip()

screen = init_pygame()

while True:
	#keys = pg.key.get_pressed()

	process_logic()
	draw_game()
	handle_input()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()