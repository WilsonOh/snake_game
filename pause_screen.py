import pygame


def pause_screen(snake_len: int) -> None:
    window = pygame.display.get_surface()
    clock = pygame.time.Clock()
    paused = True
    font = pygame.font.SysFont("comicsans", window.get_height() // 15, bold=True)
    game_over_font = font.render(f"GAME PAUSED. YOUR SCORE IS {snake_len}",
                                 True, pygame.Color('red'))
    keys_font = font.render("Press escape to return or q to quit", True, pygame.Color('blue'))
    while paused:
        clock.tick(5)
        window.fill(pygame.Color('gray49'))
        window.blit(game_over_font, (window.get_width() // 2 - game_over_font.get_width() // 2,
                                     window.get_height() // 2 - game_over_font.get_height() // 2))
        window.blit(keys_font, (window.get_width() // 2 - keys_font.get_width() // 2,
                                window.get_height() // 2 - keys_font.get_height() // 2 +
                                game_over_font.get_height()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.update()
