import pygame as py
import random as r

def draw_player(x):
    screen.blit(eval(x), p_rect)
def draw_level_count(level):
    level_text = font.render(str(level+1), False, (255,255,255))
    level_text_rect = level_text.get_rect(center = (400, 100))
    screen.blit(level_text, level_text_rect)
def update_player(x):
    if x == 'next':
        p_rect.x = 50
    else:
        p_rect.x = 700
def update_light(x):
    if x == 'next':
        light_rect.x = 50
    else:
        light_rect.x = 700
def draw_coin(x):
    if coin_status:
        pass
    else:
        screen.blit(coin_list[x], coin_rect)
def update_coin():
    coin_coord = (r.randint(100,700),r.randint(100,700))
    return coin_coord
def check_coin():
    if bullet_rect.colliderect(coin_rect):
        return True
    return False
def draw_dirt(x, num1, num2):
    screen.blit(dirt_list[x], (p_rect.x +num1, p_rect.y + num2))
def fire_weapon():
    if player_direction == 'player_right':
        bullet_rect.x += bullet_vel
    elif player_direction == 'player_left':
        bullet_rect.x -= bullet_vel
    elif player_direction == 'player_up':
        bullet_rect.y -= bullet_vel
    elif player_direction == 'player_down':
        bullet_rect.y += bullet_vel
def draw_weapon():
    screen.blit(bullet, bullet_rect)
def bullet_wall_collision():
    if bullet_rect.y > 750:
        return True
    elif bullet_rect.y < 50:
        return True
    return False

py.init()
screen = py.display.set_mode((800,800))
py.display.set_caption('Dungeon Traveller Game')
clock = py.time.Clock()

# background
background = py.transform.scale(py.image.load('background.png').convert(), (800,800))
bg_rect = background.get_rect(center = (400,400))

# walls

hor_wall = py.transform.scale(py.image.load('block.png').convert(), (800, 50))
ver_wall = py.transform.scale(py.image.load('block.png').convert(), (50, 350))

wall1_rect = hor_wall.get_rect(center = (400, 25))
wall2_rect = hor_wall.get_rect(center = (400, 775))

# player

player_right = py.transform.scale(py.image.load('player/sprite_0.png').convert_alpha(), (50,50))
player_up = py.transform.scale(py.image.load('player/sprite_1.png').convert_alpha(), (50,50))
player_left = py.transform.scale(py.image.load('player/sprite_2.png').convert_alpha(), (50,50))
player_down = py.transform.scale(py.image.load('player/sprite_3.png').convert_alpha(), (50,50))
p_rect = player_right.get_rect(center = (400,400))

player_direction = 'player_right'

# coin

coin0 = py.transform.scale(py.image.load('coin/coin_0.png').convert_alpha(), (50,50))
coin1 = py.transform.scale(py.image.load('coin/coin_1.png').convert_alpha(), (50,50))
coin2 = py.transform.scale(py.image.load('coin/coin_2.png').convert_alpha(), (50,50))
coin_list = [coin0, coin1, coin2]
coin_index = 0
coin_rect = coin1.get_rect(center = (600, 400))

coin_status = False

# dirt

dirt0 = py.transform.scale(py.image.load('dirt/dirt_0.png').convert_alpha(), (50,50))
dirt1 = py.transform.scale(py.image.load('dirt/dirt_1.png').convert_alpha(), (50,50))
dirt2 = py.transform.scale(py.image.load('dirt/dirt_2.png').convert_alpha(), (50,50))
dirt_list = [dirt0,dirt1,dirt2]
dirt_index = 0
dirt_rect = dirt0.get_rect(center = p_rect.center)

# light circle

light = py.transform.scale(py.image.load('light circle.png').convert_alpha(), (350,350))
light_rect = light.get_rect(center = p_rect.center)
# enemy

enemy = py.transform.scale(py.image.load('enemy.png').convert(), (50,50))
enemy_rect = enemy.get_rect()

# bullet

bullet = py.transform.scale(py.image.load('bullet.png').convert(), (20,20))
bullet_rect = bullet.get_rect(center = p_rect.center)
bullet_vel = 2
hit_status = False
fire_status = False

# door hitboxes

door = py.transform.scale(py.image.load('door.png').convert(), (50,800))
door1_rect = door.get_rect(center = (800, 400))
door2_rect = door.get_rect(center = (0, 400))



# level counter

level = 0
latest_level = level

# text

font = py.font.Font('ARCADECLASSIC.ttf', 50)

# temporary set array for each level

level_list = [[1,2], [2,1], [4,3]]

while True:
    screen.blit(background, bg_rect)
    screen.blit(light, light_rect)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    
    key = py.key.get_pressed()
    if coin_status == False and p_rect.colliderect(door1_rect):
        pass
    else:

        if key[py.K_RIGHT]:
            p_rect.x += 5
            light_rect.x += 5
            player_direction = 'player_right'
            draw_dirt(int(dirt_index), -50, 0)
            if dirt_index < 2.95:
                dirt_index += 0.05
            else:
                dirt_index = 0
    if level == 0 and p_rect.colliderect(door2_rect):
        pass
    else:
        if key[py.K_LEFT]:
            p_rect.x -= 5
            light_rect.x -= 5
            player_direction = 'player_left'
            draw_dirt(int(dirt_index), 50, 0)
            if dirt_index < 2.95:
                dirt_index += 0.05
            else:
                dirt_index = 0
    if p_rect.colliderect(wall1_rect) == False:
        if key[py.K_UP]:
            p_rect.y -= 5
            light_rect.y -= 5
            player_direction = 'player_up'
            draw_dirt(int(dirt_index), 0, 50)
            if dirt_index < 2.95:
                dirt_index += 0.05
            else:
                dirt_index = 0
    if p_rect.colliderect(wall2_rect) == False:
        if key[py.K_DOWN]:
            p_rect.y += 5
            light_rect.y += 5
            player_direction = 'player_down'
            draw_dirt(int(dirt_index), 0, -50)
            if dirt_index < 2.95:
                dirt_index += 0.05
            else:
                dirt_index = 0

    if fire_status == False:
        if key[py.K_SPACE]:
            bullet_rect.center = p_rect.center
            fire_status = True
        

    if check_coin():
        coin_status = True

    if p_rect.colliderect(door1_rect):
        if coin_status:
            level += 1
            latest_level = level
            update_player('next')
            update_light('next')
            coin_coord = update_coin()
            coin_rect.center = coin_coord
            coin_status = False

            if bullet_rect.x > 800:
                bullet_rect.x -= 800
            else:
                bullet_rect.x = -(800-bullet_rect.x)
        elif latest_level > level:
            update_player('next')
            update_light('next')
            level += 1
            if bullet_rect.x > 800:
                bullet_rect.x -= 800
            else:
                bullet_rect.x = -(800-bullet_rect.x)



    if p_rect.colliderect(door2_rect):
        if level > 0:
            level -= 1
            update_player('previous')
            update_light('previous')


    
    screen.blit(door, door1_rect)
    screen.blit(door, door2_rect)

    if bullet_wall_collision():
        fire_status = False

    if fire_status:
        fire_weapon()
        draw_weapon()       
    if latest_level == level:
        if abs(p_rect.x - coin_rect.x) < 170 and abs(p_rect.y - coin_rect.y) < 170:
            draw_coin(int(coin_index))
            if coin_index < 2.95:
                coin_index += 0.05
            else:
                coin_index = 0
    draw_player(player_direction)
    draw_level_count(level)
    screen.blit(hor_wall, wall1_rect)
    screen.blit(hor_wall, wall2_rect)
    py.display.update()
    clock.tick(120)