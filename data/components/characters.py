import pygame as pg

from data.components import sounds

import random

class Prank:
  def __init__(self):
    self.image = pg.image.load("assets/textures/characters/daniel_prank/idle.png")
    self.x = 700 // 2
    self.y = 500 // 2

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))
    sounds.stopSounds()
    sounds.danielPrankSound()

class Rooster:
  def __init__(self):
    self.image = pg.image.load("assets/textures/characters/riley_rooster/idle.png")
    self.x = 0
    self.y = 0

class Bartender:
  def __init__(self):
    self.image = pg.image.load("assets/textures/characters/bartender/idle.png")
    self.x = 360
    self.y = 390

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))
    self.image = pg.transform.scale(self.image, (72, 72))

  def dialog(screen):
    font = pg.font.SysFont("Comic Sans MS", 20)
    text_y = 530
    text_x = 500

    voicelines = [
      "Last night, there was a fire in the Bronx last night that killed people during the fire last night in the Bronx. They say they died due to the fire being too hot for their bodies. Bummer.",
      "An unknown killer is loose in the town. For your own safety, stay inside and do not trust anyone.",
      "My friend Bart says pasta isn't real. I told him that he's just thinking of 'Italian' people.",
      "This is unrelated to any events, but I talked to my good friend Bart about his views on pineapples. He believes they aren't real. What an idiot.",
      "Funny how pineapples are so unrelated to coffee."
    ]

    newsLabel = font.render(voicelines[random.randint(0, 4)], True, (255, 0, 0))

    pg.draw.rect(screen, (255, 255, 255), (0, 500, 800, 100))

    screen.blit(newsLabel, (text_x, text_y))