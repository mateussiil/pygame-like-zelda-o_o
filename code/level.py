from random import choice
import pygame
import pygame.freetype
from ui import UI
from weapon import Weapon  # Import the freetype module.
from settings import *
from support import import_csv_layout, import_folder 
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        # get the display surface

        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCamerGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # ata sprite
        self.current_attack = None

        # sprite setup
        self.create_map()

        self.ui = UI()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../map/map_Grass.csv'),
            'object': import_csv_layout('../map/map_Objects.csv')
        }

        graphics = {
            'grass': import_folder('../graphics/Grass'),
            'objects': import_folder('../graphics/objects'),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y), [self.obstacle_sprites, self.visible_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y), [self.obstacle_sprites, self.visible_sprites], 'object', surf)
        self.player: Player = Player((2150,1430), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None            
         
    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        

class YSortCamerGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        # self.offset = pygame.math.Vector2(self.half_width, self.half_height) Camera in half screen
        self.offset = pygame.math.Vector2(self.half_width, self.half_height)
        
        #creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))

    def custom_draw(self, player: Player):

        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y =  player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery): # type: ignore #O bloco nao fica em cima do player
            assert sprite.rect is not None
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)