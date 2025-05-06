import pygame
from pygame.locals import *
import random
from sprites import *

class Game:

    def __init__(self):
        pygame.init()

        # Window setup
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Car Game')

        # Colors
        self.gray = (100, 100, 100)
        self.green = (76, 208, 56)
        self.red = (200, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 232, 0)

        # Road and markers
        self.road_width = 300
        self.marker_width = 10
        self.marker_height = 50
        self.left_lane = 150
        self.center_lane = 250
        self.right_lane = 350
        self.lanes = [self.left_lane, self.center_lane, self.right_lane]

        self.road = (100, 0, self.road_width, self.height)
        self.left_edge_marker = (95, 0, self.marker_width, self.height)
        self.right_edge_marker = (395, 0, self.marker_width, self.height)

        self.lane_marker_move_y = 0

        # Player
        self.player_x = 250
        self.player_y = 400
        self.player = PlayerVehicle(self.player_x, self.player_y)
        self.player_group = pygame.sprite.Group(self.player)

        # Vehicles
        self.vehicle_group = pygame.sprite.Group()

        # Load vehicle images
        image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
        self.vehicle_images = [pygame.image.load('../images/' + name) for name in image_filenames]

        self.crash = pygame.image.load('../images/crash.png')
        self.crash_rect = self.crash.get_rect()

        # Sounds
        self.background_music = pygame.mixer.Sound('../sounds/music.mp3')
        self.crash_sound = pygame.mixer.Sound('../sounds/crash.mp3')
        self.steering_sound = pygame.mixer.Sound('../sounds/steering.mp3')
        self.boost_sound = pygame.mixer.Sound('../sounds/boost.mp3')

        self.background_music.set_volume(0.1)
        self.crash_sound.set_volume(0.5)
        self.steering_sound.set_volume(0.1)
        self.boost_sound.set_volume(0.2)

        self.background_music.play(loops=-1)

        # State
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.gameover = False
        self.speed = 2
        self.score = 0
        self.running = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            if event.type == KEYDOWN and not self.gameover:
                if (event.key == K_LEFT or event.key == K_a) and self.player.rect.center[0] > self.left_lane:
                    self.player.rect.x -= 100
                    self.steering_sound.play()
                elif (event.key == K_RIGHT or event.key == K_d) and self.player.rect.center[0] < self.right_lane:
                    self.player.rect.x += 100
                    self.steering_sound.play()

    def simulate(self):
        self.clock.tick(self.fps)

        self.process_events()

        if len(self.vehicle_group) < 2:
            add_vehicle = all(v.rect.top >= v.rect.height * 1.5 for v in self.vehicle_group)
            if add_vehicle:
                lane = random.choice(self.lanes)
                image = random.choice(self.vehicle_images)
                vehicle = Vehicle(image, lane, self.height / -2)
                self.vehicle_group.add(vehicle)

        for vehicle in self.vehicle_group:
            vehicle.rect.y += self.speed
            if vehicle.rect.top >= self.height:
                vehicle.kill()
                self.score += 1
                if self.score > 0 and self.score % 5 == 0:
                    self.boost_sound.play()
                    self.speed += 1

        # Check for collisions
        for vehicle in self.vehicle_group:
            if pygame.sprite.collide_rect(self.player, vehicle):
                self.gameover = True
                self.crash_rect.center = [self.player.rect.centerx, self.player.rect.top]
                self.crash_sound.play()

    def draw(self):
        self.screen.fill(self.green)
        pygame.draw.rect(self.screen, self.gray, self.road)
        pygame.draw.rect(self.screen, self.yellow, self.left_edge_marker)
        pygame.draw.rect(self.screen, self.yellow, self.right_edge_marker)

        self.lane_marker_move_y += self.speed * 2
        if self.lane_marker_move_y >= self.marker_height * 2:
            self.lane_marker_move_y = 0

        for y in range(self.marker_height * -2, self.height, self.marker_height * 2):
            pygame.draw.rect(self.screen, self.white, (self.left_lane + 45, y + self.lane_marker_move_y, self.marker_width, self.marker_height))
            pygame.draw.rect(self.screen, self.white, (self.center_lane + 45, y + self.lane_marker_move_y, self.marker_width, self.marker_height))

        self.player_group.draw(self.screen)
        self.vehicle_group.draw(self.screen)

        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Score: ' + str(self.score), True, self.white)
        self.screen.blit(text, (20, 20))

        if self.gameover:
            self.screen.blit(self.crash, self.crash_rect)
            pygame.draw.rect(self.screen, self.red, (0, 50, self.width, 100))
            text = font.render('Game Over. Press Y to restart or N to quit.', True, self.white)
            self.screen.blit(text, (self.width / 2 - 150, 80))

        pygame.display.update()

    def resetgame_or_quitgame(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_y:
                    self.score = 0
                    self.speed = 2
                    self.vehicle_group.empty()
                    self.player.rect.center = [self.player_x, self.player_y]
                    self.gameover = False
                elif event.key == K_n:
                    self.running = False



game = Game()

while game.running:
    if game.gameover:
        game.resetgame_or_quitgame()
    else:
        game.simulate()
        game.draw()

pygame.quit()
