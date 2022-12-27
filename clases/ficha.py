import pygame

class Ficha():
    def __init__(self,letra,posx,posy):
        self.letra=letra #el nombre de la letra por ejemplo "A"
        self.estado=0 #es el estado de la ficha o carta... tapada, o descubierta
        self.posx=posx
        self.posy=posy
        self.imagen=""
        

    def cargarImagen(self,direccion):
        self.imagen=pygame.image.load(direccion)
