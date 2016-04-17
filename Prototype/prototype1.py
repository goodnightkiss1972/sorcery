import pygame
import os

# it is better to have an extra variable, than an extremely long line.
img_path = os.path.join('', 'sorcery.png')

sorcerer1 = os.path.join('', 'sorcery1.png')
sorcerer2 = os.path.join('', 'sorcery2.png')
sorcerer3 = os.path.join('', 'sorcery3.png')
sorcerer4 = os.path.join('', 'sorcery4.png')


class Bird(object):  # represents the bird, not the game	
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(sorcerer1)
        # the bird's position
        self.x = 100
        self.y = 100
        self.flipsorcerer = 5
    
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left
        #gravity effect
        self.y += dist / 2

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        self.flipsorcerer += 1
        if self.flipsorcerer == 5:
            self.image = pygame.image.load(sorcerer1)
        elif self.flipsorcerer == 10:
            self.image = pygame.image.load(sorcerer2)
        elif self.flipsorcerer == 15:
            self.image = pygame.image.load(sorcerer3)
        elif self.flipsorcerer == 20:
            self.image = pygame.image.load(sorcerer4)
            self.flipsorcerer = 0

        surface.blit(self.image, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((640, 400))

bird = Bird() # create an instance
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    bird.handle_keys() # handle the keys

    screen.fill((0,0,0)) # fill the screen with black
    bird.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(100)
