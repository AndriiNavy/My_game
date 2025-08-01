import pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 1000, 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("It`s big game!")
# Rectangle setup
rect_width, rect_height = 50, 50
x, y = 200, 200
vel = 15
run = True
while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    # --- BOUNDARY CHECKS ---
    if x < 0:
        x = 0
    if x + rect_width > WIDTH:
        x = WIDTH - rect_width
    if y < 0:
        y = 0
    if y + rect_height > HEIGHT:
        y = HEIGHT - rect_height
    # Drawing
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, rect_width, rect_height))
    pygame.display.update()
pygame.quit()
