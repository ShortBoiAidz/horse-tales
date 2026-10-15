import pygame as pg

from data.components import player, maps, sounds
from data.states import soundstates

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

  def loadMap(self, pos, screen, mapSprites):
    global bar

    bar = maps.BarMap(pos, screen, mapSprites)

  def checkSounds(self):
    pass

  def update(self, pos, screen, mapSprites):
    self.loadMap(pos, screen, mapSprites)
    match self.mapstate:
      case "bar":
        bar.draw(screen, mapSprites)
      case "cave":
        sounds.caveTheme()
      case "jungle":
        pass

class PrintDebug:
  def printDebug(self):
    print(f"Mapstate: {currentMapObject.mapstate}")