import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"
import pygame
import random
import math
import matplotlib.pyplot as plt
import numpy as np

#Constants
HEIGHT = 720
WIDTH = 720
FPS = 30
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (100, 64.7, 0)
MIX = (100, 255, 100)

#Functions
def draw_text(text, surf, size, x, y, colour):
    font = pygame.font.Font(font_name, size)
    text_surf = font.render(text, True, colour)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surf, text_rect)

def draw_text2(text, surf, size, x, y, colour):
    font = pygame.font.Font(font_name, size)
    text_surf = font.render(text, True, colour)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surf, text_rect)

def input_value(string, string_x, string_y, val_x, val_y, colour):
    global running
    draw_text(string, screen, 18, string_x, string_y, colour)
    waiting = True
    string = ''
    screen.fill(ORANGE, rect = (val_x, val_y - 7.5, WIDTH / 10, 30))
    while waiting:
        for te in pygame.event.get():
            if te.type == pygame.QUIT:
                running = False
                waiting = False
            if te.type == pygame.KEYDOWN:
                if te.key == pygame.K_RETURN:   
                    waiting = False
                    A.append(int(string))
                elif te.key == pygame.K_BACKSPACE:
                    n = len(string)
                    string = string[:n-1]
                    screen.fill(ORANGE, rect = (val_x, val_y, WIDTH / 10, 15))
                else:
                    string += te.unicode
        text_surf = base_font.render(string, False, WHITE)
        screen.blit(text_surf, (val_x+5, val_y))
        pygame.display.flip()

def input_value2(string, string_x, string_y, val_x, val_y, colour, real, imag):
    global running
    global parameter_page
    draw_text(string, screen, 18, string_x, string_y, colour)
    waiting = True
    string = ''
    screen.fill(ORANGE, rect = (val_x, val_y - 7.5, WIDTH / 10, 30))
    screen.fill(BLACK, rect = (val_x + 15, val_y + 30, WIDTH / 10, 30))
    draw_text('j', screen, 14, val_x + 5, val_y + 35, WHITE)
    pygame.draw.circle(screen, WHITE, (val_x+5, val_y+33), 1)
    while waiting:
        for te in pygame.event.get():
            if te.type == pygame.QUIT:
                running = False
                waiting = False
                parameter_page = False
            if te.type == pygame.KEYDOWN:
                if te.key == pygame.K_RETURN:   
                    waiting = False
                    real.append(int(string))
                elif te.key == pygame.K_BACKSPACE:
                    n = len(string)
                    string = string[:n-1]
                    screen.fill(ORANGE, rect = (val_x, val_y, WIDTH / 10, 15))
                else:
                    string += te.unicode
        text_surf = base_font.render(string, False, WHITE)
        screen.blit(text_surf, (val_x+5, val_y))
        pygame.display.flip()
    if running:
        waiting = True
        screen.fill(ORANGE, rect = (val_x + 15, val_y + 30, WIDTH / 10, 30))
    string = ' '
    while waiting:
        for te in pygame.event.get():
            if te.type == pygame.QUIT:
                running = False
                waiting = False
            if te.type == pygame.KEYDOWN:
                if te.key == pygame.K_RETURN:   
                    waiting = False
                    imag.append(int(string))
                elif te.key == pygame.K_BACKSPACE:
                    n = len(string)
                    string = string[:n-1]
                    screen.fill(ORANGE, rect = (val_x+15, val_y+35, WIDTH / 10, 15))
                else:
                    string += te.unicode
        text_surf = base_font.render(string, False, WHITE)
        screen.blit(text_surf, (val_x+20, val_y + 35))
        pygame.display.flip()

def ytoz(zreal, zimag):
    try :
        y11 = complex(yreal[0], yimag[0])
        y12 = complex(yreal[1], yimag[1])
        y21 = complex(yreal[2], yimag[2])
        y22 = complex(yreal[3], yimag[3])
        det = y11 * y22 - y12 * y21
        zreal.append(round((y22 / det).real, 4))
        zimag.append(round((y22 / det).imag, 4))
        zreal.append(round((-y12 / det).real, 4))
        zimag.append(round((-y12 / det).imag, 4))
        zreal.append(round((-y21 / det).real, 4))
        zimag.append(round((-y21 / det).imag, 4))
        zreal.append(round((y11 / det).real, 4))
        zimag.append(round((y11 / det).imag, 4))
    except:
        zreal = []
        zimag = []

def ztoy(yreal, yimag):
    try:
        z11 = complex(zreal[0], zimag[0])
        z12 = complex(zreal[1], zimag[1])
        z21 = complex(zreal[2], zimag[2])
        z22 = complex(zreal[3], zimag[3])
        det = z11 * z22 - z12 * z21
        yreal.append(round((z22 / det).real, 4))
        yimag.append(round((z22 / det).imag, 4))
        yreal.append(round((-z12 / det).real, 4))
        yimag.append(round((-z12 / det).imag, 4))
        yreal.append(round((-z21 / det).real, 4))
        yimag.append(round((-z21 / det).imag, 4))
        yreal.append(round((z11 / det).real, 4))
        yimag.append(round((z11 / det).imag, 4))
    except:
        yreal = []
        yimag = []

def ytot(treal, timag):
    try:
        y11 = complex(yreal[0], yimag[0])
        y12 = complex(yreal[1], yimag[1])
        y21 = complex(yreal[2], yimag[2])
        y22 = complex(yreal[3], yimag[3])
        det = y12 * y21 - y11 * y22
        treal.append(round((-y22 / y21).real, 4))
        timag.append(round((-y22 / y21).imag, 4))
        treal.append(round((-1 / y21).real, 4))
        timag.append(round((-1 / y21).imag, 4))
        treal.append(round((det / y21).real, 4))
        timag.append(round((det / y21).imag, 4))
        treal.append(round((-y11 / y21).real, 4))
        timag.append(round((-y11 / y21).imag, 4))
    except:
        treal = []
        timag = []

def ttoy(yreal, yimag):
    try:
        A = complex(treal[0], timag[0])
        B = complex(treal[1], timag[1])
        C = complex(treal[2], timag[2])
        D = complex(treal[3], timag[3])
        yreal.append(round((D / B).real, 4))
        yimag.append(round((D / B).imag, 4))
        yreal.append(round(((B*C - A*D)/B).real, 4))
        yimag.append(round(((B*C - A*D)/B).imag, 4))
        yreal.append(round((-1 / B).real, 4))
        yimag.append(round((-1 / B).imag, 4))
        yreal.append(round((A / B).real, 4))
        yimag.append(round((A / B).imag, 4))
    except:
        yreal = []
        yimag = []

def ttoh(hreal, himag):
    try:
        A = complex(treal[0], timag[0])
        B = complex(treal[1], timag[1])
        C = complex(treal[2], timag[2])
        D = complex(treal[3], timag[3])
        hreal.append(round((B/D).real, 4))
        himag.append(round((B/D).imag, 4))
        hreal.append(round(((A*D - B*C)/D).real, 4))
        himag.append(round(((A*D - B*C)/D).imag, 4))
        hreal.append(round((-1/D).real, 4))
        himag.append(round((-1/D).imag, 4))
        hreal.append(round((C/D).real, 4))
        himag.append(round((C/D).imag, 4))
    except:
        hreal = []
        himag = []

def htot(treal, timag):
    try:
        h11 = complex(hreal[0], himag[0])
        h12 = complex(hreal[1], himag[1])
        h21 = complex(hreal[2], himag[2])
        h22 = complex(hreal[3], himag[3])
        treal.append(round(((h12*h21 - h11*h22)/h21).real, 4))
        timag.append(round(((h12*h21 - h11*h22)/h21).imag, 4))
        treal.append(round((-h11/h21).real, 4))
        timag.append(round((-h11/h21).imag, 4))
        treal.append(round((-h11/h21).real, 4))
        timag.append(round((-h11/h21).imag, 4))
        treal.append(round((-1/h21).real, 4))
        timag.append(round((-1/h21).imag, 4))
    except: 
        treal = []
        timag = []

def addtolist():
    try:
        ans.append("Z11 = " + str(complex(zreal[0], zimag[0])))
        ans.append("Z12 = " + str(complex(zreal[1], zimag[1])))
        ans.append("Z21 = " + str(complex(zreal[2], zimag[2])))
        ans.append("Z22 = " + str(complex(zreal[3], zimag[3])))
    except:
        ans.append("Z11 =  NaN")
        ans.append("Z12 =  NaN")
        ans.append("Z21 =  NaN")
        ans.append("Z22 =  NaN")
    try:
        ans.append("A = " + str(complex(treal[0], timag[0])))
        ans.append("B = " + str(complex(treal[1], timag[1])))
        ans.append("C = " + str(complex(treal[2], timag[2])))
        ans.append("D = " + str(complex(treal[3], timag[3])))
    except:
        ans.append("A =  NaN")
        ans.append("B =  NaN")
        ans.append("C =  NaN")
        ans.append("D =  NaN")
    try:
        ans.append("h11 = " + str(complex(hreal[0], himag[0])))
        ans.append("h12 = " + str(complex(hreal[1], himag[1])))
        ans.append("h21 = " + str(complex(hreal[2], himag[2])))
        ans.append("h22 = " + str(complex(hreal[3], himag[3])))
    except:
        ans.append("h11 =  NaN")
        ans.append("h12 =  NaN")
        ans.append("h21 =  NaN")
        ans.append("h22 =  NaN")
    try:
        ans.append("Y11 = " + str(complex(yreal[0], yimag[0])))
        ans.append("Y12 = " + str(complex(yreal[1], yimag[1])))
        ans.append("Y21 = " + str(complex(yreal[2], yimag[2])))
        ans.append("Y22 = " + str(complex(yreal[3], yimag[3])))
    except:
        ans.append("Y11 =  NaN")
        ans.append("Y12 =  NaN")
        ans.append("Y21 =  NaN")
        ans.append("Y22 =  NaN")

def check(param):
    if len(param) != 4:
        for i in range(4):
            param.append("NaN")

# Setting up screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("NETWORKS ANALYSIS PROJECT")
clock = pygame.time.Clock()

#All Images and fonts
loc = os.path.dirname(os.path.realpath(__file__))
font_name = pygame.font.match_font('arial', bold = True)
base_font = pygame.font.Font(None, 25)
background1 = pygame.image.load(os.path.join(loc, 'background1.jpg')).convert()
background1_rect = background1.get_rect()
background2 = pygame.image.load(os.path.join(loc, 'background2.jpeg')).convert()
background2_rect = background1.get_rect()
background3 = pygame.image.load(os.path.join(loc, 'background3.jpg')).convert()
background3_rect = background3.get_rect()
op1 = pygame.image.load(os.path.join(loc, 'T-PI.png')).convert()
op12 = pygame.transform.scale(op1, (380,180))
op12_rect = op12.get_rect()
op12_rect.center = (200, 150)
op5 = pygame.image.load(os.path.join(loc, 'rlc.jpg')).convert()
op5 = pygame.transform.scale(op5, (380,180))
op5_rect = op5.get_rect()
op5_rect.center = (200, 600)
yparam = pygame.image.load(os.path.join(loc, 'Y-parameter.jpg')).convert()
yparam_rect = yparam.get_rect()
zparam = pygame.image.load(os.path.join(loc, 'Z-parameter.jpg')).convert()
zparam_rect = zparam.get_rect()
var = [YELLOW] * 4
scnd_page = [MIX] * 4
running = True
main_page = True
parameter_page = False

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # Quiting
        if event.type == pygame.QUIT:
            running = False

        # Highliting
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            if main_page and x > 75 and x < 91 and y > 73 and y < 87:
                var[0] = BLUE
            elif main_page and x > 75 and x < 91 and y > 160 and y < 179:
                var[1] = BLUE
            elif main_page and x > 75 and x < 91 and y > 341 and y < 358:
                var[2] = BLUE
            elif main_page and  x > 75 and x < 91 and y > 540 and y < 557:
                var[3] = BLUE
            elif main_page:
                var = [YELLOW] * 4
            
        # Click detection
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Operation 1
            if main_page and x > 75 and x < 91 and y > 73 and y < 87:
                main_page = False
                A = []
                R = []
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                op1_rect = op1.get_rect()
                op1_rect.center = (360, 200)
                screen.blit(op1, op1_rect)
                draw_text("PI to T network conversion", screen, 18, 360, 50, GREEN)
                input_value("ENTER Zab(ohms): ", 100, 345, 187, 350, RED)
                if running: input_value("ENTER Zbc(ohms): ", 100, 405, 187, 410, RED)
                if running: input_value("ENTER Zca(ohms): ", 100, 465, 187, 470, RED)
                if running: 
                    tot = A[0] + A[1] + A[2]
                    R.append(round(A[0] * A[2] / tot, 2))
                    R.append(round(A[0] * A[1] / tot, 2))
                    R.append(round(A[2] * A[1] / tot, 2))
                    ans1 = "Za = " + str(R[0]) + " ohm"
                    ans2 = "Zb = " + str(R[1]) + " ohm"
                    ans3 = "Zc = " + str(R[2]) + " ohm"
                    draw_text2(ans1, screen, 18, 400, 345, YELLOW)
                    draw_text2(ans2, screen, 18, 400, 405, YELLOW)
                    draw_text2(ans3, screen, 18, 400, 465, YELLOW)
                    draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN)
            # Operation 2
            if main_page and x > 75 and x < 91 and y > 160 and y < 179:
                main_page = False
                A = []
                R = []
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                op1_rect = op1.get_rect()
                op1_rect.center = (360, 200)
                screen.blit(op1, op1_rect)
                draw_text("T to PI network conversion", screen, 18, 360, 50, GREEN)
                input_value("ENTER Za(ohms): ", 100, 345, 187, 350, GREEN)
                if running: input_value("ENTER Zb(ohms): ", 100, 385, 187, 390, GREEN)
                if running: input_value("ENTER Zc(ohms): ", 100, 425, 187, 430, GREEN)
                if running:
                    tot = A[0] * A[1] + A[1] * A[2] + A[2] * A[0]
                    R.append(round(tot / A[2], 2))
                    R.append(round(tot / A[0], 2))
                    R.append(round(tot / A[1], 2))
                    ans1 = "Zab = " + str(R[0]) + " ohm"
                    ans2 = "Zbc = " + str(R[1]) + " ohm"
                    ans3 = "Zca = " + str(R[2]) + " ohm"
                    draw_text2(ans1, screen, 18, 400, 345, YELLOW)
                    draw_text2(ans2, screen, 18, 400, 385, YELLOW)
                    draw_text2(ans3, screen, 18, 400, 425, YELLOW)
                    draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN)
            # Operation 3
            if main_page and x > 75 and x < 91 and y > 341 and y < 358:
                main_page = False
                parameter_page = True
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                draw_text("Parameter Conversion", screen, 18, 360, 20, GREEN)
                zreal, zimag = [], []
                yreal, yimag = [], []
                hreal, himag = [], []
                treal, timag = [], []
                for i in range(4):
                    pygame.draw.circle(screen, scnd_page[i], (84 + 150 * i, 81), 10)
                draw_text2("Y", screen, 18, 100, 71, WHITE)
                draw_text2("Z", screen, 18, 250, 71, WHITE)
                draw_text2("ABCD", screen, 18, 400, 71, WHITE)
                draw_text2("h", screen, 18, 550, 71, WHITE)
                previous = False
                # Clicking
                while parameter_page:
                    for sub in pygame.event.get():
                        if sub.type == pygame.QUIT:
                            parameter_page = False
                            running = False
                        if sub.type == pygame.MOUSEMOTION:
                            x, y = pygame.mouse.get_pos()
                            if x > 72 and x < 90 and y > 70 and y < 89:
                                pygame.draw.circle(screen, RED, (84 + 150 * 0, 81), 10)
                            elif x > 222 and x < 240 and y > 70 and y < 89:
                                pygame.draw.circle(screen, RED, (84 + 150 * 1, 81), 10)
                            elif x > 372 and x < 390 and y > 70 and y < 89:
                                pygame.draw.circle(screen, RED, (84 + 150 * 2, 81), 10)
                            elif x > 522 and x < 540 and y > 70 and y < 89:
                                pygame.draw.circle(screen, RED, (84 + 150 * 3, 81), 10)
                            else:
                                for i in range(4):
                                    pygame.draw.circle(screen, MIX, (84 + 150 * i, 81), 10)
                        if sub.type == pygame.MOUSEBUTTONDOWN:
                            X, Y = pygame.mouse.get_pos()
                            if not previous and X > 72 and X < 90 and Y > 70 and Y < 89:
                                previous = True
                                parameter_page = False
                                input_value2("Y11", 25, 150, 55 ,150, GREEN, yreal, yimag)
                                if running: input_value2("Y12", 25, 250, 55 ,250, GREEN, yreal, yimag)
                                if running: input_value2("Y21", 25, 350, 55 ,350, GREEN, yreal, yimag)
                                if running: input_value2("Y22", 25, 450, 55 ,450, GREEN, yreal, yimag)
                                if running:                                    
                                    ytoz(zreal, zimag), ytot(treal, timag), ttoh(hreal, himag)
                                    check(zreal), check(treal), check(hreal)
                                    ans = []
                                    addtolist()
                                    for j in range(3):
                                        for i in range(4):
                                            draw_text2(ans[4*j+i], screen, 16, 155 + 190*j, 140 + 100*i, YELLOW)
                            if not previous and X > 222 and X < 240 and Y > 70 and Y < 89:
                                parameter_page = False
                                previous = True
                                input_value2("Z11", 205, 150, 235 ,150, GREEN, zreal, zimag)
                                if running: input_value2("Z12", 205, 250, 235 ,250, GREEN, zreal, zimag)
                                if running: input_value2("Z21", 205, 350, 235 ,350, GREEN, zreal, zimag)
                                if running: input_value2("Z21", 205, 450, 235 ,450, GREEN, zreal, zimag)
                                if running:
                                    ztoy(yreal, yimag), ytot(treal, timag), ttoh(hreal, himag)
                                    check(yreal), check(treal), check(hreal)
                                    ans = []
                                    addtolist()
                                    for i in range(4):
                                        draw_text2(ans[12+i], screen, 16, 10, 140 + 100*i, YELLOW)
                                    for j in range(1, 3):
                                        for i in range(4):
                                            draw_text2(ans[4*j+i], screen, 16, 155 + 190*j, 140 + 100*i, YELLOW)
                            if not previous and X > 372 and X < 390 and Y > 70 and Y < 89:
                                parameter_page = False
                                previous = True
                                input_value2("A", 355, 150, 385 ,150, GREEN, treal, timag)
                                if running: input_value2("B", 355, 250, 385 ,250, GREEN, treal, timag)
                                if running: input_value2("C", 355, 350, 385 ,350, GREEN, treal, timag)
                                if running: input_value2("D", 355, 450, 385 ,450, GREEN, treal, timag)
                                if running:
                                    ttoy(yreal, yimag), ytoz(zreal, zimag), ttoh(hreal, himag)
                                    check(yreal), check(zreal), check(hreal)
                                    ans = []
                                    addtolist()
                                    for i in range(4):
                                        draw_text2(ans[i], screen, 16, 185, 120 + 100*i, YELLOW)
                                    for i in range(4):
                                        draw_text2(ans[8+i], screen, 16, 140 + 190*2, 120 + 100*i, YELLOW)
                                    for i in range(4):
                                        draw_text2(ans[12+i], screen, 16, 10, 160 + 100*i, YELLOW)
                            if not previous and X > 522 and X < 540 and Y > 70 and Y < 89:
                                parameter_page = False
                                previous = True
                                input_value2("h11", 505, 150, 535 ,150, GREEN, hreal, himag)
                                if running: input_value2("h12", 505, 250, 535 ,250, GREEN, hreal, himag)
                                if running: input_value2("h21", 505, 350, 535 ,350, GREEN, hreal, himag)
                                if running: input_value2("h22", 505, 450, 535 ,450, GREEN, hreal, himag)
                                if running:
                                    htot(treal, timag), ttoy(yreal, yimag), ytoz(zreal, zimag)
                                    check(yreal), check(zreal), check(treal)
                                    ans = []                                                                        
                                    addtolist()
                                    for i in range(4):
                                        draw_text2(ans[i], screen, 16, 160, 160 + 100*i, YELLOW)
                                    for i in range(4):
                                        draw_text2(ans[4+i], screen, 16, 160 + 190, 120 + 100*i, YELLOW)
                                    for i in range(4):
                                        draw_text2(ans[12+i], screen, 16, 10, 120 + 100*i, YELLOW)
                    pygame.display.flip()
                draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN)
            # Operation 4
            if main_page and  x > 75 and x < 91 and y > 540 and y < 557:
                main_page = False
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                op5_newrect = op5.get_rect()
                op5_newrect.center = (360, 150)
                draw_text("Series RLC Circuit Analysis", screen, 18, 360, 20, GREEN)
                screen.blit(op5, op5_newrect)
                A = []
                input_value("ENTER the Resistance of the RLC Circuit(ohm): ", 210, 280, 430, 285, GREEN)
                if running: input_value("ENTER the Inductance of the RLC Circuit (mH): ", 210, 310, 430, 315, GREEN)
                if running: input_value("ENTER the Capacitance of the RLC Circuit (uF): ", 212, 340, 430, 345, GREEN)
                if running: input_value("ENTER the frequency of the sinusoidal wave(HZ): ", 215, 370, 430, 375, GREEN)
                if running:
                    pie = 2 * math.pi
                    omega = round(2 * 3.14 * A[3], 2)
                    I_rx = round(omega * A[1] * 0.001, 2)
                    C_rx = round(1000000 / (omega * A[2]), 2)
                    Z_imp = round(math.sqrt(A[0] ** 2 + (C_rx - I_rx) ** 2), 2)
                    phase_rad = round(math.atan((I_rx - C_rx) / A[0]), 3)
                    phase_deg = round(phase_rad * 180 / math.pi, 3)
                    res_freq = round(10000 / (2 * math.pi * math.sqrt(A[1] * A[2] * 0.1)), 3)
                    q_fact = round((2 * math.pi * res_freq * A[1] / A[0]) * 0.001, 3)
                    band = round(A[0] * 1000 / (2 * math.pi * A[1]), 2)
                    x_axis = np.arange(1, 8 * res_freq, 0.001)
                    y_axis = np.sqrt(A[0] ** 2 + (pie*x_axis*A[1]*0.001 - (10 ** 6/(A[2]*x_axis*pie))) ** 2)
                    draw_text2(chr(969) + " = " + str(omega) + " rad/s", screen, 18, 100, 440, RED)
                    draw_text2("XL = " + str(I_rx) + " ohms", screen, 18, 100, 480, RED)
                    draw_text2("XC = " + str(C_rx) + " ohms", screen, 18, 100, 520, RED)
                    draw_text2("Z = " + str(Z_imp) + " ohms", screen, 18, 100, 560, RED)
                    draw_text2(chr(981) + " = " + str(phase_rad) + " rad  = " + str(phase_deg) + "deg", screen, 18, 350, 440, RED)
                    draw_text2("Resonant frequency fo = " + str(res_freq) + " HZ", screen, 18, 350, 480, RED)
                    draw_text2("Q-factor Q = " + str(q_fact), screen, 18, 350, 520, RED)
                    draw_text2("Bandwidth = " + str(band) + " Hz", screen, 18, 350, 560, RED)
                    pygame.display.flip()
                    plt.xlabel('frequency(fo)')
                    plt.ylabel('Impedence (ohm)')
                    plt.plot(x_axis, y_axis, color = 'red')
                    plt.annotate('Resonance', (res_freq, A[0]), color = 'blue')
                    plt.scatter(res_freq, A[0])
                    plt.title('Resonance Graph')
                    plt.show()
                    draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 640, GREEN)
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                main_page = True
                scnd_page = False
                var = [YELLOW] * 4
                scnd_page = [MIX] * 4
    if main_page == True:
        screen.fill(BLACK)
        screen.blit(background2, background2_rect)
        draw_text("CLICK ON THE YELLOW BUTTON!!", screen, 18, 360, 10, RED)
        draw_text("PI to T network conversion", screen, 18, 220, 70, WHITE)
        draw_text("T to PI network conversion", screen, 18, 220, 160, WHITE)
        draw_text("Parameter conversion", screen, 18, 200, 341, WHITE)
        draw_text("Series RLC circuit solver", screen, 18, 210, 540, WHITE)
        pygame.draw.circle(screen, var[0], (84, 81), 10)
        pygame.draw.circle(screen, var[1], (84, 171), 10)
        pygame.draw.circle(screen, var[2], (84, 351), 10)
        pygame.draw.circle(screen, var[3], (84, 551), 10)
    pygame.display.flip()
pygame.quit()