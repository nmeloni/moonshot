import pygame

pygame.init()
pygame.display.set_caption("Toto")
screen = pygame.display.set_mode( (500,500) )


done = False
clock = pygame.time.Clock()
x=60
y=60

while not done:
    clock.tick(60)
    screen.blit(image, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: y -= 1
            if pressed[pygame.K_DOWN]: y += 1
            if pressed[pygame.K_LEFT]: x -= 1
            if pressed[pygame.K_RIGHT]: x += 1
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, x+30, y+30))
        
    pygame.display.flip()
