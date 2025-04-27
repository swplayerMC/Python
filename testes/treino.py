import pygame
pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
square_pos = pygame.Rect(800, 100, 50, 50)
while True:
    if pygame.event.get(pygame.QUIT): break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square_pos.y -= 20
    if keys[pygame.K_DOWN]:
        square_pos.y += 20
    if keys[pygame.K_LEFT]:
        square_pos.x -= 20
    if keys[pygame.K_RIGHT]:
        square_pos.x += 20
    if keys[pygame.K_RCTRL]:
        square_pos.x -= 100
    if keys[pygame.K_RSHIFT]:
        square_pos.x += 100
    screen.fill('black')
    pygame.draw.rect(screen, 'red', square_pos)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
