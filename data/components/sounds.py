import pygame as pg

pg.mixer.init()

cave = pg.mixer.Sound("assets/sounds/music/themes/caveTheme.mp3")
sad = pg.mixer.Sound("assets/sounds/music/ambient/sad.wav")
daniel_prank_theme = pg.mixer.Sound("assets/sounds/music/themes/daniel_prank.mp3")
minigame_theme = pg.mixer.Sound("assets/sounds/music/themes/minigame.mp3")
news = pg.mixer.Sound("assets/sounds/music/themes/news.mp3")

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