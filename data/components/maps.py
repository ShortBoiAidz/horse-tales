import pygame as pg
from pytmx.util_pygame import load_pygame as lpg
from PygameTkinterGUITools import *

from data.states import mapstates
from data.components import player

SPEED = 200

class Bar():
  def __init__(self):
    global world, camera, zoom_camera, playerObj, body, walls, bar, playerSprite

    playerObj = player.Player()
    playerSprite = playerObj.playerSprite

    bar = TiledMap("assets/textures/mapsheets/bar.tmx")
    walls = [obj["rect"] for obj in bar.collision_objects]
    body = TopDownBody(playerSprite, solids=walls, speed=SPEED, hitbox=10)
    body.hitbox_rect

    camera = Camera(bar.width, bar.height, (800, 800))
    zoom_camera = ZoomCamera(camera, (800, 800), zoom=1.5)

    world = World(bar, camera, y_sort=False)
    world.add_sprite(playerSprite)

  def update(self, tick):
    keys = pg.key.get_pressed()
  
    ground = bar.tile_properties_at(body.hitbox_rect.center)
    speed = SPEED * ground.get("speed", 1)

    dx = keys[pg.K_RIGHT] - keys[pg.K_LEFT]
    dy = keys[pg.K_DOWN] - keys[pg.K_UP]

    body.move(dx, dy, speed)
    body.update(tick)
    world.update(tick)
    camera.follow(playerObj)
    #zoom_camera.update(tick)

  def drawMap(self, screen):
    zoom_camera.draw_world(world, screen)

    if Debug.on:
      body.draw_debug(screen, zoom_camera)
      for wall in walls:
        pg.draw.rect(screen, (255, 0, 0), zoom_camera.apply(wall), 1)
# ----------------------------------