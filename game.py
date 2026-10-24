
#* =====================
#* RULES FOR FORMATTING
#* =====================
#* 1) Keep spacing and tabs consistent (Tab Size: 2)
#* 2) DO NOT fuck with variables if you don't know what they do
#* 3) If something works, DO NOT FUCKING TOUCH IT
#* 4) Listen to other comments (e.g. labels)
#* 5) Keep names and shit consistent throughout all files
#* 6) DO NOT FUCKING NEST. NEVER NEST. WE HATE NESTERS. NO STUPID IF STATEMENTS INSIDE OTHER IF STATEMENTS. FIND A BETTER SOLUTION.
#* 7) Try to avoid repeating code. Call another function if you have to
#* 8) Try to keep camelCase and rarely use snake_case

from data.states import cutscenes, mapstates, soundstates
from data.components import items, sounds, player, characters, enemies, maps

import pygame as pg
import sys

WIDTH, HEIGHT = 800, 800
GAME_NAME = "Horse Tale"
DEBUG = True
HITBOX = False
FPS = 20

def init_pygame():
	global clock, bartenderObj, playerSprite, playerAnimator, playerObj, currentMap, printMapstateDebug, keys, bartenderDialogObj, barObj, mapstatesDefineObjects, soundstatesObject

	screen = pg.display.set_mode((WIDTH, HEIGHT))
	clock = pg.time.Clock()

	#& Character objects
	bartenderObj = characters.Bartender()
	playerObj = player.Player()
	playerAnimator = playerObj.playerAnimator
	playerSprite = playerObj.playerSprite

	#& Map shit
	mapstatesDefineObjects = mapstates.defineObjects()
	currentMap = mapstates.currentMap()
	printMapstateDebug = mapstates.PrintDebug()

	#& Objects and stuff
	soundstatesObject = soundstates.checkSounds()
	bartenderDialogObj = characters.bartenderDialogObj
	barObj = maps.Bar()

	pg.init()
	pg.display.set_caption(GAME_NAME)

	return screen, clock

# ----------------------------------

def process_logic():
	mapstatesDefineObjects.update()
	playerObj.update(keys, tick)
	currentMap.update(screen)
	bartenderObj.update()
	bartenderDialogObj.update(keys)
	barObj.update(tick, keys)

# ----------------------------------

def draw_game():
	bartenderObj.draw(screen)
	playerSprite.draw(screen)
	playerObj.drawAnimation(screen, tick)

	pg.display.flip()

screen, clock = init_pygame()

soundstatesObject.playSound()

# ===============================

while True:
	keys = pg.key.get_pressed()
	tick = clock.tick(FPS)

	process_logic()
	draw_game()

	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

	if DEBUG:
		print("========")
		printMapstateDebug.printDebug()
		playerObj.printDebug()
		soundstatesObject.printDebug()
		bartenderObj.printDebug(f"Bartender status: {bartenderObj.status}")