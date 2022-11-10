import pygame

def ExecutePyGame():
	#Initialize pygame modúl.
	pygame.init()

	pygame.display.set_caption("MAYA")

	screen = pygame.display.set_mode((800,500))

	isGameRunning = True

	while isGameRunning:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				isGameRunning = False

if __name__=="__main__":
	ExecutePyGame()
