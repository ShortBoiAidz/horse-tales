import pygame as pg

from data.states import mapstates
from data.components import sounds
from PygameTkinterGUITools import *

class checkSounds():
  def __init__(self):
    currentMapObject = mapstates.currentMap()

    self.mapstate = currentMapObject.mapstate
    self.sound = "[null]"

  def playSound(self):
    match self.mapstate:
      case "titleScreen":
        sounds.ThemeSound("HorseTale_mainTheme").play()
        self.sound = "Horse Tale Main Theme | ShortBoiAidz"

      case "bar":
        sounds.ThemeSound("long_face").play()
        self.sound = "Long Face | DJ Foot Fungus"
        
      case "cave":
        sounds.AmbientSound("cave").play()
        self.sound = "Wow Magic | 1empted"

  def printDebug(self):
    print(f"Current track: {self.sound}")

  def checkSounds(self):
    if pg.mixer.get_busy() == False:
      self.playSound()