import pygame, sys, time
from settings import *
from sprites import BG, Ground, Cat, Obstacle
from random import choice

class Game:
    def __init__(self):

        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Cat')
        self.clock = pygame.time.Clock()
        self.active = True

        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collition_sprites = pygame.sprite.Group()

        #scale factor
        bg_height = pygame.image.load('../graphics/environment/background.jpg').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height

        #sprite setup
        BG(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites, self.collition_sprites], self.scale_factor)
        self.cat = Cat(self.all_sprites, self.scale_factor * 1.7)

        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        #text
        self.font = pygame.font.Font('../graphics/font/Melting Candle.otf', 60)
        self.score = 0

        #menu
        imported_menu = pygame.image.load('../graphics/ui/button.png').convert_alpha()
        self.menu_surf = pygame.transform.scale(imported_menu, pygame.math.Vector2(imported_menu.get_size()) * self.scale_factor * 0.3)
        self.menu_rect = self.menu_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        #sounds
        self.background_music = pygame.mixer.Sound('../sounds/meow-song.mp3')
        self.die_sound = pygame.mixer.Sound('../sounds/cat-die.mp3')
        self.background_music.set_volume(0.1)
        self.die_sound.set_volume(1)

        self.background_music.play(loops = -1)

    def collitions(self):
        if pygame.sprite.spritecollide(self.cat, self.collition_sprites,False, pygame.sprite.collide_mask)\
            or self.cat.pos.y <= -10:
            for sprite in self.collition_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
            self.active = False
            self.die_sound.play()
            self.cat.kill()

    def display_score(self):
        if self.active:
            #self.score = pygame.time.get_ticks() // 1000
            y = WINDOW_HEIGHT/10
        else:
            y = WINDOW_HEIGHT/2 + self.menu_rect.height

        score_surf = self.font.render(str(self.score), True, 'black')
        score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH/2, y))

        self.display_surface.blit(score_surf, score_rect)

    def run(self):
        last_time = time.time()
        while(True):

            #delta time
            dt = time.time() - last_time
            last_time = time.time()

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.active:
                        self.cat.jump()
                    else:
                        self.score = 0
                        self.active = True
                        self.cat = Cat(self.all_sprites, self.scale_factor * 1.7)


                if event.type == self.obstacle_timer and self.active:
                    self.score += 1
                    orientation = choice(('up', 'down', 'duo'))
                    if orientation == 'duo':
                        Obstacle([self.all_sprites, self.collition_sprites], self.scale_factor * 0.46, 'up')
                        Obstacle([self.all_sprites, self.collition_sprites], self.scale_factor * 0.46, 'down')
                    else:
                        Obstacle([self.all_sprites, self.collition_sprites], self.scale_factor * 0.5, orientation)


            #game logic
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.active: 
                self.collitions()
            else: self.display_surface.blit(self.menu_surf,self.menu_rect)

            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()