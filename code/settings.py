FPS = 60
WIDTH = 1280
HEIGTH = 720
TILESIZE = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'


# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sai/full.png'},
}

magic_data = {
    'fire': {'strength': 5, 'cost': 20, 'graphic': '../graphics/particles/fire/fire.png'},
    'heal': {'strength': 5, 'cost': 20, 'graphic': '../graphics/particles/heal/heal.png'},
}

# enemy

monsters_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound':'../audio/attacl/slash.wav', 'speed': 3, 'resistence': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 20, 'attack_type': 'claw', 'attack_sound':'../audio/attacl/claw.wav', 'speed': 2, 'resistence': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 20, 'attack_type': 'thunder', 'attack_sound':'../audio/attacl/fireball.wav', 'speed': 4, 'resistence': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 20, 'attack_type': 'leaf_attack', 'attack_sound':'../audio/attacl/slash.wav', 'speed': 3, 'resistence': 3, 'attack_radius': 50, 'notice_radius': 300}
}