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

class Smirk:
  def __init__(self):
    self.image = pg.image.load("assets/textures/characters/carleighe_smirk/idle.png")
    self.image_shot = pg.image.load("assets/textures/characters/carleighe_smirk/shot.png")
    self.x = 700 // 2
    self.y = 500 // 2

  def draw(self, screen):
    sounds.stopSounds()
    sounds.newsSound()
    screen.blit(self.image, (self.x, self.y))

  def draw_shot(self, screen):
    sounds.stopSounds()
    sounds.smirkShotSound()
    screen.blit(self.image_shot, (self.x, self.y))
    pg.time.delay(1000)
    sounds.sadSound()

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
    print(voicelines[random.randint(0, 5)])