from sr_ram import *
import pygame
import sys
import win32.lib.win32con as win32con
import win32.win32gui as win32gui

class Text:
    def __init__(self,text:list,font:pygame.font.Font,color:list,pos=None):
        self.text=text
        self.font=font
        self.size=self.font.size('A')[1]
        self.color=color
        self.pos = pos
        if pos=None:
            self.pos = []
            for i in range(len(txt)):
                self.pos.append([0,self.size*i])
        self.rendered=[None for _ in range(len(text))]
        for i in range(len(text)):
            self.render(i)
    def render(self,index):
        self.rendered[index] = self.font.render(self.text[index],False,self.color)
    def update(self,index,val=None,pos=None):
        self.text[index] = val
        self.pos[index] = pos
        if val != None:
            self.render(index)
    def display(self,surf):
        for i in range(len(self.rendered)):
            surf.blit(self.rendered[i],self.pos[i])

#Initialize
pygame.init()

#Set up display
surfSize = (read("xResolution",0,True), read("yResolution",0,True))
surf = pygame.display.set_mode(surfSize)

#Get Surf Info
hwnd = pygame.display.get_wm_info()["window"]

# This will set the opacity and transparency color key of a layered window
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                       hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, 0b00000000100000000000000010000000, 0, win32con.LWA_COLORKEY)
#DWORD with 4 bytes -> RGBA -> ABGR

#Configure it to be always at the top
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

#Text
txtColor=color=[255,0,0]
txt=Text(text=['Sonic R RAM Visual Test',
               ' '],
         font=pygame.font.SysFont('monospace',48,bold=True),
         color=txtColor)

while True:
    #Event
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Rendering
    surf.fill((128,0,128))
    txt.update(1,bitfield("controlBitfieldP1"))
    txt.display(surf)
    pygame.display.update()
    
