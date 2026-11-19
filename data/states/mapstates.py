import pygame as pg

from data.components import maps
from data.states import soundstates

from libraries.PygameTkinterGUITools import *


#& ----------------------------------

class defineObjects():
  def __init__(self):
    self._defineObjects()
    
  def _defineObjects(self):
    global currentMapObj, soundstatesObj, bar, title, cave

    currentMapObj = currentMap()
    soundstatesObj = soundstates.checkSounds()

    #* Creating maps / scenes
    title = maps.TitleScreen(pg.display.get_surface())
    bar = maps.barMap
    # cave = maps.caveMap #!bug This needs every tile asset. So far, we just have the TMX file.

#&===============================================
class currentMap:
  def __init__(self):
    self.mapstate = "bar"

#&--------------------------------------------------------

#* Update
  def update(self, screen):
    """Uses a switch statement to switch maps and render them using their corresponding drawMap(_screen_) function

    Args:
        screen (pygame.Surface): The screen surface to draw the map on
    """
    match self.mapstate:
      case "titleScreen":
        title.drawMap(screen)
      case "bar":
        bar.drawMap(screen)
      case "cave":
        cave.drawMap(screen)
      case "jungle":
        pass