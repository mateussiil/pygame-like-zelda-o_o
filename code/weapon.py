import pygame
import pygame.freetype
from debug import debug

from player import Player  # Import the freetype module.

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player: Player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        #graphic
        full_path = f'../graphics/weapons/{player.weapon}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        #placement
        
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16)) #type: ignore
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16)) #type: ignore
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0)) #type: ignore
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-15,0)) #type: ignore
