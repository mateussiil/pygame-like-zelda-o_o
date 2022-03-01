from dis import dis
from support import import_folder
from entity import Entity
from player import Player
from settings import *
import pygame

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites ):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # movement
        self.rect: pygame.rect.Rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        self.monster_name = monster_name
        monster_info = monsters_data[self.monster_name]
        self.speed =  monster_info['speed']
        self.health =  monster_info['health']
        self.exp =  monster_info['exp']
        self.attack_damage =  monster_info['damage']
        self.resistence =  monster_info['resistence']
        self.attack_radius =  monster_info['attack_radius']
        self.notice_radius =  monster_info['notice_radius']
        self.attack_type =  monster_info['attack_type']

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': [] }
        main_path = f'../graphics/monsters/{name}'

        for animation in self.animations.keys():
            full_path = main_path + '/' + animation
            self.animations[animation] = import_folder(full_path)
    