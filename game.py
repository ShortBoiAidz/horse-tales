

#* Please refer to './rulesForDevs.py' for information on how to structure documents.


from data.states import mapstates, soundstates
from data.components import items, sounds, characters, enemies, maps, player
from libraries import justEnoughAssets as jea


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
  global clock, bartender_obj, danielPrank_obj, playerSprite, playerAnimator, playerObj, currentMap, printMapstateDebug, keys, barObj, mapstatesDefineObjects, mapsDefineObjects, soundstatesObject, renderCharactersObj

  screen = pg.display.set_mode((WIDTH, HEIGHT))
  clock = pg.time.Clock()


  #* Character Objects
  renderCharactersObj = characters.RenderCharacters()

  bartender_obj = renderCharactersObj.bartenderObj
  danielPrank_obj = renderCharactersObj.danielPrank


  #* Map and Sound objects
  mapsDefineObjects = maps.defineObjects()
  mapstatesDefineObjects = mapstates.defineObjects()

  currentMap = mapstates.currentMap()
  
  barObj = mapstates.bar
  
  barObj.add_sprite(bartender_obj)
  soundstatesObject = soundstates.checkSounds()


  #* Misc Objects
  playerObj = maps.playerObj
  playerAnimator = playerObj.playerAnimator
  playerSprite = playerObj.playerSprite


  #* Proximity Detection
  bartender_obj.proximity = jea.Proximity(
    bartender_obj,
    coordinates=(334, 189),
    interactionRange=110,
    player=playerSprite,
  )
  danielPrank_obj.proximity = jea.Proximity(
    danielPrank_obj,
    coordinates=(630, 170),
    interactionRange=100,
    player=playerSprite,
  )


  #* Debug shit
  printMapstateDebug = mapstates.PrintDebug()
  

  pg.init()
  pg.display.set_caption(GAME_NAME)


  return screen, clock


#& ----------------------------------


def process_logic():
  """Runs _update()_ functions for objects.
  """
  
  barObj.update(screen, tick)
  currentMap.update(screen)
  renderCharactersObj.updateCharacters(screen, tick, playerSprite)


#& ----------------------------------


def init_justEnoughAssets():
  jea.init()


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


  init_justEnoughAssets()
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
    bartender_obj.printDebug(f"Bartender status: {bartender_obj.status}")
    print("========")