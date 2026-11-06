
import pygame as pg
import random
import json
import sys

from libraries.PygameTkinterGUITools import *


#& ----------------------------------

class createLabel():
  def __init__(self, scene, text, font_size, row):
    """Creates a label using Pygame Tkinter Gui Tools but makes it a little easier to read and write. Kind of just an extra layer of maintainability.

    Args:
        scene (str): The scene to which the label belongs. E.g. "menu" or "game"
        text (str): The text to display on the label
        font_size (int): The size of the font for the label
        row (int): The row position of the label
    """
    self.text = text
    self.font_size = font_size
    self.row = row
    self.scene = scene


  def draw(self):
    Label(self.scene, text=self.text, font_size=self.font_size).grid(row=self.row, column=0, pady=(0, 20))


class Character(pg.sprite.Sprite):
  def __init__(self, character, x, y, pathToImg=None, animation=False, pathToAnimation=None, width=None, height=None, rows=None, cols=None, allowJSON=False, pathToJSON=None):
    """Creates a character sprite with dialog functionality. Allows for customization of the character's dialog through JSON files. See documentation for required JSON structure.

    Args:
        character (_str_): The name of the character to create. Must be the same as the image file names.
        x (_int_): The x-coordinate of the character's position.
        y (_int_): The y-coordinate of the character's position.
        pathToImg (_str_): The path to the directory containing the character's image assets.
        
        animation (_bool_): Whether the character has an animation. Defaults to False.
        pathToAnimation (_str_): The path to the directory containing the character's animation spritesheet.
        width (_int_): The width of each frame in the animation spritesheet.
        height (_int_): The height of each frame in the animation spritesheet.
        rows (_int_): The number of rows in the animation spritesheet.
        cols (_int_): The number of columns in the animation spritesheet.
        
        allowJSON (bool, optional): Whether to allow JSON dialog customization. Defaults to False.
        pathToJSON (_str_): The path to the JSON file containing character data.
    """

    with open(pathToJSON, "r") as characters:
      charactersJSON = json.load(characters)


    super().__init__()


    self.animation = animation


    self.x = x
    self.y = y


    self.idleImage = pg.image.load(pathToImg + "/idle.png")
    self.idleImage = pg.transform.scale(self.idleImage, (72, 72))


    pg.font.init()
    self.font = pg.font.Font('freesansbold.ttf', 24)


    self.status = "notTalking"


    self.textCounter = 0
    self.textSpeed = 1
    self.textCompleted = False
    self.snip = self.font.render('', True, (255, 255, 255))


    self.dialog = (charactersJSON["Characters"][f"{character}"]["dialog"])

    if "randomDialog" in charactersJSON["Characters"][f"{character}"]:
      self.randomDialog = (charactersJSON["Characters"][f"{character}"]["randomDialog"])
      self.activeRandomMessage = random.randint(0, len(self.randomDialog) - 1)
      self.randomDialog = self.randomDialog[self.activeRandomMessage]


    self.activeMessage = 0

    self.dialog = self.dialog[self.activeMessage]


    if self.animation:
      self._loadFromSheet(pathToAnimation, width, height, rows, cols)


    self.rect = self.idleImage.get_rect(topleft=(self.x, self.y))



    self.textRunning = False



  def update(self, keys, screen):
    if (keys[pg.K_e] == True):
      self.textRunning = True
      self.status = "active"


    if self.textRunning == True:
      self._drawDialog(screen)
     
    if self.textCompleted and keys[pg.K_e] == True:
      self.activeMessage += 1
      self._drawDialog(screen)
      self.textRunning = False


  def _drawDialog(self, screen):
    pg.draw.rect(screen, (20, 20, 60), [0, 700, 800, 500])
   
    if self.textCounter < self.textSpeed * len(self.dialog):
      self.textCounter += 1


    elif (self.textCounter >= self.textSpeed * len(self.dialog)):
      self.textCompleted = True


    self.snip = self.font.render(self.dialog[0: self.textCounter//self.textSpeed], True, (255, 255, 255))
    screen.blit(self.snip, (10, 710))


  def nextLine(self):
    global line


    line = (line + 1) % len(self.dialog)


  def draw(self, screen, scaledSize=None, camera=None):
    """Draws the character sprite on the screen. If the character has an animation, it will cycle through the animation frames. If not, it will display the idle image.

    Args:
        screen (_pg.display_): The Pygame display surface.
        scaledSize (_int_): The size (in px) to which the sprite should be scaled to. Defaults to None, which means no scaling will be applied.
        camera (_pg.Rect_, optional): The camera rectangle. Defaults to None.
    """

    if self.animation and self.status == "talking":
      rect = camera.apply(self.rect) if camera else self.rect
      screen.blit(self.idleImage, rect)
    
    elif self.animation and self.status == "notTalking":
      self._cycleAnimation(screen, scaledSize, camera)
    
    else:
      rect = camera.apply(self.rect) if camera else self.rect
      screen.blit(self.idleImage, rect)


  def _loadFromSheet(self, source, tileWidth, tileHeight, rows, cols):
    """Loads a spritesheet and slices it into individual frames.

    Args:
        source (str): The path to the spritesheet image.
        tileWidth (int): The width of each frame in the spritesheet.
        tileHeight (int): The height of each frame in the spritesheet.
        rows (int): The number of rows in the spritesheet.
        cols (int): The number of columns in the spritesheet.
    """

    self.sprites = []
    self.currentSprite = 0


    sheet = pg.image.load(source).convert_alpha()
    for row in range(rows):
      for col in range(cols):
        rect = pg.Rect(col * tileWidth, row * tileHeight, tileWidth, tileHeight)
        image = sheet.subsurface(rect)
        self.sprites.append(image)

  
  def _cycleAnimation(self, screen, scaledSize, camera=None):
    self.currentSprite += 1
    
    
    if self.currentSprite >= len(self.sprites):
      self.currentSprite = 0


    self.animatedImage = self.sprites[self.currentSprite]
    self.animatedImage = pg.transform.scale(self.animatedImage, (72, 72))

    rect = camera.apply(self.rect) if camera else self.rect
    screen.blit(self.animatedImage, rect)



  def printDebug(self, message):
    print(message)