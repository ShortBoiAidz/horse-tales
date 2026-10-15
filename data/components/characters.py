import pygame as pg

from data.components import sounds
from data.states import mapstates
from PygameTkinterGUITools import *

screen = pg.display.set_mode([800, 800])

def nextLine():
  global line

  line = (line + 1) % len(bartenderObj.dialogue)

class Bartender(pg.sprite.Sprite):
  def __init__(self):
    global line, textRunning

    super().__init__()
    self.x = 360
    self.y = 167

    self.idleImage = pg.image.load("assets/textures/characters/bartender/idle.png")
    self.idleImage = pg.transform.scale(self.idleImage, (72, 72))

    pg.font.init()
    self.font = pg.font.Font('freesansbold.ttf', 24)

    self.textCounter = 0
    self.textSpeed = 3
    self.textCompleted = False
    self.snip = self.font.render('', True, (255, 255, 255))

    self.dialogue = [
                      "Why the long face?",
                      "Oh...you're upset? I'd hate to be you.",
                      "My go-to solution is always resorting to alcohol. Fancy a beer?"
                    ]
    self.activeMessage = 0
    self.dialogue = self.dialogue[self.activeMessage]

    textRunning = False

    self.status = "inactive"

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

  def draw(self, screen):
    if self.status == "active":
      self.rect.topleft = (self.x, self.y)
      screen.blit(self.idleImage, self.rect.topleft)
    else:
      self.cycleAnimation(screen)

  def update(self, keys, screen):
    global textRunning

    if keys[pg.K_e] or keys[pg.K_SPACE] == True:
      textRunning = True
      self.status = "active"
      pg.display.flip()

    if keys[pg.K_RETURN] and self.textCompleted and self.activeMessage < len(self.dialogue):
      self.activeMessage += 1
      self.textCompleted = False
      self.dialogue = self.dialogue[self.activeMessage]
      self.textCounter = 0

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

bartenderObj = Bartender()

while textRunning:
  pg.draw.rect(screen, (20, 20, 60), [0, 300, 800, 200])
  if bartenderObj.textCounter < bartenderObj.textSpeed * len(bartenderObj.dialogue):
    bartenderObj.textCounter += 1

  elif bartenderObj.textCounter >= bartenderObj.textSpeed * len(bartenderObj.dialogue):
    bartenderObj.textCompleted = True

  bartenderObj.snip = bartenderObj.font.render(bartenderObj.dialogue[0: bartenderObj.textCounter//bartenderObj.textSpeed], True, (255, 255, 255))
  pg.display.flip()