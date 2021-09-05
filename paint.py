import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
screen.fill(white)
pygame.display.update()

class Circle():
    def __init__(self,color,pos,radius,width):

        self.circle_color=color
        self.circle_pos=pos
        self.circle_radius=radius
        self.circle_width=width
        self.circle_surface=screen
    def draw(self):
        self.Draw_circle=pygame.draw.circle(self.circle_surface,self.circle_color,self.circle_pos,self.circle_radius)

while True:
    event=pygame.event.poll()
    if event.type==pygame.MOUSEMOTION:
        pos=pygame.mouse.get_pos()
        greenCircle=Circle(green,pos,10,0)
        greenCircle.draw()
        pygame.display.update()
