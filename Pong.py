import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 13

# Ball settings
BALL_SIZE = 10
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Create paddles
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 0
ball_speed_y = 0

# Score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Game states
MENU = 0
SCORE_SELECT = 1
PLAYING = 2
PAUSED = 3
GAME_OVER = 4
PAUSE_MENU = 5

game_state = MENU
game_mode = None  # "AI" or "PVP"
max_score = 5

def reset_ball(start_side):
    global ball_speed_x, ball_speed_y
    ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
    
    if start_side == "left":
        ball.centerx = left_paddle.right + BALL_SIZE
        ball.centery = left_paddle.centery
        ball_speed_x = BALL_SPEED_X
    elif start_side == "right":
        ball.centerx = right_paddle.left - BALL_SIZE
        ball.centery = right_paddle.centery
        ball_speed_x = -BALL_SPEED_X
    else:  # random
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))

def reset_game():
    global left_score, right_score
    left_paddle.centery = HEIGHT // 2
    right_paddle.centery = HEIGHT // 2
    left_score = 0
    right_score = 0
    reset_ball("random")

def draw_menu():
    window.fill(BLACK)
    title = font.render("PONG", True, WHITE)
    pvp_text = font.render("1. Player vs Player", True, WHITE)
    ai_text = font.render("2. Player vs AI", True, WHITE)
    controls_text = font.render("PvP: W/S (left) and UP/DOWN (right)", True, WHITE)
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
    window.blit(pvp_text, (WIDTH // 2 - pvp_text.get_width() // 2, HEIGHT // 2))
    window.blit(ai_text, (WIDTH // 2 - ai_text.get_width() // 2, HEIGHT // 2 + 50))
    window.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 2 + 100))

def draw_score_select():
    window.fill(BLACK)
    title = font.render("Select Max Score (1-20)", True, WHITE)
    score_text = font.render(str(max_score), True, WHITE)
    instruction = font.render("UP/DOWN to change, ENTER to confirm", True, WHITE)
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    window.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, 2 * HEIGHT // 3))

def draw_game():
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, left_paddle)
    pygame.draw.rect(window, WHITE, right_paddle)
    pygame.draw.ellipse(window, WHITE, ball)
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    window.blit(left_text, (WIDTH // 4, 20))
    window.blit(right_text, (3 * WIDTH // 4, 20))
    pygame.draw.aaline(window, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

def draw_pause():
    pause_text = font.render("PAUSED", True, WHITE)
    resume_text = font.render("Press SPACE to resume", True, WHITE)
    window.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 3))
    window.blit(resume_text, (WIDTH // 2 - resume_text.get_width() // 2, HEIGHT // 2))
    
def draw_pause_menu():
    menu_text = font.render("MENU", True, WHITE)
    restart_text = font.render("R - Restart", True, WHITE)
    main_menu_text = font.render("M - Main Menu", True, WHITE)
    resume_text = font.render("ESC - Resume", True, WHITE)
    window.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 3))
    window.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
    window.blit(main_menu_text, (WIDTH // 2 - main_menu_text.get_width() // 2, HEIGHT // 2 + 50))
    window.blit(resume_text, (WIDTH // 2 - resume_text.get_width() // 2, HEIGHT // 2 + 100))

def draw_game_over(winner):
    window.fill(BLACK)
    game_over_text = font.render("GAME OVER", True, WHITE)
    winner_text = font.render(f"{winner} Wins!", True, WHITE)
    play_again_text = font.render("Press SPACE to play again", True, WHITE)
    menu_text = font.render("Press M to return to menu", True, WHITE)
    window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
    window.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
    window.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, 2 * HEIGHT // 3))
    window.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, 2 * HEIGHT // 3 + 50))

# Game loop
# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == MENU:
                if event.key == pygame.K_1:
                    game_mode = "PVP"
                    game_state = SCORE_SELECT
                elif event.key == pygame.K_2:
                    game_mode = "AI"
                    game_state = SCORE_SELECT
            elif game_state == SCORE_SELECT:
                if event.key == pygame.K_UP:
                    max_score = min(max_score + 1, 20)
                elif event.key == pygame.K_DOWN:
                    max_score = max(max_score - 1, 1)
                elif event.key == pygame.K_RETURN:
                    game_state = PLAYING
                    reset_game()
            elif game_state == PLAYING:
                if event.key == pygame.K_SPACE:
                    game_state = PAUSED
                elif event.key == pygame.K_ESCAPE:
                    game_state = PAUSE_MENU
            elif game_state == PAUSED:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING
                elif event.key == pygame.K_ESCAPE:
                    game_state = PAUSE_MENU
            elif game_state == PAUSE_MENU:
                if event.key == pygame.K_r:
                    game_state = PLAYING
                    reset_game()
                elif event.key == pygame.K_m:
                    game_state = MENU
                elif event.key == pygame.K_ESCAPE:
                    game_state = PLAYING
            elif game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING
                    reset_game()
                elif event.key == pygame.K_m:
                    game_state = MENU
                    
    if game_state == PLAYING:
        keys = pygame.key.get_pressed()
        
        if game_mode == "PVP":
            # Left paddle movement (W/S keys)
            if keys[pygame.K_w] and left_paddle.top > 0:
                left_paddle.y -= PADDLE_SPEED
            if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
                left_paddle.y += PADDLE_SPEED
                
            # Right paddle movement (UP/DOWN keys)
            if keys[pygame.K_UP] and right_paddle.top > 0:
                right_paddle.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
                right_paddle.y += PADDLE_SPEED
        else:  # AI mode
            # Player paddle movement (UP/DOWN keys)
            if keys[pygame.K_UP] and left_paddle.top > 0:
                left_paddle.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and left_paddle.bottom < HEIGHT:
                left_paddle.y += PADDLE_SPEED
                
            # AI paddle movement
            if right_paddle.centery < ball.centery and right_paddle.bottom < HEIGHT:
                right_paddle.y += PADDLE_SPEED
            elif right_paddle.centery > ball.centery and right_paddle.top > 0:
                right_paddle.y -= PADDLE_SPEED
                
        # Move ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        
        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1
            
        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x *= -1
            
        # Score points
        if ball.left <= 0:
            right_score += 1
            if right_score >= max_score:
                game_state = GAME_OVER
            else:
                reset_ball("right")
        elif ball.right >= WIDTH:
            left_score += 1
            if left_score >= max_score:
                game_state = GAME_OVER
            else:
                reset_ball("left")
                
    # Drawing
    if game_state == PLAYING:
        draw_game()
    elif game_state == MENU:
        draw_menu()
    elif game_state == SCORE_SELECT:
        draw_score_select()
    elif game_state == PAUSED:
        draw_game()
        draw_pause()
    elif game_state == PAUSE_MENU:
        draw_game()
        draw_pause_menu()
    elif game_state == GAME_OVER:
        winner = "Left Player" if left_score >= max_score else "Right Player"
        if game_mode == "AI" and winner == "Right Player":
            winner = "AI"
        draw_game_over(winner)
        
    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)
    
# Quit the game
pygame.quit()