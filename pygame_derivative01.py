# Hide the welcome message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import numpy

screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
W, H = screen.get_size()

# It’s going to be less than 60 times a second anyway, so why is it so verbose?
# Let's return to the Zen of Python.
def events():
  raw = pygame.event.get()
  ret = []
  for event in raw:
    if event.type == pygame.QUIT:
        ret.append(('quit',0))
    elif event.type == pygame.KEYDOWN:
        ret.append(('keydown', event.key))
    elif event.type == pygame.KEYUP:
        ret.append(('keyup', event.key))
    elif event.type == pygame.MOUSEMOTION:
        ret.append(('mousemove', event.pos)) # refer to js
    elif event.type == pygame.MOUSEBUTTONUP:
        ret.append(('mouseup', event.button))
    elif event.type == pygame.MOUSEBUTTONDOWN:
        ret.append(('mousedown', event.button))
  return ret
