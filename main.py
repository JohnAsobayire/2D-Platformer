import pygame

""""
Objects
"""
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.width = 40
    self.height = 60
    self.image = pygame.Surface((self.width, self.height))
    self.image.fill((220, 20, 20))
    self.rect = self.image.get_rect()
    self.movex = 0
    self.movey = 0

  def control(self, x, y):
    """
    control player movement
    """
    self.movex += x
    self.movey += y

  def update(self):
    """
    Update sprite position
    """
    self.rect.x += self.movex
    self.rect.x += self.movey

"""
Setup
"""
worldx = 800
worldy =600
fps = 40
ani = 4
steps = 10 # how many pixels to move
clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([worldx, worldy])

# RGB
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

player = Player()
player.rect.x = 0
player.rect.y = 0

player_list = pygame.sprite.Group()
player_list.add(player)

main = True

"""
Main Look
"""
while main:
  world.fill(BLUE) 
  player.update()
  player_list.draw(world)
  pygame.display.flip() 
  clock.tick(fps) 
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit() 
      main = False 
       
    if event.type == pygame.KEYDOWN: 
      if event.key == ord('q'): 
        pygame.quit() 
        main = False
      if event.key == pygame.K_LEFT or event.key == ord('a'):
        player.control(-steps, 0)
      if event.key == pygame.K_RIGHT or event.key == ord('d'):
        player.control(0, steps)
      if event.key == pygame.K_UP or event.key == ord('w'):
        print("jump")

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == ord('a'):
        player.control(steps, 0)
      if event.key == pygame.K_RIGHT or event.key == ord('d'):
        player.control(0, -steps)
      if event.key == pygame.K_UP or event.key == ord('w'):
        print("Up stop")
