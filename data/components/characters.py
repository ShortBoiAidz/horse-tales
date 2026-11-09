import json
import pygame as pg
import random


from data.components import sounds
from data.states import mapstates
from libraries import justEnoughAssets as jea

#& ----------------------------------

with open("data/characters.json", "r") as characters:
    charactersJSON = json.load(characters)

screen = pg.display.set_mode([800, 800])


#& ----------------------------------

class RenderCharacters():
  def __init__(self) :
    self.Prank = self.danielPrank = jea.Character(
                                    character="danielPrank",
                                    x=560, y=147,
                                    pathToImg="assets/textures/characters/danielPrank",
                                    allowJSON=True,
                                    pathToJSON="data/characters.json",
                                    speakingSound=None,
                                    themeMusic="assets/sounds/music/themes/danielPrank_theme.wav",
                                    themeMusicVolume=1.5
                                    )

    self.bartenderObj = jea.Character(
                                    character="bartender",
                                    x=310, y=170,
                                    pathToImg="assets/textures/characters/bartender",
                                    animation=True,
                                    pathToAnimation="assets/textures/characters/bartender/animation/bartenderActive_spritesheet.png",
                                    width=33, height=33,
                                    rows=3, cols=4,
                                    allowJSON=True,
                                    pathToJSON="data/characters.json",
                                    speakingSound="assets/sounds/sfx/bartender_voice.wav"
                                    )

  def drawCharacters(self, screen):
    self.bartenderObj.draw(screen, scaledSize=72)
    self.danielPrank.draw(screen, scaledSize=72)
  
  def updateCharacters(self, screen, tick, player=None):
    self.danielPrank.update(screen, tick, player)
    self.bartenderObj.update(screen, tick, player)

#& ----------------------------------