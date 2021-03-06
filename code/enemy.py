from dis import dis
from debug import debug
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

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        self.vulnerable = True
        self.hit_time = None
        self.invicibility_duration = 300

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

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)
    
    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistence

    def get_damage(self, player: Player, attack_type):
        if self.vulnerable:
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else: 
                # magic damage
                pass
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        debug(self.health)
        if self.health <= 0:
            self.kill()

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if not self.can_attack:
            if current_time - self.attack_time >=self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >=self.invicibility_duration:
                self.vulnerable = True

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()
    
    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)