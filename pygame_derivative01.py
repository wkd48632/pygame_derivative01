import os
# Hide the welcome message
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import numpy

screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
