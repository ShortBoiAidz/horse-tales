import pygame as pg

def init_assets():
  global  daniel_prank_theme, smirk_shot, sad, minigame_theme

  smirk_shot = pg.mixer.Sound("assets/sounds/sfx/smirk-shot.mp3")
  sad = pg.mixer.Sound("assets/sounds/music/ambient/sad.wav")
  daniel_prank_theme = pg.mixer.Sound("assets/sounds/music/themes/daniel_prank.mp3")
  minigame_theme = pg.mixer.Sound("assets/sounds/music/themes/minigame.mp3")