import pygame as pg
from data.components import player

class currentMap:
  def __init__(self):
    self.mapstate = "caveEntrance"

  def update(self, screen, playerObjectRect):
    match self.mapstate:
      case "caveEntrance":
        caveEntranceMapObject.drawMap(screen)
        caveEntranceMapObject.update(screen, playerObjectRect)
      case "innerCave_0":
        innerCaveMap0_Object.drawMap(screen)
        innerCaveMap0_Object.update(screen, playerObjectRect)

  def drawHitbox(self, screen):
    match self.mapstate:
      case "caveEntrance":
        pg.draw.rect(screen, (255, 0, 0), caveEntranceMapObject.entranceRect, 2)
      case "innerCave_0":
        pass

  def collisionDetection(self, screen, playerObjectRect):
    if caveEntranceMapObject.entranceRect.colliderect(playerObjectRect): # Only triggers when hitboxes are colliding
      caveEntranceMapObject.switchMap(screen, playerObject)

class caveEntranceMap:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/cave_entrance.png")
    self.img = pg.transform.scale(self.img, (800, 800))

    self.entranceRect = pg.Rect(350, 230, 200, 100)
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)
    pg.draw.rect(screen, (0), self.entranceRect)

  def update(self, screen, playerObjectRect):
    self.entranceRect.update(350, 230, 200, 100)
    currentMapObject.collisionDetection(screen, playerObjectRect)

  def switchMap(self, screen, playerObjectRect):
    currentMapObject.mapstate = "innerCave_0"
    currentMapObject.update(screen, playerObjectRect)

class innerCaveMap_0:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/innerCave_0.png")
    self.img = pg.transform.scale(self.img, (800, 800))

    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)

  def update(self, screen, playerObjectRect):
    if playerObjectRect.x >= 745:
      playerObject.x = 500
      playerObject.draw(screen)

class PrintDebug:
  def printDebug(self):
    print(f"Mapstate: {currentMapObject.mapstate}")

playerObject = player.Player()
currentMapObject = currentMap()
caveEntranceMapObject = caveEntranceMap()
innerCaveMap0_Object = innerCaveMap_0()