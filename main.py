import pygame

#initialize pygame
pygame.init()

#generate la fenetre de notre jeu
pygame.display.set_caption("Comet fall down")
screen = pygame.display.set_mode((1080, 720))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('Assets/bg.jpg')

#game loop
running = True
while running:
    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))
    # mettre à jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()