# importing modules
from modules import player, characters, objects, sounds, maps, enemies, cutscenes

# importing pygame shit
import pygame as pg
import sys

WIDTH, HEIGHT = 800, 600
GAME_NAME = "Horse Tale"

def init_pygame():
	global carleigheSmirk, danielPrank

	screen = pg.display.set_mode((WIDTH, HEIGHT))

	carleigheSmirk = characters.Smirk()
	danielPrank = characters.Prank()

	pg.init()
	pg.display.set_caption(GAME_NAME)

	carleigheSmirk.draw(screen)

	return screen

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

		if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			carleigheSmirk.draw_shot(screen)
		if event.type == pg.KEYDOWN and event.key == pg.K_g:
			danielPrank.draw(screen)

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