#!/usr/bin/env python
#_*_ coding: utf8 _*_

# importamos las libreria
import pygame
import json 
from clases.ficha import Ficha
from clases.reloj import Reloj
from clases.boton import Boton
import random

# Inicializa el motor de juegos
pygame.init()

# posiciones de cartas
posicionCartas=[(10,10), (250,10),(500,10),(750,10),(10,300), (250,300),(500,300),(750,300)]


# carga cartas
with open('img/img.json') as file:
    data = json.load(file)

#posiciones y creciones de fichas
listaFicha=[]

fondo=pygame.image.load(data['fondo'][0]['direccion'])

boton=Boton(450,600)
boton.cargarImagen(data['boton'][0]['direccion'])
direccion=data['cartas'][0]['direccion'] #direccion general del recurso
recurso=data['cartas'][0]['carta'] #carga la lista de propiedades de la carta
tapada=pygame.image.load(direccion+recurso[4]['archivo'])
for x in range(2):
    for i in range(4):

        posicion=random.randint(0, len(posicionCartas)-1) #se cargo con un 3
        
        ficha=Ficha(recurso[i]['nombre'],posicionCartas[posicion][0],posicionCartas[posicion][1])
        ficha.cargarImagen(direccion+recurso[i]['archivo'])
        listaFicha.append(ficha) #agrega un elemento a la lista listFicha
        posicionCartas.pop(posicion) #elimina un elemento a la posicionCartas
   

# Definir algunos colores (CONSTANTES)
NEGRO  = (  0,   0,   0) #son colores en RGB
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
AZUL   = (0,   0,   255)
ROSA   = (205,   177,   241)
SAKURA = (255,  0,  128)


# Definimos variable de las Dimensiones
dimensiones=(1100,720)
#variable pantalla en donde se carga la clase display (pantalla)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Sakura Card Captor")

#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False
 
# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
comienzo=0
i=0
reloj1=Reloj() #crea el objeto nuevo reloj NUEVO
cartasEncontradas=0
while not hecho:
    
    
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo alg
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Esto que indica que hemos acabado y sale de este bucle

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if comienzo ==0:
                reloj1.start()
            x0, y0 = evento.pos
            print(x0,y0)
            for r in range(8):
                if listaFicha[r].posx <= x0 and listaFicha[r].posx+125 >=x0:
                    if listaFicha[r].posy <= y0 and listaFicha[r].posy+250 >=y0:
                        if listaFicha[r].estado!=3 and listaFicha[r].estado!=1:
                            listaFicha[r].estado=1
                            i=i+1     
                            if i==3:
                                if listaFicha[carta1].estado==1:
                                    listaFicha[carta1].estado=0
                                    listaFicha[carta2].estado=0
                                    print(listaFicha[carta1].estado)
                                    print(listaFicha[carta2].estado)    
                                i=1
                            if i==1:
                                carta1=r    
                            if i ==2:
                                carta2=r
                                if listaFicha[carta1].letra ==listaFicha[carta2].letra :
                                    listaFicha[carta1].estado=3
                                    listaFicha[carta2].estado=3
                                    cartasEncontradas=cartasEncontradas+1
    
        
                



   
   
   
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO
    
    
    # Limpia la ventana y establece el color del fondo
    pantalla.fill(ROSA)
   
    pantalla.blit(fondo, [0, 0])
    pantalla.blit(boton.imagen,[boton.posx,boton.posy])
    for l in range(8):
        #pantalla.blit(listaFicha[l].imagen, [listaFicha[l].posx, listaFicha[l].posy])
        if listaFicha[l].estado==1 or listaFicha[l].estado==3:
            pantalla.blit(listaFicha[l].imagen, [listaFicha[l].posx, listaFicha[l].posy])
        else:
            pantalla.blit(tapada, [listaFicha[l].posx, listaFicha[l].posy])

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    
    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
 
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
 
    # Limita a 20 fotogramas por segundo (frames per second)
    # Avanza y actualiza la pantalla con lo que hemos dibujado.
    if reloj1.estado==1:
        if cartasEncontradas!=4:
            strTime=reloj1.draw_time(SAKURA,pantalla) #MUESTRA EL RELOJ
        else:
            reloj1.stop()
    else:
        reloj1.draw_textCero(SAKURA,20,20,pantalla)
    pygame.display.flip()


    reloj.tick(60)
