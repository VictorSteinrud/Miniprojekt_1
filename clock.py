import pygame
import sys
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.set_caption("Analog clock")
clock = pygame.time.Clock()
# boiler plate opsætning



def small_radiating_lines():
    n = 60
    delta_angle = 2 * math.pi/n # en hel rotation divideret med mængden af opdelinger af cirklen: n
    x = 320
    y = 240
    r = 200

    for i in range(n): 
        theta = i * delta_angle # vinklen for 1 / 60 af en rotation ganget med det index linje den er ved at tegne
        x_end = x + r * math.cos(theta) # cosinus for den radian den er ved at tegne ganget med længden af linjen giver os x_end for givne linje
        y_end = y + r * math.sin(theta) # sinus gør ligeledes for y_end
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x_end, y_end), width=3) # 60 gange tegner vi en linje




def white_cirle_big():
    pygame.draw.circle(screen, (255, 255, 255), (320, 240), 187) # vi fylder midten med en hvid cirkel så small_radiating_lines() bliver en minutangivelse

 

def radiating_lines(): # Vi gør det samme som i small_radiating_lines() bare kun 12 gange hvilket leder til en større grad mellem stregerne.
    n = 12
    delta_angle = 2 * math.pi/n
    x = 320
    y = 240
    r = 200

    for i in range(n): # vi tegner timeangivende streger med radiating_lines()
        theta = i * delta_angle
        x_end = x + r * math.cos(theta)
        y_end = y + r * math.sin(theta)
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x_end, y_end), width=5)




def white_cirle_small(): # de timeangivende linjer skal også kun være i ydersiden og vi laver derfor endnu en cirkel. dog lidt mindre en den første cirkel.
    pygame.draw.circle(screen, (255, 255, 255), (320, 240), 165)



def outer_circle(): # dette tegner den ydre cirkel der indeholder uret
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), 201, 5)


def draw_hands(): # Nu importerer vi tid og bruger denne til live at opdatere tre linjer der angiver timer minutter og sekunder.
    now = datetime.datetime.now()
    second = now.second
    minutes = now.minute
    hours = now.hour % 12
    seconds = second + (now.microsecond / 1000000) # vi tilføjer dividerer microsekunder med 1000000 da, hvis vi ikke gjorde dette ville sekund tallet være meget højt.
                                                   # for et eksempel hvis der var gået 1.5 sekunder 
                                                   # og vi ikke havde dividerer ville vi have en int værdi i seconds på: 1 + 500.000 = 500.001 sekunder

    angle_second = (2 * math.pi * seconds / 60) - (math.pi / 2) # her udregnes vinklen som sekundviseren har. 
                                                                # Vi har igen en hel rotation i 2 * pi og 60 sekunder svarer til 1 * (2 * pi).
                                                                # Vi minusser med en kvart rotation en fuld rotation ellers ville starte klokken ved 3 timers punktet

    endx = 320 + 150 * math.cos(angle_second) # vi udregner endepunkterne for linjen(sekundviseren) på samme måde som vi gjorde ved small_radiating_lines()
                                              # Dog er angle_second her en opdaterende værdi der følger tiden.
    endy = 240 + 150 * math.sin(angle_second) 
    pygame.draw.line(screen, (0, 0, 0), (320, 240), (endx, endy), 2)


    angle_minute = (2 * math.pi * (minutes / 60) - (math.pi / 2)) # vi dividerer minutes med 60 da 60 minutter svarer til en time og henholdsvis en fuld rotation. 
                                                                  # vi minusser igen og af samme anledning som før med pi / 2
    endx = 320 + 165 * math.cos(angle_minute)
    endy = 240 + 165 * math.sin(angle_minute)
    pygame.draw.line(screen, (0, 0, 0), (320, 240), (endx, endy), 4)

    angle_hour = (2 * math.pi * (hours / 12) - (math.pi / 2)) # samme logik her som med de andre visere. vi dividere hours med 12 da 12 timer svarer til en hel rotation
    endx = 320 + 90 * math.cos(angle_hour)
    endy = 240 + 90 * math.sin(angle_hour)
    pygame.draw.line(screen, (0, 0, 0), (320, 240), (endx, endy), 6)
    


def clock(): # vi samler hele uret i den rigtige rækkefølge i en funktion for at det ikke ser lige så cluttered ud
    small_radiating_lines()
    white_cirle_big()
    radiating_lines()
    white_cirle_small()
    outer_circle()
    draw_hands()
    pygame.display.flip()
    print()

while True:
    for event in pygame.event.get(): # det der sker her er at vi kører clock() indtil event.type == pygame.QUIT hvilket vil sige at uret kører indtil vi trykker på kryds.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    clock()
