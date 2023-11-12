import pygame 
import time
from random import randint
"Створення вікна програми"
pygame.init()
wn = pygame.display.set_mode((500,500))
wn.fill((200,255,255))
clock = pygame.time.Clock()
"Клас Прямокутник"
class Area():
    def __init__(self, x=0, y=0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x,y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(wn, self.fill_color, self.rect)
    def outline(self, frame_color, thikness): #Обведання прямокуника
        pygame.draw.rect(wn, frame_color, self.rect, thikness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
"Класс напис"
class Label(Area):
    def set_text(self, Text, fsize = 12, text_color = (0,0,0)):
        self.image = pygame.font.SysFont("verdana", fsize).render(Text,True,text_color)
    def draw(self, shift_x = 0, shift_y = 0):
        self.fill()
        wn.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))

Yellow = (255,255,0)
Dark_blue = (0,0,100)
Green = (0,255,81)
Blue = (80,80,255)
LIGHT_GREEN = (200,255,200)
LIGHT_RED = (250,128,114)
Red = (255,0,0)
cards = []

x = 70

for i in range (4):
    new_card = Label(x,170,70,100,Yellow)
    new_card.outline(Blue,10)
    new_card.set_text("Click", 26)
    cards.append(new_card)
    x = x+100

start_time = time.time()
cur_time = start_time

time_text = Label(0,0,50,50, (200,255,255))
time_text.set_text("Час:",40,Dark_blue)
time_text.draw(20,20)

score_text = Label(380,0,50,50, (200,255,255))
score_text.set_text("Рахунок:",45,Dark_blue)
score_text.draw(20,20)

timer = Label(50,55,50,40,(200,255,255))
timer.set_text("0",40,Dark_blue)
timer.draw(0,0)

score = Label(400,55,50,40,(200,255,255))
score.set_text("0",40,Dark_blue)
score.draw(0,0)

points = 0

wait = 0
while 1:
    if wait == 0:
        wait = 20
        click = randint(1, 4)
        for i in range(4):
            cards[i].color(Yellow)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for i in range(4):
                if cards[i].collidepoint(x,y):
                    if (i+1) == click:
                        cards[i].color(Green)
                        points +=1
                    else:
                        cards[i].color(Red)
                        points -=1
                    cards[i].fill()
                         
                score.set_text(str(points),40, Dark_blue)
                score.draw(0,0)
    new_time = time.time()
    if int(new_time) - int(cur_time) == 1:
        timer.set_text(str(int(new_time - start_time)),40,Dark_blue)
        timer.draw(0,0)
        cur_time = new_time
    if new_time - start_time >= 11:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Час вичерпано!!!", 60, Dark_blue)
        win.draw(110, 180)
        break

    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text("Ти переміг!!!", 60, Dark_blue)
        win.draw(140,180)
        resul_time = Label(90, 230, 250, 250, LIGHT_GREEN)
        resul_time.set_text("Час проходження: " + str (int(new_time - start_time)) + " секунд", 40, Dark_blue)
        resul_time.draw(0,0)
        break
    pygame.display.update()
    clock.tick(40)
pygame.display.update()