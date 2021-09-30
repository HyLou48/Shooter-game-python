import pygame
from game import Game
from player import Player

#initialize pygame
pygame.init()

#generate la fenetre de notre jeu
pygame.display.set_caption("Comet fall down")
screen = pygame.display.set_mode((1080, 720))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('Assets/bg.jpg')

#charger notre joueur
player = Player()

#charger notre jeu
game = Game()


#game loop
running = True
while running:
    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # mettre à jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            print("Fermeture du jeu")

        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False