import pygame
from datetime import datetime


class Reloj():
    def __init__(self):
        self.fuente = pygame.font.SysFont("Consolas",60)
        self.horaInicio= 0
        self.estado=0
        self.horaFinal=0

    def draw_text(self,text, font, text_col, x,y, screen):
        img = font.render(text, True, text_col)
        rect = img.get_rect()
        rect.center = (250,600)
        screen.blit(img, rect)
        
    def draw_textCero(self,text_col, x,y, screen):
        img = self.fuente.render("00:00:00", True, text_col)
        rect = img.get_rect()
        rect.center = (250,600)
        screen.blit(img, rect)

    def draw_textStop(self,text_col, x,y, screen):
        img = self.fuente.render("00:00:00", True, text_col)
        rect = img.get_rect()
        rect.center = (250,600)
        screen.blit(img, rect)
        
    def draw_bg(self,color):
        screen.fill(color)

    def draw_time(self,color,screen):
        segundos= (datetime.now() - self.horaInicio).total_seconds()
        horas = int(segundos / 60 / 60)
        
        segundos -= horas*60*60
        minutos = int(segundos/60)
        
        segundos -= minutos*60

        if minutos <10:
            minutos=str(minutos)[:1].zfill(2)
        else:
            minutos=str(minutos)[:2]
        if horas <10:
            horas=str(horas)[:1].zfill(2)
        else:
            horas=str(horas)[:2]
        if segundos <10:
            segundos=str(segundos)[:1].zfill(2)
        else:
            segundos=str(segundos)[:2]
        
        strTime = horas+":"+minutos+":"+segundos
        strTime=str(strTime)
        self.draw_text(strTime, self.fuente, color, 20,20,screen)



    def start(self):
        self.horaInicio= datetime.now()
        self.estado=1

    def stop(self):
        self.estado=2
        self.horaFinal=0
   
   


        
