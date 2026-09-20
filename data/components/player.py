import pygame as pg

class Player:
  def __init__(self, image):
    self.x = 800 // 2
    self.y = 600 // 2
    self.image = pg.image.load(image)
    self.rect = self.image.get_rect(center=(self.x, self.y))
    self.lives = 3

  def update(self):
    for event in pg.event.get():
      if event.type == pg.KEYDOWN and event.type == pg.K_LEFT:
        self.image = pg.image.load("assets/textures/characters/player/walk1.png") # This doesnt really work

  def draw(self, screen):
    screen.blit(self.image, self.rect.topleft)