import pygame as pg
import random
import json
import sys

from libraries.PygameTkinterGUITools import *

#&====================================
'''
#* ABOUT:

This library is based around simplifying Adam Fox's "Pygame Tkinter GUI Tools" library.
Fox's PTGT is aimed at making game development easier by giving pre-built tools for developers to use.
I didn't really like how he vibe coded the whole thing so I made the library Just Enough Assets.
JEF simplifies Fox's vibe coded library and makes implementation a lot quicker and easier.

========================================================

#* INITALISING:
1. Import JEF using the following syntax in your Python file:
`from {module directory} import justEnoughAssets.py as jea`

2. Initialise the module in your `process_logic()` function using the following syntax:
`jea.init()`

3. You do not need to initalise in each module. As long as this runs through your `while` loop, everything should work fine.

4. You do need to import the module in each of your files though (obviously).

========================================================

#* HOW TO USE:

#* Labels
1. Use the `createLabel(a, b, c, d, e)` with the following params:
  a. scene
    i. For example: `menu` or `startScreen`
  b. text
    i. Self explanatory. If I need to tell you what "text" is, kill yourself.
  c. font size
    i. Same goes here. If you don't know what "font size" is, kill yourself.
  d. row
    i. The row on the Y axis. This sets it in place so other labels don't overlap.
    ii. For example: one label could be on row 1, meaning a label below it would be on row 2.
  e. padding on the Y axis
    i. The amount of space above and below the label

2. Putting `.draw()` at the end of initialising the label automatically draws it on screen.
  a. Handy, because it doesn't make you do `thisAwesomeCoolLabel.draw()` after initalising it.
  
#$suggestion: `createLabel(menu, "Horse Tale", 48, 0).draw()`

'''
#&====================================


#& ----------------------------------

def init():
  global keys

  keys = pg.key.get_pressed()

#& ----------------------------------

#* Label Creation
class createLabel():
  def __init__(self, scene, text, fontSize, row, yPadding=20):
    """Creates a label using Pygame Tkinter Gui Tools but makes it a little easier to read and write. Kind of just an extra layer of maintainability.

    Args:
        scene (str): The scene to which the label belongs. E.g. "menu" or "game"
        text (str): The text to display on the label
        fontSize (int): The size of the font for the label
        row (int): The row position of the label
        yPadding (int, optional): Padding on the Y-axis. Defaults to 20.
    """

    self.scene = scene
    self.text = text
    self.font_size = fontSize
    self.row = row
    self.padY = yPadding


  def draw(self):
    Label(self.scene, text=self.text, font_size=self.font_size).grid(row=self.row, column=0, pady=(0, self.padY))


#& ----------------------------------

#* Character Creation

class Character(pg.sprite.Sprite):
  def __init__(self, character, x, y, pathToImg=None, animation=False, pathToAnimation=None, width=None, height=None, rows=None, cols=None, allowJSON=False, pathToJSON=None, speakingSound=None):
    """Creates a character sprite with dialog functionality if "e" is pressed. Allows for customization of the character's dialog through JSON files. See documentation for required JSON structure.

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
        speakingSound (_str_): The file for the character's voice when they speak.
    """
    global characters, charactersJSON

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
    self.speakingFile = speakingSound
    self.interactionTarget = None
    self.interactionRange = 100


    self.textCounter = 0
    self.textSpeed = 1
    self.textCompleted = False
    self.snip = self.font.render('', True, (255, 255, 255))


    self.dialog = (charactersJSON["Characters"][f"{character}"]["dialog"])

    if allowJSON:
      self._loadJSON(character, charactersJSON)


    self.activeMessage = 0
    self.e_wasPressed = False


    if self.animation:
      self._loadFromSheet(pathToAnimation, width, height, rows, cols)

    self.rect = self.idleImage.get_rect(topleft=(self.x, self.y))

    self.textRunning = False


  def _loadJSON(self, character, charactersJSON):
    if "randomDialog" in charactersJSON["Characters"][f"{character}"]:
      self.randomDialog = (charactersJSON["Characters"][f"{character}"]["randomDialog"])
      self.activeRandomMessage = random.randint(0, len(self.randomDialog) - 1)
      self.randomDialog = self.randomDialog[self.activeRandomMessage]


  def update(self, screen, tick):
    """Detects if the 'toggleDialog' key is pressed. If true, runs the dialog until the 'toggleDialog' key is pressed again.

    Args:
        screen (_pygame.display_): Pygame's display
        tick (_int_): _Frame rate of the game_
    """

    e_pressed = keys[pg.K_e]

    e_justPressed = e_pressed and not self.e_wasPressed

    self.e_wasPressed = e_pressed

    playerNearby = (
      self.interactionTarget is not None
      and pg.Vector2(self.rect.center).distance_to(self.interactionTarget.rect.center) <= self.interactionRange
    )
    #note^ Detects if the player less than or greater to the interaction range (20)px

    if e_justPressed:
      self._playerNearby(playerNearby)

    if self.textRunning:
      self._drawDialog(screen)


  def _playerNearby(self, playerNearby):
    if self.textRunning and self.textCompleted:
            self.nextLine()
    
    elif not self.textRunning and self.dialog and playerNearby:
      self.activeMessage = 0
      self.textCounter = 0
      self.textCompleted = False
      self.textRunning = True
      self.status = "talking"


  def _drawDialog(self, screen):
    pg.draw.rect(screen, (20, 20, 60), [0, 700, 800, 500])
    dialog = self.dialog[self.activeMessage]

    if self.textCounter < self.textSpeed * len(dialog):
      self.textCounter += 1
      self._playSpeakingSound()


    elif self.textCounter >= self.textSpeed * len(dialog):
      self.textCompleted = True


    self.snip = self.font.render(dialog[0: self.textCounter//self.textSpeed], True, (255, 255, 255))
    screen.blit(self.snip, (10, 710))

  def _playSpeakingSound(self):
    if self.speakingFile is not None:
      pg.mixer.Sound(self.speakingFile).play()


  def nextLine(self):
    if self.activeMessage + 1 < len(self.dialog):
      self.activeMessage += 1
      self.textCounter = 0
      self.textCompleted = False
    else:
      self.textRunning = False
      self.status = "notTalking"
      self.textCounter = 0
      self.textCompleted = False


  def draw(self, screen, scaledSize=None, camera=None):
    """Draws the character sprite on the screen. If the character has an animation, it will cycle through the animation frames in the linked spritesheet. If not, it will display the idle image.

    Args:
        screen (_pg.display_): The Pygame display surface.
        scaledSize (_int_): The size (in px) to which the sprite should be scaled to. Defaults to None, which means no scaling will be applied.
        camera (_pg.Rect_, optional): The camera rectangle. Defaults to None.
    """

    if camera is None and hasattr(scaledSize, "apply"):
      camera = scaledSize

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


#& ----------------------------------

#* Map Creation

class Map():
  def __init__(self, TMXfile, playerObject, ySort=False):
    """Creates a map object using a TMX file. Reads the TMX file and sorts components based on their Y value relative to the player object.

    Args:
        TMXfile (_str_): _Path to the map's TMX file_.
        playerObject (_str_): _The object of the player. E.g. playerModule.PlayerClass()_.
        ySort (bool, optional): _Determines if the map's components will be sorted based on their Y value relative to the player object_. Defaults to False.
    """

    global world, camera, zoom_camera, body, walls, map, ground, speed, playerSprite, playerObj

    SPEED = 100

    map = TiledMap(TMXfile)
    walls = [obj["rect"] for obj in map.collision_objects]

    playerObj = playerObject
    playerSprite = playerObj.playerSprite

    for layer in map.tmx.layers:
      if getattr(layer, "class", "").lower() != "collision":
        continue

      walls.extend(
        pg.Rect(
          x * map.tilewidth,
          y * map.tileheight,
          map.tilewidth,
          map.tileheight,
        )

        for y, row in enumerate(layer.data)
        for x, gid in enumerate(row)
        if gid
      )

    body = TopDownBody(
      playerSprite,
      solids=walls,
      speed=SPEED,
      hitbox=(12, 10),
      hitbox_offset=(0, -2),
    )
    body.hitbox_rect


    camera = Camera(map.width, map.height, (800, 800))
    zoom_camera = ZoomCamera(camera, (800, 800), zoom=1.5)
    camera.follow(playerSprite)
    zoom_camera.snap()


    world = World(map, camera, y_sort=ySort)
    world.add_sprite(playerSprite)


    ground = map.tile_properties_at(body.hitbox_rect.center)
    speed = SPEED * ground.get("speed", 1)


  def update(self, screen, tick):
    """Updates the player on the map


    Args:
        screen (pygame.display.surface()): The surface basically passing through a heap of stuff
        tick (integer): Tick rate of pygame's _Clock()_ (FPS)
    """
    dx = (keys[pg.K_RIGHT] or keys[pg.K_d]) - (keys[pg.K_LEFT] or keys[pg.K_a])
    dy = (keys[pg.K_DOWN] or keys[pg.K_s]) -( keys[pg.K_UP] or keys[pg.K_w])


    body.move(dx, dy, speed)
    body.update(tick)
    map_bounds = pg.Rect(0, 0, map.width, map.height)
    bounded_position = playerSprite.rect.clamp(map_bounds).topleft

    if bounded_position != playerSprite.rect.topleft:
      body.set_position(*bounded_position)
      
    playerObj.x, playerObj.y = playerSprite.rect.topleft
    playerObj.cycleSprites(bool(dx or dy))
    world.update(screen, tick)
    zoom_camera.update(tick)


  def add_sprite(self, *sprites):
    world.add_sprite(*sprites)


  def drawMap(self, screen):
    zoom_camera.draw_world(world, screen)


    if Debug.on:
      body.draw_debug(screen, zoom_camera)
      for wall in walls:
        pg.draw.rect(screen, (255, 0, 0), zoom_camera.apply(wall), 1)