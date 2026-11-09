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

#& ================================================

def init():
  global keys

  keys = pg.key.get_pressed()

#& ================================================

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


#& ================================================

#* Character Creation

class Character(pg.sprite.Sprite):
  def __init__(self, character, x, y, pathToImg=None, animation=False, pathToAnimation=None, width=None, height=None, rows=None, cols=None, allowJSON=False, pathToJSON=None, speakingSound=None, themeMusic=None, themeMusicVolume=0.7):
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
        themeMusic (_str_): The character's theme that plays when they're speaking.
        themeMusicVolume (_float_): Self explainatory. If I need to explain what this means, kill yourself.
    """
    global characters, charactersJSON

    with open(pathToJSON, "r") as characters:
      charactersJSON = json.load(characters)


    super().__init__()

    #* Inputted variables
    self.character = character
    self.animation = animation
    self.speakingFile = speakingSound
    self.x = x
    self.y = y


    #* Initialising
    self.proximity = Proximity(self, self.rect.center)
    self.rect = self.idleImage.get_rect(topleft=(self.x, self.y))
    
    if allowJSON:
      self._loadJSON(character, charactersJSON)
    
    if self.animation:
      self._loadFromSheet(pathToAnimation, width, height, rows, cols)

    
    #* Images
    self.idleImage = pg.image.load(pathToImg + "/idle.png")
    self.idleImage = pg.transform.scale(self.idleImage, (72, 72))


    #* Font
    pg.font.init()
    self.font = pg.font.Font('freesansbold.ttf', 24)


    #* Dialog shit
    self.status = "notTalking"
    self.dialog = (charactersJSON["Characters"][f"{character}"]["dialog"])
    
    self.activeMessage = 0
    self.textCounter = 0
    self.textSpeed = 1
    self.textCompleted = False
    self.textRunning = False
    
    self.snip = self.font.render('', True, (255, 255, 255))
    self.e_wasPressed = False


    #* Music
    self.themeMusicFile = themeMusic
    self.themeMusicChannel = None
    self.themeMusicVolume = themeMusicVolume

#&--------------------------------------------------------

  def _loadJSON(self, character, charactersJSON):
    if "randomDialog" in charactersJSON["Characters"][f"{character}"]:
      self.randomDialog = (charactersJSON["Characters"][f"{character}"]["randomDialog"])
      self.activeRandomMessage = random.randint(0, len(self.randomDialog) - 1)
      self.randomDialog = self.randomDialog[self.activeRandomMessage]

#&--------------------------------------------------------

  def update(self, screen, tick, player=None):
    """Detects if the 'toggleDialog' key is pressed. If true, runs the dialog until the 'toggleDialog' key is pressed again.

    Args:
        screen (_pygame.display_): Pygame's display
        tick (_int_): _Frame rate of the game_
    """

    e_pressed = keys[pg.K_e]
    e_justPressed = e_pressed and not self.e_wasPressed
    self.e_wasPressed = e_pressed


    if e_justPressed:
      self._detectTextStatus(player)

    if self.textRunning:
      self._drawDialog(screen)

#&--------------------------------------------------------

#* Dialog
  def _drawDialog(self, screen):
    dialog = self.dialog[self.activeMessage]

    if self.textCounter < self.textSpeed * len(dialog):
      self.textCounter += 1
      self._playSpeakingSound()


    elif self.textCounter >= self.textSpeed * len(dialog):
      self.textCompleted = True


    visibleText = dialog[0: self.textCounter // self.textSpeed]
    lines = self._wrapDialogText(visibleText, screen.get_width() - 20)
    lineHeight = self.font.get_linesize()
    padding = 10
    panelHeight = min(screen.get_height(), max(100, len(lines) * lineHeight + padding * 2))
    panelTop = screen.get_height() - panelHeight
    #note^ Not mine. Stole this from a guy on stackoverflow. Don't know what's going on here but it works so I'll leave it

    pg.draw.rect(screen, (20, 20, 60), (0, panelTop, screen.get_width(), panelHeight))

    for lineIndex, line in enumerate(lines):
      self.snip = self.font.render(line, True, (255, 255, 255))
      screen.blit(self.snip, (padding, panelTop + padding + lineIndex * lineHeight))


  def _detectTextStatus(self, player):
    if self.textRunning and self.textCompleted:
      self._nextLine()
    elif not self.textRunning and self.dialog and self.proximity is not None:
      self.proximity.interact(player)


  def _startDialog(self):
    self.activeMessage = 0
    self.textCounter = 0
    self.textCompleted = False
    self.textRunning = True
    self.status = "talking"
    self._detectThemeMusic()

  
  def _nextLine(self):
    if self.activeMessage + 1 < len(self.dialog):
      self.activeMessage += 1
      self.textCounter = 0
      self.textCompleted = False
    else:
      self.textRunning = False
      self.status = "notTalking"
      self.textCounter = 0
      self.textCompleted = False
      self._fadeoutThemeMusic()


  def _wrapDialogText(self, text, maxWidth):
    lines = []

    for paragraph in text.split("\n"):
      line = ""
      for word in paragraph.split():
        candidate = word if not line else f"{line} {word}"
        if self.font.size(candidate)[0] <= maxWidth:
          line = candidate
          continue

        if line:
          lines.append(line)
          line = ""

        while word and self.font.size(word)[0] > maxWidth:
          splitAt = 1
          while splitAt < len(word) and self.font.size(word[:splitAt + 1])[0] <= maxWidth:
            splitAt += 1
          lines.append(word[:splitAt])
          word = word[splitAt:]
        line = word

      lines.append(line)

    return lines
  #note^ Also not mine. The nesting is fucking horrible

#&--------------------------------------------------------

#* Theme music
  def _playSpeakingSound(self):
    if self.speakingFile is not None:
      pg.mixer.Sound(self.speakingFile).play()


  def _detectThemeMusic(self):
    if self.themeMusicFile:
      self._detectIfThemeIsPlayable()


  def _detectIfThemeIsPlayable(self): #?query Any other names for this?? It fucking sucks
    pg.mixer.music.load(self.themeMusicFile)
    pg.mixer.music.set_volume(self.themeMusicVolume)
    pg.mixer.music.play(loops=-1, fade_ms=500)


  def _fadeoutThemeMusic(self):
    pg.mixer.music.fadeout(800)

#&--------------------------------------------------------

#* Draw
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

#&--------------------------------------------------------

#* Spritesheet
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

    while self.sprites and not self.sprites[-1].get_bounding_rect():
      self.sprites.pop()

#&--------------------------------------------------------
  
#* Animation
  def _cycleAnimation(self, screen, scaledSize, camera=None):
    self.animatedImage = self.sprites[self.currentSprite]
    self.animatedImage = pg.transform.scale(self.animatedImage, (72, 72))

    rect = camera.apply(self.rect) if camera else self.rect
    screen.blit(self.animatedImage, rect)
    self.currentSprite = (self.currentSprite + 1) % len(self.sprites)

#&--------------------------------------------------------

#* Debug
  def printDebug(self, message):
    print(message)


#& ================================================

#* Proximity control

class Proximity():
  def __init__(self, character, coordinates=None, interactionRange=100, player=None):
    """__init__ Initialises the proximity control. Detects if the player object is nearby.

    Args:
        character (_str_): _Character object (the one that has the dialog)_
        coordinates (_int_, optional): _Coordinates of the character's rect/hitbox_. Defaults to None.
        interactionRange (int, optional): _Distance (in px) for the proximity to apply_. Defaults to 100.
        player (_str_): _The player object. Used for detecting proximity_. Defaults to none.
    """
    self.character = character
    self.coordinates = pg.Vector2(coordinates if coordinates is not None else character.rect.center)
    self.interactionRange = interactionRange
    self.player = player

#&--------------------------------------------------------

#* Detects if the player is nearby
  def isNear(self, player):
    if player is None:
      return False

    playerPosition = player.rect.center if hasattr(player, "rect") else player

    return self.coordinates.distance_to(pg.Vector2(playerPosition)) <= self.interactionRange
    #@temp Really not happy with 2 return statements

  def interact(self, player=None):
    player = player if player is not None else self.player
    if not self.isNear(player) or not self.character.dialog:
      return False

    self.character._startDialog()
    return True


#& ================================================

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