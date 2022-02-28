import pygame
from player import Player

class Magic(pygame.sprite.Sprite):
    def __init__(self, player: Player, style, strength, cost, groups):
        super().__init__(groups)
        direction = player.status.split('_')[0]
        print(direction)

        full_path = f'../graphics/particles/{style}/{style}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16)) #type: ignore

        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16)) #type: ignore
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16)) #type: ignore
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0)) #type: ignore
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-15,0)) #type: ignore
