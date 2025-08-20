import pygame
pygame.init()

# Constants
screenWidth, screenHeight = 400, 400
gridSize = 20
cellSize = screenWidth // gridSize

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game of Life")

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
gridColour = (200, 200, 200)

# Manually define the initial state of the grid
# 1 represents alive cells, 0 represents dead cells
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Import play button
playButton = pygame.image.load('playButton.png').convert_alpha()
image = pygame.Surface((447, 558)).convert_alpha()
image.blit(playButton, (0, 0))
image = pygame.transform.scale(image, (cellSize - 8, cellSize - 5))
image.set_colorkey(black)
playButton = image

# Import reset button
resetArrow = pygame.image.load('resetArrow.png').convert_alpha()
image = pygame.Surface((447, 558)).convert_alpha()
image.blit(resetArrow, (0, 0))
image = pygame.transform.scale(image, (cellSize + 10, cellSize + 20))
image.set_colorkey(black)
resetArrow = image

on = False
tickCooldown = 50
lastTick = 0
currentTick = pygame.time.get_ticks()

# Main loop
running = True
while running:
    # Reset Screen
    screen.fill(white)
    
    # Deal with quiting, playing, resetting and clicking cells
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
            delete = None
            while dragging == True:
                x, y = pygame.mouse.get_pos()
                
                if x < screenWidth and y < screenHeight and x > 0 and y > 0:
                    if on == True:
                        if ((x > screenWidth - cellSize * 2) and (x < screenWidth - cellSize)) and (y < cellSize):
                            on = False
                    else:
                        if ((x > screenWidth - cellSize * 2) and (x < screenWidth - cellSize)) and (y < cellSize):
                            on = True
                        elif (x > screenWidth - cellSize) and (y < cellSize):
                            for y in range(gridSize):
                                for x in range(gridSize):
                                    grid[y][x] = 0
                        else:
                            if delete == None:
                                grid[y // cellSize][x // cellSize] = 1 - grid[y // cellSize][x // cellSize]
                                delete = 1 - grid[y // cellSize][x // cellSize]
                            elif delete == 0:
                                grid[y // cellSize][x // cellSize] = 1
                            else:
                                grid[y // cellSize][x // cellSize] = 0
                    
                    # Draw grid
                    for y in range(gridSize):
                        for x in range(gridSize):
                            if grid[y][x] == 1:
                                colour = black 
                            else: 
                                colour = white

                            pygame.draw.rect(screen, colour, (x * cellSize, y * cellSize, cellSize, cellSize))

                    # Draw vertical grid lines
                    for x in range(0, screenWidth, cellSize):
                        pygame.draw.line(screen, gridColour, (x, 0), (x, screenHeight))

                    # Draw horizontal grid lines
                    for y in range(0, screenHeight, cellSize):
                        pygame.draw.line(screen, gridColour, (0, y), (screenWidth, y))
                    
                    # Play play button
                    pygame.draw.rect(screen, black, (screenWidth - cellSize * 2, 0, cellSize, cellSize))
                    if on == True:
                        pygame.draw.rect(screen, white, ((screenWidth - cellSize * 1.5) - 5, 4, 12, 12))
                    else:
                        screen.blit(playButton, ((screenWidth - cellSize * 1.5) - 5, 2))

                    # Draw reset button
                    pygame.draw.rect(screen, black, (screenWidth - cellSize, 0, cellSize, cellSize))
                    screen.blit(resetArrow, (screenWidth - cellSize + 3, 1))
                    
                    pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        dragging = False
                        delete = None
    
    # Update Grid
    currentTick = pygame.time.get_ticks()
    if currentTick - lastTick >= tickCooldown:
        if on == True:
            for y in range(gridSize):
                for x in range(gridSize):
                    alive = 0
                    if grid[y][x] == 1:
                        for i in [-1, 0, 1]:
                            for j in [-1, 0, 1]:
                                if 0 <= y + i <= gridSize - 1 and 0 <= x + j <= gridSize - 1:
                                    if i != 0 or j != 0:
                                        if grid[y + i][x + j] == 1:
                                            alive += 1

                        if alive >= 4:
                            grid[y][x] = 0
                        elif alive <= 1:
                            grid[y][x] = 0

                    else:
                        if ((y != 0) and (y != gridSize - 1)) and ((x != 0) and (x != gridSize - 1)):
                            for i in range(-1, 2):
                                for j in range(-1, 2):
                                    if i != 0 or j != 0:
                                        if grid[y + i][x + j] == 1:
                                            alive += 1
                            
                            if alive == 3:
                                grid[y][x] = 1

        lastTick = currentTick

    # Draw grid
    for y in range(gridSize):
        for x in range(gridSize):
            if grid[y][x] == 1:
                colour = black 
            else: 
                colour = white

            pygame.draw.rect(screen, colour, (x * cellSize, y * cellSize, cellSize, cellSize))

    # Draw vertical grid lines
    for x in range(0, screenWidth, cellSize):
        pygame.draw.line(screen, gridColour, (x, 0), (x, screenHeight))

    # Draw horizontal grid lines
    for y in range(0, screenHeight, cellSize):
        pygame.draw.line(screen, gridColour, (0, y), (screenWidth, y))
    
    # Play play button
    pygame.draw.rect(screen, black, (screenWidth - cellSize * 2, 0, cellSize, cellSize))
    if on == True:
        pygame.draw.rect(screen, white, ((screenWidth - cellSize * 1.5) - 5, 4, 12, 12))
    else:
        screen.blit(playButton, ((screenWidth - cellSize * 1.5) - 5, 2))

    # Draw reset button
    pygame.draw.rect(screen, black, (screenWidth - cellSize, 0, cellSize, cellSize))
    screen.blit(resetArrow, (screenWidth - cellSize + 3, 1))

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
