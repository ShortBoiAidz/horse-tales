import pygame as pg
from PygameTkinterGUITools import *

class Player(pg.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 250
    self.y = 230

    self.sprites_left = []
    self.sprites_right = []

    self.sprites_left.append(pg.image.load("assets/textures/characters/player/walk1_left.png"))
    self.sprites_left.append(pg.image.load("assets/textures/characters/player/walk2_left.png"))

    self.sprites_right.append(pg.image.load("assets/textures/characters/player/walk1_right.png"))
    self.sprites_right.append(pg.image.load("assets/textures/characters/player/walk2_right.png"))

    self.current_sprite = 0
    self.image = self.sprites_left[self.current_sprite]
    self.image = self.sprites_right[self.current_sprite]
    self.image = pg.transform.scale(self.image, (96, 96))
    self.rect = self.image.get_rect(center=(self.x, self.y))

  def update(self, keys):
    if keys[pg.K_LEFT] or keys[pg.K_a] == True:
      self.x -= 10
      self.cycleSprites_left()

    elif keys[pg.K_RIGHT] or keys[pg.K_d] == True:
      self.x += 10
      self.cycleSprites_right()

    elif keys[pg.K_UP] or keys[pg.K_w] == True:
      self.y -= 10
      self.cycleSprites_right()

    elif keys[pg.K_DOWN] or keys[pg.K_s] == True:
      self.y += 10
      self.cycleSprites_left()

    elif keys[pg.K_DOWN] and keys[pg.K_LEFT] or keys[pg.K_s] and keys[pg.K_a] == True:
      self.y += 5
      self.x -= 5
      self.cycleSprites_left
 
    elif keys[pg.K_DOWN] and keys[pg.K_RIGHT] or keys[pg.K_s] and keys[pg.K_d] == True:
      self.y += 5
      self.x += 5
      self.cycleSprites_right
 
    elif keys[pg.K_UP] and keys[pg.K_LEFT] or keys[pg.K_w] and keys[pg.K_a] == True:
      self.y -= 5
      self.x -= 5
      self.cycleSprites_left
 
    elif keys[pg.K_UP] and keys[pg.K_RIGHT] or keys[pg.K_w] and keys[pg.K_d] == True:
      self.y -= 5
      self.x += 5
      self.cycleSprites_right

  def draw(self, screen):
    self.rect.topleft = (self.x, self.y)
    screen.blit(self.image, self.rect.topleft)

  def drawHitbox(self, screen):
    pg.draw.rect(screen, (255, 0, 0), self.rect, 2)

  def cycleSprites_left(self):
    self.rect.topleft = (self.x, self.y)
    self.current_sprite += 1

    if self.current_sprite >= len(self.sprites_left):
      self.current_sprite = 0

    self.image = self.sprites_left[self.current_sprite]
    self.image = pg.transform.scale(self.image, (96, 96))

  def cycleSprites_right(self):
    self.rect.topleft = (self.x, self.y)
    self.current_sprite += 1

    if self.current_sprite >= len(self.sprites_right):
      self.current_sprite = 0

    self.image = self.sprites_right[self.current_sprite]
    self.image = pg.transform.scale(self.image, (96, 96))

  def printDebug(self):
    print(f"Player coords: ({self.x}, {self.y})")