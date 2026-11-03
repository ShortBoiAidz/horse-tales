import pygame as pg

from data.components import maps, sounds
from data.states import soundstates
from libraries.PygameTkinterGUITools import *
from pytmx.util_pygame import load_pygame as lpg

class defineObjects():
  @staticmethod
  def update():
    global currentMapObject, soundstatesObject, bar, title

    currentMapObject = currentMap()
    soundstatesObject = soundstates.checkSounds()

    bar = maps.Bar()
    title = maps.TitleScreen(pg.display.get_surface())

class currentMap:
  def __init__(self):
    self.mapstate = "bar"

  def update(self, screen):
    match self.mapstate:
      case "titleScreen":
        title.drawMap(screen)
      case "bar":
        bar.drawMap(screen)
      case "cave":
        pass
      case "jungle":
        pass

class PrintDebug:
  @staticmethod
  def printDebug():
    print(f"Current Map: {currentMapObject.mapstate}")