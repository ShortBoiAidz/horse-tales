import pygame as pg

class Player(pg.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.x = 500
    self.y = 500

    self.sprites_left = []
    self.sprites_right = []

    # Appending images
    self.sprites_left.append(pg.image.load("assets/textures/characters/player/walk1_left.png"))
    self.sprites_left.append(pg.image.load("assets/textures/characters/player/walk2_left.png"))

    self.sprites_right.append(pg.image.load("assets/textures/characters/player/walk1_right.png"))
    self.sprites_right.append(pg.image.load("assets/textures/characters/player/walk2_right.png"))
    #self.sprites_right.append(pg.image.load("assets/textures/characters/player/appa.png"))

    # Assigning images to sprites
    self.current_sprite = 0
    self.image = self.sprites_left[self.current_sprite]
    self.image = self.sprites_right[self.current_sprite]
    self.image = pg.transform.scale(self.image, (72, 72))
    self.rect = self.image.get_rect(center=(self.x, self.y))

  def update(self, keys):
    # LEFT movement
    if keys[pg.K_LEFT] or keys[pg.K_a] == True:
      self.x -= 10
      self.cycleSprites_left()

    # RIGHT movement
    elif keys[pg.K_RIGHT] or keys[pg.K_d] == True:
      self.x += 10
      self.cycleSprites_right()

    # UP movement
    elif keys[pg.K_UP] or keys[pg.K_w] == True:
      self.y -= 10
      self.cycleSprites_right()

    # DOWN movement
    elif keys[pg.K_DOWN] or keys[pg.K_s] == True:
      self.y += 10
      self.cycleSprites_left()

  def draw(self, screen):
    self.rect.topleft = (self.x, self.y)
    screen.blit(self.image, self.rect.topleft)

  def draw_hitbox(self, screen):
    pg.draw.rect(screen, (255, 0, 0), self.rect, 2)

  def cycleSprites_left(self):
    self.rect.topleft = (self.x, self.y)
    self.current_sprite += 1

    if self.current_sprite >= len(self.sprites_left):
      self.current_sprite = 0

    self.image = self.sprites_left[self.current_sprite]
    self.image = pg.transform.scale(self.image, (72, 72))

  def cycleSprites_right(self):
    self.rect.topleft = (self.x, self.y)
    self.current_sprite += 1

    if self.current_sprite >= len(self.sprites_right):
      self.current_sprite = 0

    self.image = self.sprites_right[self.current_sprite]
    self.image = pg.transform.scale(self.image, (72, 72))

  def printDebug(self):
    print(f"Player coords: {self.x}, {self.y}")