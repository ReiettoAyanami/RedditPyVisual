import pygame
import requests
import re
import tkinter
from tkinter import filedialog

def mouse_overlaps(x,y,w,h):
    mX, mY = pygame.mouse.get_pos()

    if mX > x and mX < x+w and mY < y + h and  mY  > y:
                #print(mX,mY,_scale,'isOver')
                
        return True
    else: return False

        
def download(url):
    

    root = tkinter.Tk()

    root.withdraw()

    folder = filedialog.askdirectory()

    file_name = url.split("/")

    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    
    if "." not in file_name:
         file_name += ".jpg"
    #print(file_name)
    
    r = requests.get(url)
    
    #print(folder)

    with open(folder + '/' +  file_name,"wb") as f:
        f.write(r.content)
