import pygame
import sys
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("ChatBot")
screen =  pygame.display.set_mode((1370,389),pygame.FULLSCREEN ,pygame.NOFRAME)
#screen =  pygame.display.set_mode((1370,589),0,32)

bfont = pygame.font.SysFont(None,200)
sfont = pygame.font.SysFont(None,50)
font = pygame.font.SysFont(None,90)

def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text ,font ,colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj,textrect)
    
click = False

def main_menu():
    click = False
    while True:
        img = pygame.image.load('/home/kalremo/ai screen.jpg').convert()
        img = pygame.transform.smoothscale(img,screen.get_size())
        imgrect = img.get_rect()
        screen.blit(img, imgrect)
        draw_text("Introducing",bfont, (184,167,209),screen, 800,400)
        draw_text("ChatBot",bfont, (184,167,209),screen, 1100,550)
        draw_text("Say Something!",sfont, (184,167,209),screen, 830,700) 
        
        mx, my = pygame.mouse.get_pos()
        
        settings_bttn = pygame.Rect(850, 750, 200, 50)
        devices_bttn = pygame.Rect(1150, 750, 200, 50)
        faq_bttn = pygame.Rect(1450, 750, 200, 50)
        
        if settings_bttn.collidepoint((mx,my)):
            if click:
                settings()
        if devices_bttn.collidepoint((mx,my)):
            if click:
                devices()
        if faq_bttn.collidepoint((mx,my)):
            if click:
                faq()
        
        pygame.draw.rect(screen, (161, 142, 191), settings_bttn)
        pygame.draw.rect(screen, (161, 142, 191), devices_bttn)
        pygame.draw.rect(screen, (161, 142, 191), faq_bttn)
        
        draw_text("Settings",sfont, (41,34,51),screen, 880,760)
        draw_text("Devices",sfont, (41,34,51),screen, 1185,760)
        draw_text("FAQs",sfont, (41,34,51),screen, 1505,760)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()
        mainClock.tick(60)

def settings():
    running = True
    click = False
    while running:
        screen.fill((211,206,219))
        draw_text("Settings",font, (41,34,51),screen, 840,80)
        
        mx, my = pygame.mouse.get_pos()
        
        back_bttn = pygame.Rect(1250, 850, 200, 50)
        
        if back_bttn.collidepoint((mx,my)):
            if click:
                running = False
                
        pygame.draw.rect(screen, (161, 142, 191), back_bttn)
        draw_text("Back",sfont, (41,34,51),screen, 1305,860)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        pygame.display.update()
        mainClock.tick(60)
        
def devices():
    running = True
    click = False
    while running:
        screen.fill((211,206,219))
        draw_text("Devices",font, (41,34,51),screen, 830,80)
        mx, my = pygame.mouse.get_pos()
        
        back_bttn = pygame.Rect(1250, 850, 200, 50)
        
        if back_bttn.collidepoint((mx,my)):
            if click:
                running = False
                
        pygame.draw.rect(screen, (161, 142, 191), back_bttn)
        draw_text("Back",sfont, (41,34,51),screen, 1305,860)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
          
        pygame.display.update()
        mainClock.tick(60)

def faq():
    running = True
    click = False
    while running:
        screen.fill((211,206,219))
        draw_text("Frequently Asked Questions",font, (41,34,51),screen, 560,80)
        mx, my = pygame.mouse.get_pos()
        
        back_bttn = pygame.Rect(1250, 850, 200, 50)
        
        if back_bttn.collidepoint((mx,my)):
            if click:
                running = False
                
        pygame.draw.rect(screen, (161, 142, 191), back_bttn)
        draw_text("Back",sfont, (41,34,51),screen, 1305,860)
        
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
          
        pygame.display.update()
        mainClock.tick(60)
        

main_menu()

