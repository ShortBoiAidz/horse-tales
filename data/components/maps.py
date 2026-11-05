import pygame as pg
from pytmx.util_pygame import load_pygame as lpg
from libraries.PygameTkinterGUITools import *


from data.states import mapstates
from data.components import player
from libraries.justEnoughAssets import *


#& ----------------------------------


SPEED = 100
ORANGE = "#C24E00"


#& ----------------------------------


class TitleScreen():
  def __init__(self, screen):
    global menu, currentMapObj

    menu = Root(screen, bg=f"{ORANGE}", padding=300)
    menu.columnconfigure(0, weight=1)

    currentMapObj = mapstates.currentMap()

    createLabel(menu, "Horse Tale", 48, 0).draw()
    
    playButton = Button(menu, text="Start Game", command=lambda: self.changeMapstate())
    playButton.grid(row=1, column=0, pady=(0, 10))
    
    createLabel(menu, "Code by ShortBoiAidz \n Music by Helo and 1empted \n Maps by TeejMeister22", 24, 2).draw()


  def drawMap(self, screen):
    menu.draw(screen)


  def changeMapstate(self):
    currentMapObj.mapstate = "bar"



class Bar():
  def __init__(self):
    global world, camera, zoom_camera, playerObj, body, walls, bar, playerSprite, ground, speed


    playerObj = player.Player()
    playerSprite = playerObj.playerSprite


    bar = TiledMap("assets/textures/mapsheets/bar.tmx")
    walls = [obj["rect"] for obj in bar.collision_objects]

    for layer in bar.tmx.layers:
      if getattr(layer, "class", "").lower() != "collision":
        continue

      walls.extend(
        pg.Rect(
          x * bar.tilewidth,
          y * bar.tileheight,
          bar.tilewidth,
          bar.tileheight,
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


    camera = Camera(bar.width, bar.height, (800, 800))
    zoom_camera = ZoomCamera(camera, (800, 800), zoom=1.5)
    camera.follow(playerSprite)
    zoom_camera.snap()


    world = World(bar, camera, y_sort=False)
    world.add_sprite(playerSprite)


    ground = bar.tile_properties_at(body.hitbox_rect.center)
    speed = SPEED * ground.get("speed", 1)


  def update(self, tick, keys):
    """Updates the player on the _Bar_ map


    Args:
        tick (integer): Tick rate of pygame's _Clock()_ (FPS)
        keys (bool): Returns a boolean if a detected key is pressed
    """
    dx = keys[pg.K_RIGHT] - keys[pg.K_LEFT]
    dy = keys[pg.K_DOWN] - keys[pg.K_UP]


    body.move(dx, dy, speed)
    body.update(tick)
    map_bounds = pg.Rect(0, 0, bar.width, bar.height)
    bounded_position = playerSprite.rect.clamp(map_bounds).topleft
    if bounded_position != playerSprite.rect.topleft:
      body.set_position(*bounded_position)
    playerObj.x, playerObj.y = playerSprite.rect.topleft
    playerObj.cycleSprites(bool(dx or dy))
    world.update(tick)
    zoom_camera.update(tick)


  def add_sprite(self, *sprites):
    world.add_sprite(*sprites)


  def drawMap(self, screen):
    zoom_camera.draw_world(world, screen)


    if Debug.on:
      body.draw_debug(screen, zoom_camera)
      for wall in walls:
        pg.draw.rect(screen, (255, 0, 0), zoom_camera.apply(wall), 1)
#& ----------------------------------
