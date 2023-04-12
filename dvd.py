import pygame
import random

print("hiii")

screen_width = 1280
screen_height = 720
corners = 0


# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
TRAILDISPLAY = pygame.Surface(screen.get_size(), pygame.SRCALPHA) #Makes transparent layer
clock = pygame.time.Clock()
running = True
player_height = 50
velCon = 5
velVar = .25
speed = 1
dx = velCon * random.uniform(1-velVar,1+velVar) * speed
dy = velCon * random.uniform(1-velVar,1+velVar) * speed

init_x = random.randint(0,screen_width)
init_y = random.randint(0,screen_height)

# Create image


player_pos = pygame.Vector2(init_x, init_y)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, "red", (player_pos.x, player_pos.y, player_height, player_height))
    pygame.draw.circle(TRAILDISPLAY, "blue", (player_pos.x+25, player_pos.y+25), 1, 1) #draws a circle on the transparent layer (put in loop)
    keys = pygame.key.get_pressed()


    player_pos.y -= dy
    player_pos.x -= dx

    if (player_pos.x<0):
        player_pos.x = 0
        dx = -1 * dx        

    elif (player_pos.x>screen_width-player_height):
        player_pos.x = screen_width-player_height
        dx = -1 * dx        

    else: 
        player_pos.x = player_pos.x

    if (player_pos.y<0):
        player_pos.y = 0
        dy = -1 * dy
    elif (player_pos.y>screen_height-player_height):
        player_pos.y = screen_height-player_height
        dy = -1 * dy
    else: 
        player_pos.y = player_pos.y

    if (player_pos.x == 0 or player_pos.x == screen_width-50):
        if (player_pos.y == 0 or player_pos.y == screen_height-50):
            print("corner!!")
            corners+=1

    # flip() the display to put your work on screen
    screen.blit(TRAILDISPLAY, (0,0)) #renders the transparent layer
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

print(corners)