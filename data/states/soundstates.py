import pygame as pg

from data.states import mapstates
from data.components import sounds

class checkSounds():
  def __init__(self):
    currentMapObject = mapstates.currentMap()

    self.mapstate = currentMapObject.mapstate
    self.sound = "[null]"

#&--------------------------------------------------------

#* Check sounds
  def checkSounds(self):
    if pg.mixer.get_busy() == False:
      self.playSound()

#&--------------------------------------------------------

#* Play sounds
  def playSound(self):
    match self.mapstate:
      case "titleScreen":
        sounds.ThemeSound("lordStalPiggies_wConcept").play()
        self.sound = "Horse Tale Main Theme | 1empted"

      case "bar":
        sounds.ThemeSound("long_face").play()
        self.sound = "Long Face | DJ Foot Fungus"
        
      case "cave":
        sounds.AmbientSound("cave").play()
        self.sound = "Wow Magic | 1empted"

#&--------------------------------------------------------

#* Debug
  def printDebug(self):
    print(f"Current track: {self.sound}")