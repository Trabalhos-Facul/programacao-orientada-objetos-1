import sys
import pygame
import game_sprites
import game_runner

# inicializacao da janela pygame
drawer = game_sprites.GameDrawer()

runner = game_runner.Game(drawer)

clicked_card_sprite = None
game_finished = False

while True:
    drawer.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if runner.is_game_finished():
                #drawer.btn_in(pos)
                pass
            else:
                clicked_card_sprite = drawer.card_in(pos)

                if clicked_card_sprite:
                    runner.run_round(clicked_card_sprite)
    
    drawer.draw()

