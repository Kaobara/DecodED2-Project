from pygame import Vector2, Color
from pygame.locals import K_RIGHT, K_LEFT, K_SPACE, KEYDOWN, KEYUP
from src.constants import BLACK, WHITE
from src.entities.player import Player

class Game:
    # have to define all entities in the game
    entities: "list"

    # create constructor
    def __init__(self):
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)

    # the 3 behaviours
    def handleInput(self, events):
        # have to detect if player is moving left, right, or shooting
        for event in events:
            # pressing left or right
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.player.move_left()
                if event.key == K_RIGHT:
                    self.player.move_right()
                if event.key == K_SPACE:
                    print("Shoot bullet!")
            if event.type == KEYUP:
                if event.key == K_LEFT and self.player.move_direction < 0:
                    self.player.stop_moving()
                if event.key == K_RIGHT and self.player.move_direction > 0:
                    self.player.stop_moving()



    def update(self, delta):
        # constantly update every single entity over and over again
        # but we loop through the entity list from the back to front
        for i in range(len(self.entities)-1, -1, -1):
            obj = self.entities[i]
            # Execute entity logic. Can be done as entities inherit from entity class

            obj.tick(delta, self.entities)

            obj.move(delta)

    # helper function for render
    def renderText(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        # clear out entire canvas
        display.fill(BLACK)
        for obj in self.entities:
            obj.render(display)

        # render some text on the screen. Use helper function
        # loop through each entity and render it
        self.renderText(display, font, "Space Invaders", WHITE, (50, 50))
