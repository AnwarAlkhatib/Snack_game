import pygame
import time
import random

# Farben
black = (0, 0, 0)#snake
red = (255, 0, 0)#Screen nach dem man verliert
green = (0, 255, 0)#Screen Während des spiels
blue = (0, 0, 255) # farbe des schriffts

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
width = 600
height = 400
dis = pygame.display.set_mode((width, height))#Variable dis für die Umgebung (Das Fenster)
pygame.display.set_caption('Snake Anwar Game')#Überschrift am Fenster

# Snake-Parameter
snake_block = 10 #10*Pixel größe der Segmente aus denen die schlange besteht. 
snake_speed = 15 #Virtuelle umgebung wird 15 mal pro Sekunde aktualiesiert.

# Schriftart
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Funktion um die schlange zu zeichnen. 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#funktion um eine Nachricht am Bildschrim zu schreiben. 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Hauptspiel-Schleife
def gameLoop():  
    game_over = False   #variablen Definieren um bedingungen später 
    game_close = False  #erstellen zu können

    x1 = width / 2   #Start Position auf x/y Koordinate für  
    y1 = height / 2  #die Schlange fest legen

    x1_change = 0 # hier werden die variablen erstellt die später helfen
    y1_change = 0 # um richtung des schlange steuern zu könen.  

    snake_List = []   #leere liste um die Position der Sigmenten des schlange zuspeichern 
    Length_of_snake = 1 #Variable die das wachstum des schlange darstellt

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over: #solange game_over False do:

        while game_close == True:
            dis.fill(red)# Farbe des Bildschirms wenn man das Spiel verliert. 
            message("You Lost! Press C-Play Again or Q-Quit", blue) # Nachricht und farbe der nachricht
            pygame.display.update()#diese Methode aktualisiert das Fenster und zeigt alle änderungen an 
            #"pygame.event.get()"   Dieser Funktion im event model gibt eine liste aller aktuellen Ereignisse zuruck  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:#man hat ein taste gedrückt 
                    if event.key == pygame.K_q: # wenn es q ist
                        game_over = True #spiel aus 
                        game_close = False#weiter
                    if event.key == pygame.K_c:#wenn es c ist
                        gameLoop() #spiel noch mal starten.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#versuch man das fenster zu schließen...
                game_over = True #spiel aus
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:# Drückt man linken Pfeiltaste
                    x1_change = -snake_block  #bewegt man sich nach links. Auf x Achse richtung negativen Bereich. 
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #Rechte Pfeiltaste
                    x1_change = snake_block       #auf x Achse richtung Positiven Bereich. 
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0: #stell sicher das die schlange nicht gegen die wand läuft ansonsten 
            game_close = True                               #Spiel verloren 

        x1 += x1_change   #Nachdem die schlange in bestimmte richtungen gelenkt wurde 
        y1 += y1_change   #werden die daten der richtung in die koordinaten der schlange gespeichert
        dis.fill(blue)  #farbe des spielfeldes während des spiels ist blau. 
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])#Zeichne das Essen
        
        snake_Head = []#neue liste um die Koordinate des schlangenKopf zu speichern.
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)#Ich gebe die koordinaten des schlangenkopf für die Liste die die Segmente der schlange speichert
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        #hier wird überprüft, ob der Kopf der schlange mit einem der Segmente der schlange Kollisiert 
        for x in snake_List[:-1]: 
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        #Hier wächst die schlange wenn sie essen frisst 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    
    quit()

gameLoop()
