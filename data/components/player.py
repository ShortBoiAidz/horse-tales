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

    # Assigning images to sprites
    self.current_sprite = 0
    self.image = self.sprites_left[self.current_sprite]
    self.image = self.sprites_right[self.current_sprite]
    self.image = pg.transform.scale(self.image, (128, 128))
    self.rect = self.image.get_rect(center=(self.x, self.y))

  def update(self, keys):
    # LEFT movement
    if keys[pg.K_LEFT] or keys[pg.K_a] == True:
      self.x -= 10
      self.rect = self.image.get_rect(center=(self.x, self.y))
      self.current_sprite += 1

      if self.current_sprite >= len(self.sprites_left):
        self.current_sprite = 0

      self.image = self.sprites_left[self.current_sprite]
      self.image = pg.transform.scale(self.image, (128, 128))

    # RIGHT movement
    elif keys[pg.K_RIGHT] or keys[pg.K_d] == True:
      self.x += 10
      self.rect = self.image.get_rect(center=(self.x, self.y))
      self.current_sprite += 1

      if self.current_sprite >= len(self.sprites_right):
        self.current_sprite = 0

      self.image = self.sprites_right[self.current_sprite]
      self.image = pg.transform.scale(self.image, (128, 128))

    # UP movement
    elif keys[pg.K_UP] or keys[pg.K_w] == True:
      self.y -= 10
      self.rect = self.image.get_rect(center=(self.x, self.y))
      self.current_sprite += 1

      if self.current_sprite >= len(self.sprites_right):
        self.current_sprite = 0

      self.image = self.sprites_right[self.current_sprite]
      self.image = pg.transform.scale(self.image, (128, 128))

    # DOWN movement
    elif keys[pg.K_DOWN] or keys[pg.K_s] == True:
      self.y += 10
      self.rect = self.image.get_rect(center=(self.x, self.y))
      self.current_sprite += 1

      if self.current_sprite >= len(self.sprites_left):
        self.current_sprite = 0

      self.image = self.sprites_left[self.current_sprite]
      self.image = pg.transform.scale(self.image, (128, 128))

  def draw(self, screen):
    screen.blit(self.image, self.rect.topleft)