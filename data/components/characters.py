import pygame as pg

from data.components import sounds
from data.states import mapstates
from PygameTkinterGUITools import *

DIALOGUE = [
  "Why the long face?"
]

def nextLine():
  global line

  line = (line + 1) % len(DIALOGUE)
  dialogue.config(text=DIALOGUE[line])

class Bartender(pg.sprite.Sprite):
  def __init__(self):
    global line, dialogue, rule

    super().__init__()
    self.x = 360
    self.y = 167

    self.idleImage = pg.image.load("assets/textures/characters/bartender/idle.png")
    self.idleImage = pg.transform.scale(self.idleImage, (72, 72))

    self.status = "active"

    self.sprites = []

    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (1).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (2).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (3).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (4).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (5).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (6).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (7).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (8).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (9).png"))

    self.current_sprite = 0

    self.rect = self.idleImage.get_rect(center=(self.x, self.y))

    line = 0
    rule = Separator(150, 100, length=500)
    dialogue = Message(100, 380, DIALOGUE[0],
                       width=600,
                       bg=(20, 20, 60),
                       fg=(255, 255, 255),
                       padding=16,
                       font_size=28
                       )

  def draw(self, screen):
    if self.status == "inactive":
      self.rect.topleft = (self.x, self.y)
      screen.blit(self.idleImage, self.rect.topleft)
    else:
      self.cycleAnimation(screen)

  def update(self, keys, screen):
    if keys[pg.K_e] or keys[pg.K_SPACE] == True:
      self.status = "inactive"
      dialogue.draw(screen)
      pg.display.flip()
    elif keys[pg.K_KP_ENTER]:
      nextLine()

  def cycleAnimation(self, screen):
    self.rect.topleft = (self.x, self.y)
    self.current_sprite += 1

    if self.current_sprite >= len(self.sprites):
      self.current_sprite = 0

    self.animatedImage = self.sprites[self.current_sprite]
    self.animatedImage = pg.transform.scale(self.animatedImage, (72, 72))

    screen.blit(self.animatedImage, self.rect.topleft)

  def printDebug(self):
    print(f"Bartender status: {self.status}")