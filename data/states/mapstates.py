import pygame as pg

from data.components import player, maps, sounds
from data.states import soundstates
from PygameTkinterGUITools import *

class defineObjects():
  def __init__(self):
    pass

  def update(self):
    global currentMapObject, playerObject, soundstatesObject

    currentMapObject = currentMap()
    playerObject = player.Player()
    soundstatesObject = soundstates.checkSounds()

class currentMap:
  def __init__(self):
    self.mapstate = "bar"

  def loadMap(self):
    global bar

    bar = maps.Bar()

  def checkSounds(self):
    pass

  def update(self, screen):
    self.loadMap()
    match self.mapstate:
      case "bar":
        bar.drawMap(screen)
      case "cave":
        pass
      case "jungle":
        pass

class PrintDebug:
  def printDebug(self):
    print(f"Mapstate: {currentMapObject.mapstate}")