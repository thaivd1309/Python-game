import pygame
import random

pygame.init()

def movement(x, y):
    global head
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and direction != [1, 0]:
        direction[0] = -1
        direction[1] = 0
    elif key[pygame.K_RIGHT] and direction != [-1, 0]:
        direction[0] = 1
        direction[1] = 0
    elif key[pygame.K_UP] and direction != [0, 1]:
        direction[0] = 0
        direction[1] = -1
    elif key[pygame.K_DOWN] and direction != [0, -1]:
        direction[0] = 0
        direction[1] = 1
  
def snake(body):
    global head, speed_count, speed
    for i in range(len(body)):
        pygame.draw.rect(win, (255, 255, 255), (body[i][0], body[i][1], step - 1, step - 1))
    head = [body[0][0], body[0][1]]
    if speed_count >= speed:
        head[0] += step * direction[0]
        head[1] += step * direction[1]
        speed_count = 0
        body.insert(0, head)
        if body[0] != snack:
            tail = body.pop()
            pygame.draw.rect(win, (0, 0, 0), (tail[0], tail[1], step, step))
        
    
def snack_gen():
    global snack, x_snack, y_snack, score
    pygame.draw.rect(win, (0, 255, 0), (snack[0], snack[1], step, step))
    if snack == body[0]:
        pygame.draw.rect(win, (0, 0, 0), (snack[0], snack[1], step, step))
        score += 1
        snack[0] = random.randint(0, (width / step) - 1) * step
        snack[1] = random.randint(0, (width / step) - 1) * step
        while snack in body:
            snack[0] = random.randint(0, (width / step) - 1) * step
            snack[1] = random.randint(0, (width / step) - 1) * step
            
def write(text, size):
    font = pygame.font.SysFont('comicsans', size) 
    text_display = font.render(text, True, (255, 255, 255)) 
    return text_display

def lose(x, y):
    global run, win, credit
    if head[0] < 0 or head[1] < 0 or head[0] > width - step or head[1] > width - step or head in body[1:]:
        pygame.time.delay(2000)
        run = False
        credit = True 
def intro(start, win):
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
        confirm = pygame.key.get_pressed()
        if confirm[pygame.K_RETURN]:
            start = False
            run = False
        title = write('SNAKE', 50)
        press_enter = write('Press Enter', 40)
        win.blit(title, (width / 2 - title.get_width() / 2, width / 2 - title.get_height() / 2))
        win.blit(press_enter, (width / 2 - press_enter.get_width() / 2, width / 2 + 50))
        pygame.display.update() 
        
def end(credit, win):
    while credit:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                credit = False
        win.fill((0,0,0))
        gameover = write('GAME OVER', 50)
        score_number = write('SCORE: ' + str(score), 40)
        maker = write('Maker: Duc Thai Vu', 30)
        win.blit(gameover, (width / 2 - gameover.get_width() / 2, width / 2 - gameover.get_height() / 2))
        win.blit(score_number, (width / 2 - score_number.get_width() / 2, width / 2 + 50))
        win.blit(maker, (width - maker.get_width(), width + 40 - maker.get_height()))
        pygame.display.update()

def choosediff(diff_page, win):
    global step, speed
    while diff_page:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                diff_page = False
                run = False
        choose = write('Choose difficulty', 40)
        win.blit(choose, (width / 2 - choose.get_width() / 2, width / 2 - choose.get_height() / 2 - 40))
        choose1 = write('1 - Easy', 30)
        choose2 = write('2 - Medium', 30)
        choose3 = write('3 - Hard', 30)
        win.blit(choose1, (width / 2 - choose1.get_width() / 2, width / 2 - choose1.get_height() / 2))
        win.blit(choose2, (width / 2 - choose2.get_width() / 2, width / 2 - choose2.get_height() / 2 + 40))
        win.blit(choose3, (width / 2 - choose3.get_width() / 2, width / 2 - choose3.get_height() / 2 + 80))
        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            step = 400 / 20
            diff_page = False
        if key[pygame.K_2]:
            step = 400 / 10
            diff_page = False
        if key[pygame.K_3]:
            step = 400 / 10
            speed = 3
            diff_page = False     
        pygame.display.update()
    
#main
width = 400
x = 40
y = 40
speed = 4
direction = [1, 0]
x_snack = width / 2
y_snack = width / 2
speed_count = 0
score = 0
body = [[x, y], [x - step, y]]
snack = [x_snack, y_snack]

win = pygame.display.set_mode((width, width + 40))
clock = pygame.time.Clock()
pygame.display.set_caption('SNAKE')
start = True
run = True
credit = False
diff_page = True

intro(start, win)
win.fill((0,0,0))
pygame.display.update()
choosediff(diff_page, win)
win.fill((0,0,0))
pygame.display.update()
while run:
    pygame.time.delay(50)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.line(win, (255, 0, 0), (0, width), (width, width), 5)
    win.fill((0, 0, 0), (0, width, width, 40))
    win.blit(write('SCORE: ' + str(score), 30), (20, width + 15))
    speed_count += 1
    snake(body)
    movement(x, y)
    snack_gen()
    pygame.display.update()
    lose(x, y)
end(credit, win)

pygame.quit()
