# =====================
# RULES FOR FORMATTING
# =====================
# 1) Keep spacing and tabs consistent (Tab Size: 2)
# 2) DO NOT fuck with variables if you don't know what they do
# 3) If something works, DO NOT FUCKING TOUCH IT
# 4) Listen to other comments (e.g. labels)
# 5) Keep functions and shit consistent throughout all files

# importing modules
from data.states import cutscenes, mapstates
from data.components import items, sounds, player, characters, enemies

# importing pygame shit
import pygame as pg
import sys

WIDTH, HEIGHT = 800, 600
GAME_NAME = "Horse Tale"
DEBUG = True
HITBOX = True

def init_pygame():
	global clock, carleigheSmirk, danielPrank, playerObject, currentMap, keys

	screen = pg.display.set_mode((WIDTH, HEIGHT))
	clock = pg.time.Clock()

	# Character objects
	carleigheSmirk = characters.Smirk()
	danielPrank = characters.Prank()
	playerObject = player.Player()

	# Other objects
	currentMap = mapstates.currentMap()

	# Sprite groups
	movingSprites = pg.sprite.Group()
	movingSprites.add(playerObject)

	pg.init()
	pg.display.set_caption(GAME_NAME)

	return screen, clock

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

def process_logic():
	playerObject.update(keys)
	currentMap.update(screen, playerObject.rect)

def draw_game():
	playerObject.draw(screen)

	if HITBOX:
		playerObject.draw_hitbox(screen)
		currentMap.drawHitbox(screen)

	pg.display.flip()

screen, clock = init_pygame()

while True:
	keys = pg.key.get_pressed()

	process_logic()
	draw_game()
	handle_input()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

	if DEBUG:
		print(f"Player coords: {playerObject.x, playerObject.y}")

	clock.tick(10)