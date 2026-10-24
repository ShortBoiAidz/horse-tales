
#* =====================
#* RULES FOR FORMATTING
#* =====================
#* 1) Keep spacing and tabs consistent (Tab Size: 2)
#* 2) DO NOT fuck with variables if you don't know what they do
#* 3) If something works, DO NOT FUCKING TOUCH IT
#* 4) Listen to other comments (e.g. labels)
#* 5) Keep names and shit consistent throughout all files
#%important 6) DO NOT FUCKING NEST. NEVER NEST. WE HATE NESTERS. NO STUPID IF STATEMENTS INSIDE OTHER IF STATEMENTS. FIND A BETTER SOLUTION.
#* 7) Try to avoid repeating code. Call another function if you have to
#* 8) Try to keep camelCase and rarely use snake_case
#* 9) If a created function has more than 1 param (or is complex), use a docstring to explain the function

#& ----------------------------------

#* ==========
#* COMMENTING
#* ==========
#%important = Important things to deal with; priorities.
#!bug = Use on the same line as the bug; explain the error.
#todo = Things to do / work on
#note^ = Note for other collaborators. Use on the line below of which it applies to.
#& = Dividers
#~path = Explaining the path of which a file is linked to
#?query = Question or query
#$suggestion = Suggestion for other collaborators
#* = Typically for headings.
#Strikethrough / commenting out code = #//

#& ===============================

from data.states import cutscenes, mapstates, soundstates
from data.components import items, sounds, player, characters, enemies, maps

import pygame as pg
import sys

#& ----------------------------------

WIDTH, HEIGHT = 800, 800
GAME_NAME = "Horse Tale"
DEBUG = True
HITBOX = False
FPS = 20

#& ----------------------------------

def init_pygame():
	"""Initialises and globalises objects, Pygame, and variables.

	Returns:
			_screen_: Sets pygame display mode
			_clock_: Pygame _Clock()_ function
	"""
	global clock, bartenderObj, playerSprite, playerAnimator, playerObj, currentMap, printMapstateDebug, keys, bartenderDialogObj, barObj, mapstatesDefineObjects, soundstatesObject

	screen = pg.display.set_mode((WIDTH, HEIGHT))
	clock = pg.time.Clock()

	bartenderObj = characters.Bartender()
	playerObj = player.Player()
	playerAnimator = playerObj.playerAnimator
	playerSprite = playerObj.playerSprite
	#note^ Character objects

	mapstatesDefineObjects = mapstates.defineObjects()
	currentMap = mapstates.currentMap()
	printMapstateDebug = mapstates.PrintDebug()
	#note^ Map shit

	soundstatesObject = soundstates.checkSounds()
	bartenderDialogObj = characters.bartenderDialogObj
	barObj = maps.Bar()
	#note^ Objects and stuff

	pg.init()
	pg.display.set_caption(GAME_NAME)

	return screen, clock

#& ----------------------------------

def process_logic():
	"""Runs on the _while_ loop. Runs _update()_ functions for objects.
	"""
	mapstatesDefineObjects.update()
	playerObj.update(keys, tick)
	currentMap.update(screen)
	bartenderObj.update()
	bartenderDialogObj.update(keys)
	barObj.update(tick, keys)

#& ----------------------------------

def draw_game():
	"""Renders the game.
	"""
	bartenderObj.draw(screen)
	playerSprite.draw(screen)
	playerObj.drawAnimation(screen, tick)

	pg.display.flip()

#& ===============================

screen, clock = init_pygame()

soundstatesObject.playSound()

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