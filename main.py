import pygame
import time

from actors import *  # Imports all classes from actors.py

pygame.init()

# Game properties
screenWidth = 1000
screenHeight = 1000
tickDelay = 0.01  # Time between updates. Lower time = faster game.
gameTitle = "Tracker Field"

screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption(gameTitle)

# Game class
class Game:
    def __init__(self):
        self.ballStats = [ # Starting X, Starting Y, Colour, Size, Max Acceleration, Max Velocity
            [200, 200, (255, 0, 0), 10, 0.1, 5],
            [800, 800, (0, 255, 0), 8, 0.3, 7],
            [200, 800, (0, 0, 255), 10, 0.05, 15],
            [800, 200, (255, 255, 0), 7, 0.2, 2]
        ]
        self.backgroundColour = (255, 255, 255)

        self.trackers = []
        for stat in self.ballStats:
            self.trackers.append(Ball(stat[0], stat[1], stat[2], stat[3], stat[4], stat[5]))

    def logic(self):
        global screenWidth
        global screenHeight

        mousePos = pygame.mouse.get_pos()
        
        clicks = pygame.mouse.get_pressed()
        if clicks[2]: # Freeze all of the trackers and reset their velocities
            for ball in self.trackers:
                ball.velocity = [0, 0]
        else:
            for ball in self.trackers:
                ball.updatePosition(mousePos)

                if ball.position[0] < (ball.size * -1):
                    ball.position[0] = screenWidth + ball.size
                elif ball.position[0] > (ball.size + screenWidth):
                    ball.position[0] = -1 * ball.size
                
                if ball.position[1] < (ball.size * -1):
                    ball.position[1] = screenHeight + ball.size
                elif ball.position[1] > (ball.size + screenHeight):
                    ball.position[1] = -1 * ball.size

    def draw(self):
        screen.fill(self.backgroundColour)
        for ball in self.trackers:
            pygame.draw.circle(screen, ball.colour, (int(ball.position[0]), int(ball.position[1])), ball.size)
        pygame.display.flip() # Display drawn objects on screen

# Run the actual game
game = Game() # Game object

gameRunning = True
while gameRunning:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            gameRunning = False
    
    game.logic()
    game.draw()

    time.sleep(tickDelay)

pygame.quit()
