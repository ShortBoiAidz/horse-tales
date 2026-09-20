# importing modules
from data.states import cutscenes, mapstates
from data.components import sounds, player, characters, objects, enemies

# importing pygame shit
import pygame as pg
import sys

WIDTH, HEIGHT = 800, 600
GAME_NAME = "Horse Tale"

def init_pygame():
	global carleigheSmirk, danielPrank, playerObject

	screen = pg.display.set_mode((WIDTH, HEIGHT))

	carleigheSmirk = characters.Smirk()
	danielPrank = characters.Prank()
	playerObject = player.Player("assets/textures/characters/player/idle.png")

	pg.init()
	pg.display.set_caption(GAME_NAME)

	carleigheSmirk.draw(screen)
	playerObject.draw(screen)

	return screen

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

		if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			carleigheSmirk.draw_shot(screen)
		elif event.type == pg.KEYDOWN and event.key == pg.K_g:
			danielPrank.draw(screen)
		elif event.type == pg.KEYDOWN and event.key == pg.K_1:
			characters.Smirk.dialog()

def process_logic():
	playerObject.update()

def draw_game():
	pg.display.flip()

screen = init_pygame()

while True:
	keys = pg.key.get_pressed()

	process_logic()
	draw_game()
	handle_input()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()