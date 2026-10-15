import pygame as pg

from data.states import mapstates
from data.components import sounds

class checkSounds():
  def __init__(self):
    currentMapObject = mapstates.currentMap()

    self.mapstate = currentMapObject.mapstate
    self.sound = "[null]"

  def playSound(self):
    match self.mapstate:
      case "bar":
        sounds.caveTheme()
        self.sound = "Cave Theme"

  def printDebug(self):
    print(f"Current track: {self.sound}")

  def checkSounds(self):
    if pg.mixer.get_busy == False:
      self.playSound()