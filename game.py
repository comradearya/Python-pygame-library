import pygame
FPS = 60
W = 700 # ширина экрана
H = 400 # высота экрана
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 100, 50)
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
bomb = False # летит ли бомба
x_goal = 0 # координаты цели
y_goal = 0
y_bomb = H # координата бомбы
while 1:
 sc.fill(WHITE)
 pygame.display.update()
 for i in pygame.event.get():
     if i.type == pygame.QUIT:
         exit()
     elif i.type == pygame.MOUSEBUTTONDOWN:
 # если был клик, но другая бомба не летит
        if i.button == 1 and bomb == False:
            bomb = True
            x_goal = i.pos[0]
            y_goal = i.pos[1]
 # если бомба летит, но пока не достигла цели
 if bomb and y_bomb > y_goal:
    pygame.draw.circle(sc, BLACK, (x_goal, y_bomb), 15)
    y_bomb -= 1
    pygame.display.update()
 # если бомба уже достигла цели
 elif bomb and y_bomb <= y_goal:
    pygame.draw.rect(sc, ORANGE, (x_goal-25, y_bomb-15, 50, 30))
    pygame.display.update()
    pygame.time.delay(1000) # задержка, чтобы увидеть взрыв
    bomb = False
    y_bomb = H
    clock.tick(FPS)

pygame.quit()
