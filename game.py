# =====================
# RULES FOR FORMATTING
# =====================
# 1) Keep spacing and tabs consistent (Tab Size: 2)
# 2) DO NOT fuck with variables if you don't know what they do
# 3) If something works, DO NOT FUCKING TOUCH IT
# 4) Listen to other comments (e.g. labels)
# 5) Keep names and shit consistent throughout all files
# 6) DO NOT FUCKING NEST. NEVER NEST. WE HATE NESTERS. NO STUPID IF STATEMENTS INSIDE OTHER IF STATEMENTS. FIND A BETTER SOLUTION.
# 7) Try to avoid repeating code. Call another function if you have to
# 8) Try to keep camelCase and rarely use snake_case

# importing modules
from data.states import cutscenes, mapstates, soundstates
from data.components import items, sounds, player, characters, enemies, maps
from PygameTkinterGUITools import *
# importing pygame shit
import pygame as pg
import sys
from pytmx.util_pygame import load_pygame as lpg

WIDTH, HEIGHT = 800, 800
GAME_NAME = "Horse Tale"
DEBUG = True
HITBOX = False

def init_pygame():
	global clock, bartender, playerObject, currentMap, printMapstateDebug, keys, mapSprites, mapstatesDefineObjects, soundstatesObject, bar, barMap

	screen = pg.display.set_mode((WIDTH, HEIGHT))
	clock = pg.time.Clock()

	# Character objects
	bartender = characters.Bartender()
	playerObject = player.Player()

	# Map shit
	mapSprites = pg.sprite.Group() # MAPSPRITES. THIS IS IMPORTANT. DO NOT MOVE.

	mapstatesDefineObjects = mapstates.defineObjects()
	currentMap = mapstates.currentMap()
	printMapstateDebug = mapstates.PrintDebug()

	# Objects and stuff
	soundstatesObject = soundstates.checkSounds()
	barMap = maps.Bar()

	# Sprite groups
	movingSprites = pg.sprite.Group()
	movingSprites.add(playerObject)

	# More stuff
	bar = lpg("assets/textures/mapsheets/bar.tmx")

	pg.init()
	pg.display.set_caption(GAME_NAME)

	return screen, clock

def handle_input():
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

def process_logic():
	mapstatesDefineObjects.update()
	playerObject.update(keys)
	currentMap.update(screen)
	bartender.update(keys)

def draw_game():
	playerObject.draw(screen)
	barMap.drawMap(screen)
	bartender.draw(screen)

	if HITBOX:
		playerObject.drawHitbox(screen)
		currentMap.drawHitbox(screen)

	pg.display.flip()

screen, clock = init_pygame()

soundstatesObject.playSound()

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
		print("========")
		printMapstateDebug.printDebug()
		playerObject.printDebug()
		soundstatesObject.printDebug()
		bartender.printDebug(f"Bartender status: {bartender.status}")

	clock.tick(17)