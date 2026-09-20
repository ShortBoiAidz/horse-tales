import pygame as pg

pg.mixer.init()

smirk_shot = pg.mixer.Sound("assets/sounds/sfx/smirk-shot.mp3")
sad = pg.mixer.Sound("assets/sounds/music/ambient/sad.wav")
daniel_prank_theme = pg.mixer.Sound("assets/sounds/music/themes/daniel_prank.mp3")
minigame_theme = pg.mixer.Sound("assets/sounds/music/themes/minigame.mp3")
newsTheme = pg.mixer.Sound("assets/sounds/music/themes/news.mp3")

def stopSounds():
  pg.mixer.stop()

def smirkShotSound():
  smirk_shot.play()

def sadSound():
  sad.play()

def danielPrankSound():
  daniel_prank_theme.play()

def newsSound():
  newsTheme.play()