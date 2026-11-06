

#* Please refer to './rulesForDevs.py' for information on how to structure documents.


from data.states import mapstates, soundstates
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
  global clock, bartenderObj, playerSprite, playerAnimator, playerObj, currentMap, printMapstateDebug, keys, bartenderDialogObj, barObj, mapstatesDefineObjects, soundstatesObject, characterObj


  screen = pg.display.set_mode((WIDTH, HEIGHT))
  clock = pg.time.Clock()


  #* Character Objects
  characterObj = characters.characterObj
  bartenderObj = characterObj.bartenderObj


  #* Map objects
  mapstatesDefineObjects = mapstates.defineObjects()
  currentMap = mapstates.currentMap()
  printMapstateDebug = mapstates.PrintDebug()
  barObj = maps.Bar
  barObj.add_sprite(bartenderObj) #!bug Bartender does not stay put when the camera is following the player


  #* Misc Objects
  soundstatesObject = soundstates.checkSounds()
  playerObj = maps.playerObj
  playerAnimator = playerObj.playerAnimator
  playerSprite = playerObj.playerSprite


  pg.init()
  pg.display.set_caption(GAME_NAME)


  return screen, clock


#& ----------------------------------


def process_logic():
  """Runs _update()_ functions for objects.
  """
  barObj.update(screen, tick, keys)
  currentMap.update(screen)
  characterObj.updateCharacters(keys, screen)


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
    printMapstateDebug.printDebug()
    playerObj.printDebug()
    soundstatesObject.printDebug()
    # bartenderObj.printDebug(f"Bartender status: {bartenderObj.status}")
    print("========")