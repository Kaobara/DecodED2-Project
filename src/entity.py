import pygame

from src.constants import SCREEN_W


class Entity(pygame.Rect):
    velocity: pygame.Vector2
    image: pygame.Surface
    expired: bool

    ## constructor
    def __init__(self, x: int, y: int, width: int, height: int, sprite_img: str):
        super().__init__(x, y, width, height)
        self.velocity = pygame.Vector2() # (0, 0)
        self.expired = False
        self.image = pygame.transform.smoothscale(pygame.image.load(sprite_img), (width, height))

    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))

    def move(self, delta: int):
        # delta is defined as the time between frames. Want speed to compensate with frame rate.
        # low frames means that there has to be a higher delta between frames
        # higher frames mean that there should be lower.
        # have ot make sure position is based on velocity/speed
        clamp_x = max(self.x + round(self.velocity.x * delta), 0)
        clamp_x = min(clamp_x, SCREEN_W - self.width)

        self.update(
            clamp_x,
            self.y + round(self.velocity.y * delta),
            self.width,
            self.height
        )

    def boundary_check(self):
        return self.x <= 0 or self.x >= SCREEN_W - self.width

    # tick is the behavious of different entities. Each will have different tick implementation
    def tick(self, delta: int, objects: 'list'):
        pass

    def kill(self):
        self.expired = False