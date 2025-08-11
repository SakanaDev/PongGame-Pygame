from glob import glob
import time
import pygame as py
import sys
import random

# General setup
py.init()
clock = py.time.Clock()

# Setting up the main window
screen_width = 858
screen_height = 525
screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Pong Game")

# Define color
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Rectangles
ball = py.Rect(screen_width / 2 - 9, screen_height / 2 - 9, 18, 18)
player_1 = py.Rect(screen_width - 30, screen_height / 2 - 30, 10, 60)
player_2 = py.Rect(20 , screen_height / 2 - 30, 10, 60)

# Edge 
edge_1 = py.Rect(0, 0, 2, 858)
edge_2 = py.Rect(0, 0, 858, 4)
edge_3 = py.Rect(screen_width - 2, 0, 4, 858)
edge_4 = py.Rect(0, screen_height - 2, 858, 4)

# Game Variable
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player1_speed = 0
player2_speed = 0

# Score Text
player1_score = 0
player2_score = 0
game_font = py.font.Font('freesansbold.ttf', 32)
score_time = None
time_font = py.font.Font('freesansbold.ttf', 70)

# Sound
pong_sound = py.mixer.Sound("./Sound/pong.ogg") # Change the path or route
score_sound = py.mixer.Sound("./Sound/score.ogg") # Change the path or route


def ball_animation():
    global ball_speed_x, ball_speed_y, player1_score, player2_score, score_time, pong_sound, score_sound

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        py.mixer.Sound.play(pong_sound)
    
    if ball.left <= 0:
        score_time = py.time.get_ticks()
        player1_score += 1
        ball_start()
        py.mixer.Sound.play(score_sound)
    
    if ball.right >= screen_width:
        score_time = py.time.get_ticks()
        player2_score += 1
        ball_start()
        py.mixer.Sound.play(score_sound)
    
    if ball.colliderect(player_1) and ball_speed_x > 0:
        if abs(ball.right - player_1.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.top - player_1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        elif abs(ball.bottom - player_1.top) and ball_speed_y > 0:
            ball_speed_y *= -1
        py.mixer.Sound.play(pong_sound)
    
    if ball.colliderect(player_2):
        if abs(ball.left - player_2.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.top - player_2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        elif abs(ball.bottom - player_2.top) and ball_speed_y > 0:
            ball_speed_y *= -1
        py.mixer.Sound.play(pong_sound)

def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    ball.center = (screen_width / 2, screen_height / 2)
    current_time = py.time.get_ticks()

    if current_time - score_time < 700:
        number_three = time_font.render("3", False, yellow)
        screen.blit(number_three, (screen_width / 2 - 20, screen_height / 2 - 30))
    
    if 700 < current_time - score_time < 1400:
        number_two = time_font.render("2", False, yellow)
        screen.blit(number_two, (screen_width / 2 - 20, screen_height / 2 - 30))
    
    if 1400 < current_time - score_time < 2100:
        number_one = time_font.render("1", False, yellow)
        screen.blit(number_one, (screen_width / 2 - 20, screen_height / 2 - 30))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0

    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = None

def player_animation():
    global player1_speed, player2_speed

    player_1.y += player1_speed
    player_2.y += player2_speed

    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height

    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height

# --- Main Program Loop ---
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                player1_speed += 7
            if event.key == py.K_UP:
                player1_speed -= 7
            if event.key == py.K_w:
                player2_speed -= 7
            if event.key == py.K_s:
                player2_speed += 7
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player1_speed -= 7
            if event.key == py.K_UP:
                player1_speed += 7
            if event.key == py.K_w:
                player2_speed += 7
            if event.key == py.K_s:
                player2_speed -= 7
    
    # Game Logic
    ball_animation()
    player_animation()
    
    # Visuals
    screen.fill(black)
    py.draw.rect(screen, white, edge_1)
    py.draw.rect(screen, white, edge_2)
    py.draw.rect(screen, white, edge_3)
    py.draw.rect(screen, white, edge_4)
    py.draw.ellipse(screen, white, ball)
    py.draw.rect(screen, white, player_1)
    py.draw.rect(screen, white, player_2)
    py.draw.aaline(screen, white, (screen_width / 2, 0), (screen_width / 2, screen_height))
    
    if score_time:
        ball_start()

    player1_text = game_font.render(f"{player1_score}", False, white)
    screen.blit(player1_text, (screen_width / 4, 20))

    player2_text = game_font.render(f"{player2_score}", False, white)
    screen.blit(player2_text, (screen_width / 4 + screen_width / 2, 20))

    # Updating the window
    py.display.flip()
    clock.tick(60)
