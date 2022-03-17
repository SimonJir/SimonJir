#4x wild card, 4x wild ven si 4
#4 barvy, 1x 0, 2x 1, 2x 2, 2x 3, 2x 4, 2x 5, 2x 6, 2x 7, 2x 8, 2x 9, 2x eso, 2x no u, 2x draw 2

import random
balicek = ['r0','r1','r1','r2','r2','r3','r3','r4','r4','r5','r5','r6','r6','r7','r7','r8','r8','r9','r9','rEso','rEso','rNoU','rNoU','rDraw2','rDraw2','b0','b1','b1','b2','b2','b3','b3','b4','b4','b5','b5','b6','b6','b7','b7','b8','b8','b9','b9','bEso','bEso','bNoU','bNoU','bDraw2','bDraw2','g0','g1','g1','g2','g2','g3','g3','g4','g4','g5','g5','g6','g6','g7','g7','g8','g8','g9','g9','gEso','gEso','gNoU','gNoU','gDraw2','gDraw2','y0','y1','y1','y2','y2','y3','y3','y4','y4','y5','y5','y6','y6','y7','y7','y8','y8','y9','y9','yEso','yEso','yNoU','yNoU','yDraw2','yDraw2']
hrac1 = input("Zadej jméno prvního hráče: ")
hrac2 = input("Zadej jméno druhého hráče: ")
hrac3 = input("Zadej jméno třetího hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac4 = input("Zadej jméno čtvrtého hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac5 = input("Zadej jméno pátého hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac6 = input("Zadej jméno šestého hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac7 = input("Zadej jméno sedmého hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac8 = input("Zadej jméno osmého hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac9 = input("Zadej jméno devátého hráče (0 pokud už jste zadal/a všechny hráče): ")
hrac10 = input("Zadej jméno desátého hráče (více hráčů už nejde): ")
color = 0
def wild(color):
    color = input("Vyber barvu (cer, zlu, mod, zel): ")
    if color == "cer":
        return 1
    if color == "zlu":
        return 2
    if color == "mod":
        return 3
    if color == "zel":
        return 4

barvy = wild(color)

def wild4(color):
    color = input("Vyber barvu (cer, zlu, mod, zel): ")
    if color == "cer":
        return 1
    if color == "zlu":
        return 2
    if color == "mod":
        return 3
    if color == "zel":
        return 4

barvy4 = wild4(color)
balicek.append(barvy and barvy4)
balicek.append(barvy and barvy4)
random.shuffle(balicek)



