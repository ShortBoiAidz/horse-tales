import pygame as pg
from libraries.PygameTkinterGUITools import *

pg.mixer.init()

#& ----------------------------------

def stopSounds():
  pg.mixer.stop()

class Sound():
  def __init__(self, path, name):
    self.track = pg.mixer.Sound(f"assets/sounds/{path}/{name}.wav")

  def play(self):
    self.track.play(loops=-1, fade_ms=3000)
    self.track.set_volume(0.5)

#&============================================================

class AmbientSound(Sound):
  def __init__(self, name):
    super().__init__("ambient", name)

class ThemeSound(Sound):
  def __init__(self, name):
    super().__init__("music/themes", name)

class SFXSound(Sound):
  def __init__(self, name):
    super().__init__("sfx", name)

  def play(self):
    self.track.play(loops=0, fade_ms=0)