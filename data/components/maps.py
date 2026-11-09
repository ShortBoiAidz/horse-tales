import pygame as pg
from libraries.PygameTkinterGUITools import *


from data.states import mapstates
from data.components import player
from libraries.justEnoughAssets import *


#& ----------------------------------


SPEED = 100
ORANGE = "#C24E00"


#& ----------------------------------

class defineObjects():
  def __init__(self):
    self._defineObjects()
    
  def _defineObjects(self):
    global playerObj, playerSprite, barMap

    playerObj = player.Player()
    playerSprite = playerObj.playerSprite

    barMap = Map(
                TMXfile="assets/textures/mapsheets/bar.tmx",
                playerObject=playerObj
                )


#& ----------------------------------


class TitleScreen():
  def __init__(self, screen):
    global menu, currentMapObj

    menu = Root(screen, bg=f"{ORANGE}", padding=300)
    menu.columnconfigure(0, weight=1)

    currentMapObj = mapstates.currentMap()

    createLabel(menu, "Horse Tale", 48, 0).draw()
    
    playButton = Button(menu, text="Start Game", command=lambda: self.changeMapstate())
    playButton.grid(row=1, column=0, pady=(0, 10))
    
    createLabel(menu, "Code by ShortBoiAidz \n Music by Helo and 1empted \n Maps by TeejMeister22", 24, 2).draw()


  def drawMap(self, screen):
    menu.draw(screen)


  def changeMapstate(self):
    currentMapObj.mapstate = "bar"