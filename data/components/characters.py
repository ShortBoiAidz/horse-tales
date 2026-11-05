import json
import pygame as pg
import random


from data.components import sounds
from data.states import mapstates
from libraries.PygameTkinterGUITools import *


#& ----------------------------------

with open("data/characters.json", "r") as characters:
    charactersJSON = json.load(characters)

screen = pg.display.set_mode([800, 800])


#& ----------------------------------


#$suggestion Thinking of making a seperate animated sprite for the green exclamation mark so we can render it over any character.


class Character(pg.sprite.Sprite):
  def __init__(self, character, x, y):
    """Base class for different characters to inherit from.

    Args:
        character (_str_): Name of the directory containing images for the character.
        x (_int_): starting X coordinate
        y (_int_): starting Y coordinate
    """


    super().__init__()


    self.x = x
    self.y = y


    self.idleImage = pg.image.load(f"assets/textures/characters/{character}/idle.png")
    self.idleImage = pg.transform.scale(self.idleImage, (72, 72))


    pg.font.init()
    self.font = pg.font.Font('freesansbold.ttf', 24)


    self.textCounter = 0
    self.textSpeed = 1
    self.textCompleted = False
    self.snip = self.font.render('', True, (255, 255, 255))


    self.dialog = (charactersJSON["Characters"][f"{character}"]["dialog"])
    self.randomDialog = (charactersJSON["Characters"][f"{character}"]["randomDialog"])

    #TODO: Make a randomised function for the "random dialog" so the random dialog text plays AFTER the normal dialog happens


    self.activeMessage = 0
    self.activeRandomMessage = random.randint(0, len(self.randomDialog) - 1)

    self.dialog = self.dialog[self.activeMessage]
    self.randomDialog = self.randomDialog[self.activeRandomMessage]


    self.status = "inactive"


    self.sprites = []


    self.current_sprite = 0


    self.rect = self.idleImage.get_rect(topleft=(self.x, self.y))


  def draw(self, screen, camera=None):
    if self.status == "active":
      rect = camera.apply(self.rect) if camera else self.rect
      screen.blit(self.idleImage, rect)
    else:
      self.cycleAnimation(screen, camera)


  def cycleAnimation(self, screen, camera=None):
    self.current_sprite += 1


    if self.current_sprite >= len(self.sprites):
      self.current_sprite = 0


    self.animatedImage = self.sprites[self.current_sprite]
    self.animatedImage = pg.transform.scale(self.animatedImage, (72, 72))

    rect = camera.apply(self.rect) if camera else self.rect
    screen.blit(self.animatedImage, rect)


  def printDebug(self, message):
    print(message)

#& ----------------------------------

class Bartender(Character):
  #note^ Bartender's name is Gek
  def __init__(self):
    super().__init__("bartender", 310, 170)


    #~path I would love to change these to camelSnake_case
    self.sprites.append(pg.image.load("assets/textures/characters/danielPrank/animation/frame (1).png"))
    #note^ This is really horrible
    #$suggestion Perhaps make a spritesheet instead


class BartenderDialog:
  def __init__(self):
    self.textRunning = False


  def update(self, keys):
    if (keys[pg.K_e] == True):
      self.textRunning = True
      bartenderObj.status = "active"


    if self.textRunning == True:
      self.drawDialog()
     
    if bartenderObj.textCompleted and keys[pg.K_e] == True:
      bartenderObj.activeMessage += 1
      self.drawDialog()
      self.textRunning = False


  def drawDialog(self):
    pg.draw.rect(screen, (20, 20, 60), [0, 700, 800, 500])
   
    if bartenderObj.textCounter < bartenderObj.textSpeed * len(bartenderObj.dialog):
      bartenderObj.textCounter += 1
      sounds.SFXSound("bartender_voice").play()


    elif (bartenderObj.textCounter >= bartenderObj.textSpeed * len(bartenderObj.dialog)):
      bartenderObj.textCompleted = True


    bartenderObj.snip = bartenderObj.font.render(bartenderObj.dialog[0: bartenderObj.textCounter//bartenderObj.textSpeed], True, (255, 255, 255))
    screen.blit(bartenderObj.snip, (10, 710))


  def nextLine():
    global line


    line = (line + 1) % len(bartenderObj.dialog)


#& ----------------------------------


class DanielPrank(Character):
  def __init__(self):
    global line


    super().__init__("bartender", 310, 170)


    #~path I would love to change these to camelSnake_case
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (1).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (2).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (3).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (4).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (5).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (6).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (7).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (8).png"))
    self.sprites.append(pg.image.load("assets/textures/characters/bartender/animation/frame (9).png"))
    #note^ This is really horrible
    #$suggestion Perhaps make a spritesheet instead


class DanielPrankDialog():
  def __init__(self):
    pass


#& ----------------------------------


bartenderObj = Bartender()
bartenderDialogObj = BartenderDialog()

danielPrankObj = DanielPrank()
danielPrankDialogObj = DanielPrankDialog()