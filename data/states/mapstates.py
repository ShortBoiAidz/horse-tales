import pygame as pg
from data.components import player

class currentMap:
  def __init__(self):
    self.map = caveEntranceMap()
    self.mapstate = "caveEntrance"

  def update(self, screen, playerObjectRect):
    match self.mapstate:
      case "caveEntrance":
        self.map.drawMap(screen)
        self.map.update(screen, playerObjectRect)
      case "innerCave_0":
        self.map = innerCaveMap_0()
        self.map.drawMap(screen)
        self.map.update(screen, playerObjectRect)
      case "innerCave_1":
        self.map = innerCaveMap_1()
        self.map.drawMap(screen)
        self.map.update(screen, playerObjectRect)
      case "innerCave_2":
        self.map = innerCaveMap_2()
        self.map.drawMap(screen)
        self.map.update(screen, playerObjectRect)

  def drawHitbox(self, screen):
    match self.mapstate:
      case "caveEntrance":
        pg.draw.rect(screen, (255, 0, 0), self.map.entranceRect, 2)

class caveEntranceMap:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/cave_entrance.png")
    self.img = pg.transform.scale(self.img, (800, 600))

    self.entranceRect = pg.Rect(350, 230, 200, 100)
    self.rect = self.img.get_rect()

    self.mapstate = "innerCave_0"

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)
    pg.draw.rect(screen, (0), self.entranceRect)

  def update(self, screen, playerObjectRect):
    self.entranceRect.update(350, 230, 200, 100)

    if self.entranceRect.colliderect(playerObjectRect):
      print("COLLIDE")
      currentMap.update(self, screen, playerObjectRect)

class innerCaveMap_0:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/innerCave_0.png")
    self.img = pg.transform.scale(self.img, (800, 600))

    self.rect = self.img.get_rect()

    self.mapstate = "innerCave_1"

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)

  def update(self, screen, playerObjectRect):
    if playerObjectRect.x >= 800:
      playerObject.x = 500
      playerObject.draw(screen)

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

playerObject = player.Player()
currentMapObject = currentMap()