import pygame as pg
from data.components import player

playerObject = player.Player()

class currentMap:
  def __init__(self):
    self.map = caveEntranceMap()
    self.mapstate = "innerCave_0"

  def update(self, screen):
    match self.mapstate:
      case "caveEntrance":
        self.map.drawMap(screen)
        self.map.update()
      case "innerCave_0":
        self.map = innerCaveMap_0()
        self.map.drawMap(screen)
        self.map.update()
      case "innerCave_1":
        self.map = innerCaveMap_1()
        self.map.drawMap(screen)
        self.map.update()
      case "innerCave_2":
        self.map = innerCaveMap_2()
        self.map.drawMap(screen)
        self.map.update()

class caveEntranceMap:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/cave_entrance.png")
    self.img = pg.transform.scale(self.img, (800, 600))

    self.entranceRect = pg.Rect(350, 230, 200, 100)
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)
    pg.draw.rect(screen, (0), self.entranceRect)

  def update(self):
    if self.entranceRect.colliderect(playerObject.rect):
      print("COLLIDE")
      currentMapObject.mapstate = "innerCave_0"

class innerCaveMap_0:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/innerCave_0.png")
    self.img = pg.transform.scale(self.img, (800, 600))
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)

  def update(self):
    if playerObject.x >= 800:
      currentMapObject.mapstate = "innerCave_1"

class innerCaveMap_1:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/innerCave_1.png")
    self.img = pg.transform.scale(self.img, (800, 600))
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)

  def update(self):
    pass

class innerCaveMap_2:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/innerCave_2.png")
    self.img = pg.transform.scale(self.img, (800, 600))
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)

  def update(self):
    pass

currentMapObject = currentMap()