import pygame

class Boton():
    def __init__(self,posx,posy):
        self.posx=posx
        self.posy=posy
        self.imagen=""
        

    def cargarImagen(self,direccion):
        self.imagen=pygame.image.load(direccion)
