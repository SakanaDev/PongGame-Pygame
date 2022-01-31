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

def ball_animation():
	global ball_speed_x, ball_speed_y, player_score, opponent_score
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	
	# Player Score
	if ball.left <= 0: 
		ball_start()
		player_score += 1

	# Opponent Score
	if ball.right >= screen_width:
		ball_start()
		opponent_score += 1		

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

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

    player1_text = game_font.render(f"{player1_score}", False, white)
    screen.blit(player1_text, (screen_width / 4, 20))

    player2_text = game_font.render(f"{player2_score}", False, white)
    screen.blit(player2_text, (screen_width / 4 + screen_width / 2, 20))

    # Updating the window
    py.display.flip()
    clock.tick(60)
