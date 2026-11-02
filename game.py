

#* Please refer to './rulesForDevs.py' for information on how to structure documents.


from data.states import cutscenes, mapstates, soundstates
from data.components import items, sounds, characters, enemies, maps


import pygame as pg
import sys


#& ----------------------------------


WIDTH, HEIGHT = 800, 800
GAME_NAME = "Horse Tale"
DEBUG = True
HITBOX = True
FPS = 30


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
  #note^ Character objects


  mapstatesDefineObjects = mapstates.defineObjects()
  currentMap = mapstates.currentMap()
  printMapstateDebug = mapstates.PrintDebug()
  #note^ Map shit


  soundstatesObject = soundstates.checkSounds()
  bartenderDialogObj = characters.bartenderDialogObj
  mapstatesDefineObjects.update()
  barObj = mapstates.bar
  barObj.add_sprite(bartenderObj)
  playerObj = maps.playerObj
  playerAnimator = playerObj.playerAnimator
  playerSprite = playerObj.playerSprite
  #note^ Objects and stuff


  pg.init()
  pg.display.set_caption(GAME_NAME)


  return screen, clock


#& ----------------------------------


def process_logic():
  """Runs _update()_ functions for objects.
  """
  barObj.update(tick, keys)
  currentMap.update(screen)
  bartenderObj.update()
  bartenderDialogObj.update(keys)


#& ----------------------------------


def draw_game():
  """Renders the game.
  """
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