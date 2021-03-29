from threading import main_thread
import pygame
from pygame import image
import gui_loader


pygame.init()
pygame.font.init()
limit_input = int(input('Choose number of post to see: '))
subreddit_input = str(input('Choose subreddit: '))
width = 1000
height = 900
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('ReddVisualPy')
gui = gui_loader.gui(window,limit_input, subreddit_input)

def main():
    
    running = True
    

    while running:

        pygame.time.delay(40)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
            gui.gui_event_handler(event)

        window.fill((4, 0, 36)) 
         
        gui.main_page()
        gui.main_page_image_displayer()





        pygame.display.update()








             

    pygame.quit()

if __name__ == '__main__':
    main()

