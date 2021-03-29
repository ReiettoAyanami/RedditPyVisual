import pygame
import utils


class Button:
    def __init__(self,surface,IDLE_COLOR,REPLACE_COLOR,attributes,border_r,font,text,antialias_state,TEXT_IDLE_COLOR,TEXT_REPLACE_COLOR):
        self.IDLE_COLOR = IDLE_COLOR
        self.REPLACE_COLOR = REPLACE_COLOR
        self.surface = surface
        self.color = self.IDLE_COLOR
        self.attributes = attributes
        self.border_r = border_r
        self.font = font
        self.text = text
        self.antialias = antialias_state
        self.TEXT_IDLE_COLOR = TEXT_IDLE_COLOR 
        self.text_color = self.TEXT_IDLE_COLOR
        self.TEXT_REPLACE_COLOR = TEXT_REPLACE_COLOR
        

        

    def show(self):
        x,y,w,h = self.attributes            
        pygame.draw.rect(self.surface,self.color,self.attributes,border_radius = self.border_r)
        button_text = self.font.render(self.text,self.antialias,self.text_color)
        text_rect = button_text.get_rect(center = (x+w/2,y+h/2))
        self.surface.blit(button_text,text_rect)


    def is_held(self):
        x,y,w,h = self.attributes
        if utils.mouse_overlaps(x,y,w,h) and pygame.mouse.get_pressed()[0]:
            self.text_color = self.TEXT_REPLACE_COLOR
            self.color = self.REPLACE_COLOR
            return True
        else:
            self.text_color = self.TEXT_IDLE_COLOR
            self.color = self.IDLE_COLOR
            return False


    def gets_clicked(self,event):
        x,y,w,h = self.attributes
        if utils.mouse_overlaps(x,y,w,h) and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.text_color = self.TEXT_REPLACE_COLOR
                self.color = self.REPLACE_COLOR
                return True
        else: 
            self.text_color = self.TEXT_IDLE_COLOR
            self.color = self.IDLE_COLOR
            return False

            
