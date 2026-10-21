import pygame as pg

from data.components import player, maps, sounds
from data.states import soundstates
from PygameTkinterGUITools import *
from pytmx.util_pygame import load_pygame as lpg

class defineObjects():
  def __init__(self):
    pass

  def update(self):
    global currentMapObject, playerObject, soundstatesObject, bar

    currentMapObject = currentMap()
    playerObject = player.Player()
    soundstatesObject = soundstates.checkSounds()

    bar = maps.Bar()

class currentMap:
  def __init__(self):
    self.mapstate = "bar"

  def checkSounds(self):
    pass

  def update(self, screen):
    match self.mapstate:
      case "bar":
        bar.drawMap(screen)
      case "cave":
        pass
      case "jungle":
        pass

class PrintDebug:
  def printDebug(self):
    print(f"Current Map: {currentMapObject.mapstate}")