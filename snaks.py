import pygame

pygame.init()

# colors
white = [225, 225, 225]
red = [225, 0.0]

black = [0, 0, 0]


screen_width = 900
screen_hight = 600

# creating game window
gamewindow = pygame.display.set_mode((screen_width, screen_hight))

pygame.display.set_caption("Snak Game")
pygame.display.update()

exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
fps = 30
clock = pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                snake_x = snake_x + 10
        

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
