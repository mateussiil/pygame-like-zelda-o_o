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
    
    def get_player_distance_direction(self, player: Player):
        #study vector, distance, amplitude, magnitude
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)

        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
    
    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            pass
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def update(self):
        self.move(self.speed)
    
    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)