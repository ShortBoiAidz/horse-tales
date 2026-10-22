import pygame as pg
from PygameTkinterGUITools import *

class Player(pg.sprite.Sprite):
  def __init__(self):
    super().__init__()
    
    self.playerAnimator = Animator("assets/textures/characters/player/spritesheet.png", from_sheet=True, tile_width=20, tile_height=21, rows=1, cols=5, scale=2)

    self.playerAnimator.add_animation("idle", [(2, 3)])
    self.playerAnimator.add_animation("walk", [(2, 4), (2, 5)])

    self.playerSprite = SpriteObject(100, 100, image="assets/textures/characters/player/idle.png")
    self.playerSprite.move(20, 0)

    self.x = 250
    self.y = 230
    self.speed = 10

    self.playerAnimator.play("idle")

    self.facingLeft = False

  def update(self, keys, tick):
    global moving, animatedPlayerImage

    moving = False

    if keys[pg.K_LEFT] or keys[pg.K_a] == True:
      self.x -= self.speed * tick / 1000
      self.facingLeft = True
      moving = True
      self.cycleSprites()

    elif keys[pg.K_RIGHT] or keys[pg.K_d] == True:
      self.x += self.speed * tick / 1000
      self.facingLeft = False
      moving = True
      self.cycleSprites()

    elif keys[pg.K_UP] or keys[pg.K_w] == True:
      self.y -= self.speed
      self.cycleSprites()

    elif keys[pg.K_DOWN] or keys[pg.K_s] == True:
      self.y += self.speed
      self.cycleSprites()

    if keys[pg.K_DOWN] and keys[pg.K_LEFT] or keys[pg.K_s] and keys[pg.K_a] == True:
      self.y += self.speed // 3
      self.x -= self.speed // 3
      self.cycleSprites()
 
    elif keys[pg.K_DOWN] and keys[pg.K_RIGHT] or keys[pg.K_s] and keys[pg.K_d] == True:
      self.y += self.speed // 3
      self.x += self.speed // 3
      self.cycleSprites()
 
    elif keys[pg.K_UP] and keys[pg.K_LEFT] or keys[pg.K_w] and keys[pg.K_a] == True:
      self.y -= self.speed // 3
      self.x -= self.speed // 3
      self.cycleSprites()
 
    elif keys[pg.K_UP] and keys[pg.K_RIGHT] or keys[pg.K_w] and keys[pg.K_d] == True:
      self.y -= self.speed // 3
      self.x += self.speed // 3
      self.cycleSprites()

    animatedPlayerImage = self.playerAnimator.update(tick, flip_x=self.facingLeft)

  def draw(self, screen):
    self.playerAnimator.draw(screen)

  def drawHitbox(self, screen):
    pg.draw.rect(screen, (255, 0, 0), self.rect, 2)

  def cycleSprites(self):
    if not self.playerAnimator.busy:
        if moving:
            self.playerAnimator.play("walk")
        else:
            self.playerAnimator.play("idle")

  def drawAnimation(self, screen):
    screen.blit(animatedPlayerImage, animatedPlayerImage.get_rect(midbottom=(self.x, 455)))

  def printDebug(self):
    print(f"Player coords: ({self.x}, {self.y})")