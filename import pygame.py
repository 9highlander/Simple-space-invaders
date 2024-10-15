import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_speed = 5
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 2 * player_size, player_size, player_size)

# Enemies
enemy_size = 50
enemy_speed = 3
enemies = []

# Bullets
bullet_speed = 7
bullets = []

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(screen, WHITE, player)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed

def move_bullets():
    for bullet in bullets:
        bullet.y -= bullet_speed

def handle_collisions():
    global enemies, bullets

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

def main():
    global player, bullets, enemies

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(player.x + player_size // 2 - 2, player.y, 4, 10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - player_size:
            player.x += player_speed

        screen.fill((0, 0, 0))

        move_enemies()
        move_bullets()
        handle_collisions()

        draw_player()
        draw_enemies()
        draw_bullets()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
