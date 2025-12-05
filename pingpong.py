import pygame, sys, random, time
from pygame import *
from time import *

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opps_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_h:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_start()
        player_score += 1
    
    if ball.right >= screen_w:
        ball_start()
        opps_score += 1

    if ball.colliderect(player) or ball.colliderect(opps):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_h:
        player.bottom = screen_h

def opponent():
    if opps.top < ball.y:
        opps.top += opps_speed
    if opps.bottom > ball.y:
        opps.bottom -= opps_speed
    if opps.top <= 5:
        opps.top = 5
    if opps.bottom >= screen_h:
        opps.bottom = screen_h

def ball_start():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_w/2, screen_h/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

screen_w = 980
screen_h = 660
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Ping Pong")

ball = pygame.Rect(screen_w/2 - 15, screen_h/2 - 15, 30, 30)
player = pygame.Rect(screen_w - 20, screen_h/2 - 70, 10, 140)
opps = pygame.Rect(10, screen_h/2 - 70, 10, 140)

bg = pygame.Color('grey12')
grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opps_speed = 7

player_score = 0
opps_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 6
            if event.key == pygame.K_UP:
                player_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 6
            if event.key == pygame.K_UP:
                player_speed += 6


    ball_animation()
    player_animation()
    opponent()

    screen.fill(bg)
    pygame.draw.rect(screen, grey, player)
    pygame.draw.rect(screen, grey, opps)
    pygame.draw.ellipse(screen, grey, ball)
    pygame.draw.aaline(screen, grey, (screen_w/2, 0), (screen_w/2, screen_h))

    player_text = basic_font.render(f'{player_score}', False, grey)
    screen.blit(player_text, (500, 100))

    opps_text =  basic_font.render(f'{opps_score}', False, grey)
    screen.blit(opps_text, (463, 100))

    pygame.display.flip()
    clock.tick(60)