import pygame as pg
from PygameTkinterGUITools import *


class Player(pg.sprite.Sprite):
  def __init__(self):
    super().__init__()


    self.playerAnimator = Animator(
                                  "assets/textures/characters/player/spritesheet.png",
                                   from_sheet=True,
                                   tile_width=20,
                                   tile_height=42,
                                   rows=1, cols=5,
                                   scale=1.2
                                   )


    self.playerAnimator.add_animation("idle", [(0, 2)])
    self.playerAnimator.add_animation("walk", [(0, 3), (0, 4)])




    self.x = 170
    self.y = 170
    self.speed = 10


    self.playerSprite = SpriteObject(self.x, self.y, animator=self.playerAnimator)
    self.playerSprite.move(20, 0)


    self.playerAnimator.play("idle")


    self.facingLeft = False


  def update(self, keys, tick):
    """Updates the player movement


    Args:
        keys (bool): Returns a boolean if a detected key is pressed
        tick (integer): Tick rate of pygame's _Clock()_ (FPS)
    """


    left = keys[pg.K_LEFT] or keys[pg.K_a]
    right = keys[pg.K_RIGHT] or keys[pg.K_d]
    up = keys[pg.K_UP] or keys[pg.K_w]
    down = keys[pg.K_DOWN] or keys[pg.K_s]


    if left:
      self.x -= self.speed * tick / 1000
      self.facingLeft = True


    elif right:
      self.x += self.speed * tick / 1000
      self.facingLeft = False


    elif up:
      self.y -= self.speed


    elif down:
      self.y += self.speed


    if down and left:
      self.y += self.speed // 3
      self.x -= self.speed // 3
    elif down and right:
      self.y += self.speed // 3
      self.x += self.speed // 3
    elif up and left:
      self.y -= self.speed // 3
      self.x -= self.speed // 3
    elif up and right:
      self.y -= self.speed // 3
      self.x += self.speed // 3


    self.cycleSprites(left or right or up or down)


  def draw(self, screen):
    self.playerAnimator.draw(screen)


  def drawHitbox(self, screen):
    pg.draw.rect(screen, (255, 0, 0), self.rect, 2)


  def cycleSprites(self, moving):
    if moving:
      self.playerAnimator.play("walk")
    else:
      self.playerAnimator.play("idle")


  def printDebug(self):
    print(f"Player coords: ({self.x}, {self.y})")
