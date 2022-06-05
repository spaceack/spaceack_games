# coding:utf8
import pygame
from pygame.locals import *
import sys

def init_game(caption):
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(caption)
    return screen

def play_music():
    pygame.mixer.music.load('sp.mp3')
    pygame.mixer.music.play(-1, 0.0)

def body(screen):
    bg = (255, 255, 200)
    fontObj = pygame.font.Font('Songti.ttc', 26)

    zongzi = pygame.image.load("zongzi.png")
    mask = pygame.image.load("mask.png")
    freeze_mask = pygame.image.load("mask.png")
    zongzi = pygame.transform.smoothscale(zongzi, (500, 700))
    mask = pygame.transform.smoothscale(mask, (180, 180))
    freeze_mask = pygame.transform.smoothscale(freeze_mask, (180, 180))
    freeze_mask.set_alpha(200)
    mask_x = 580
    mask_y = 610

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mask_y -= 10
                if event.key == pygame.K_DOWN:
                    mask_y += 10
                if event.key == pygame.K_LEFT:
                    mask_x -= 10
                if event.key == pygame.K_RIGHT:
                    mask_x += 10

        screen.fill(bg)
        screen.blit(zongzi,(200,200))
        screen.blit(freeze_mask, (360,540))
        
        screen.blit(mask, (mask_x, mask_y))
        if mask_x == 360 and mask_y == 540:
            textSurfaceObj = fontObj.render('你真棒，粽宝宝已成功佩戴好口罩！', False, (255,10,10))# 配置要显示的文字
            screen.blit(textSurfaceObj, (50,50))
        else:
            textSurfaceObj = fontObj.render('预防疫情不松懈,请按图片的位置给粽宝宝佩戴好口罩！', False, (255,10,10))# 配置要显示的文字
            screen.blit(textSurfaceObj, (50,50))
        pygame.display.flip()

if __name__ == '__main__':
    screen = init_game(caption="Spaceack 祝大家端午安康😆")
    play_music()
    body(screen)
