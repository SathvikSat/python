import pygame
import time
import random
pygame.init()  #calls init func

display_width = 800
display_height = 1000

black = (0,0,0) #tuple for color; not default in pygame
white = (255,255,255) #tuple RGB
red = (255,0,0)

car_width = 250

#game character shapes etc and transperant

gameDisplay = pygame.display.set_mode((display_width, display_height)) #tuple h and w
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock() #frames/sec imposes on everything on game

carImg = pygame.image.load('car1.png')

def things(thingx, thingy, thingw, thingh, color):
	#pygames draw functionality where and color, coordinates and yeah hsape
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
	gameDisplay.blit(carImg,(x,y)) #trying to background the surface
 
def text_objects(text, font):
		textSurface = font.render(text, True, red)
		return textSurface, textSurface.get_rect() 

	


def message_display(text): 
		largeText = pygame.font.Font('freesansbold.ttf', 115) #font style and size
		TextSurf, TextRect = text_objects(text, largeText) #box encasing text, rect that contains it returns text surf and rect.
	#to center on screen
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect) #to kinda like draw it to the screen 
		pygame.display.update() 
		time.sleep(2)
		
		game_loop()


def crash():
	message_display('You Crashed!')


def game_loop():

	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0
	thing_startx = random.randrange(0, display_width) #starting point of block! , randomly
	thing_starty = -600 #y direction start from outside the screen
	thing_speed = 7
	thing_width = 100
	thing_height = 100
#game loop i.e logic quit or crash case
	gameExit = False

	while not gameExit: 
		#event handling
		for event in pygame.event.get(): #any event cursor, keyboard etc gets it , list of events that happens is created per frame per sec
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
					x_change = 5
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
			#print(event) #print events that occur
		gameDisplay.fill(white)
		#def things(thingx, thingy, thingw, thingh, color):
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		#y needs to be varied
		thing_starty += thing_speed


		car(x,y)
		
		if x > display_width - car_width or x< 0:
			crash()	
		
		if thing_starty > display_height:  #to repeat the incoming of blocks
			thing_starty = 0 - thing_height  
			thing_startx = random.randrange(0, display_width-thing_width)

		if y < thing_starty + thing_height:
			print('y crossover')
			
			if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width or thing_startx > x and thing_startx + thing_width < x+ car_width:
				
				print('x crossover')
				crash()

		pygame.display.flip() #or pygame.display.flip; update perticular parameter
		clock.tick(50) #To run this whole loop speed ;frames from second

game_loop()
pygame.quit()
quit()
