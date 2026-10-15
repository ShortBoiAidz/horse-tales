import pygame as pg
from PygameTkinterGUITools import *

pg.mixer.init()

cave = pg.mixer.Sound("assets/sounds/music/themes/wow_magic.mp3")
sad = pg.mixer.Sound("assets/sounds/music/ambient/sad.wav")
daniel_prank_theme = pg.mixer.Sound("assets/sounds/music/themes/daniel_prank.mp3")
minigame_theme = pg.mixer.Sound("assets/sounds/music/themes/minigame.mp3")
news = pg.mixer.Sound("assets/sounds/music/themes/news.mp3")
bar = pg.mixer.Sound("assets/sounds/music/themes/long_face.wav")

def stopSounds():
  pg.mixer.stop()

def sadTheme():
  sad.play()

def danielPrankTheme():
  daniel_prank_theme.play()

def newsTheme():
  news.play()

def caveTheme():
  cave.play()

def barTheme():
  bar.play(loops=-1, fade_ms=3000)
  bar.set_volume(0.5)