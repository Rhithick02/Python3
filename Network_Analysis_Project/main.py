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
MIX = (100, 255, 100)


def draw_text(text, surf, size, x, y, colour, fontname):
    font = pygame.font.Font(fontname, size)
    text_surf = font.render(text, True, colour)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surf, text_rect)

def draw_text2(text, surf, size, x, y, colour, fontname):
    font = pygame.font.Font(fontname, size)
    text_surf = font.render(text, True, colour)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surf, text_rect)

def input_value(string, string_x, string_y, val_x, val_y, colour, fontname):
    global running
    draw_text(string, screen, 18, string_x, string_y, colour, fontname)
    waiting = True
    string = ''
    screen.fill(BLACK, rect = (val_x, val_y - 7.5, WIDTH / 10, 30))
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
                    screen.fill(BLACK, rect = (val_x, val_y, WIDTH / 10, 15))
                else:
                    string += te.unicode
        text_surf = base_font.render(string, False, WHITE)
        screen.blit(text_surf, (val_x+5, val_y))
        pygame.display.flip()

# Setting up screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("NETWORKS ANALYSIS PROJECT")
clock = pygame.time.Clock()

#All Images and fonts
loc = os.path.dirname(os.path.realpath(__file__))
font_name1 = pygame.font.match_font('arial', bold = True)
font_name2 = pygame.font.match_font('arial', bold = False)
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
op2 = pygame.image.load(os.path.join(loc, '2port.jpg')).convert()
op34 = pygame.transform.scale(op2, (380,180))
op34_rect = op34.get_rect()
op34_rect.center = (200, 370)
op5 = pygame.image.load(os.path.join(loc, 'rlc.jpg')).convert()
op5 = pygame.transform.scale(op5, (380,180))
op5_rect = op5.get_rect()
op5_rect.center = (200, 600)
yparam = pygame.image.load(os.path.join(loc, 'Y-parameter.jpg')).convert()
yparam_rect = yparam.get_rect()
zparam = pygame.image.load(os.path.join(loc, 'Z-parameter.jpg')).convert()
zparam_rect = zparam.get_rect()
var = [YELLOW] * 5
running = True
main_page = True

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
            elif main_page and x > 75 and x < 91 and y > 291 and y < 308:
                var[2] = BLUE
            elif main_page and x > 75 and x < 91 and y > 390 and y < 407:
                var[3] = BLUE
            elif main_page and  x > 75 and x < 91 and y > 540 and y < 557:
                var[4] = BLUE
            else:
                var = [YELLOW] * 5
        
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
                draw_text("PI to T network conversion", screen, 18, 360, 50, GREEN, font_name1)
                input_value("ENTER Zab(ohms): ", 100, 345, 187, 350, RED, font_name1)
                if running: input_value("ENTER Zbc(ohms): ", 100, 405, 187, 410, RED, font_name1)
                if running: input_value("ENTER Zca(ohms): ", 100, 465, 187, 470, RED, font_name1)
                if running: 
                    tot = A[0] + A[1] + A[2]
                    R.append(round(A[0] * A[2] / tot, 2))
                    R.append(round(A[0] * A[1] / tot, 2))
                    R.append(round(A[2] * A[1] / tot, 2))
                    ans1 = "Za = " + str(R[0]) + " ohm"
                    ans2 = "Zb = " + str(R[1]) + " ohm"
                    ans3 = "Zc = " + str(R[2]) + " ohm"
                    draw_text2(ans1, screen, 18, 400, 345, YELLOW, font_name1)
                    draw_text2(ans2, screen, 18, 400, 405, YELLOW, font_name1)
                    draw_text2(ans3, screen, 18, 400, 465, YELLOW, font_name1)
                    draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN, font_name1)
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
                draw_text("T to PI network conversion", screen, 18, 360, 50, GREEN, font_name1)
                input_value("ENTER Za(ohms): ", 100, 345, 187, 350, GREEN, font_name1)
                if running: input_value("ENTER Zb(ohms): ", 100, 385, 187, 390, GREEN, font_name1)
                if running: input_value("ENTER Zc(ohms): ", 100, 425, 187, 430, GREEN, font_name1)
                if running:
                    tot = A[0] * A[1] + A[1] * A[2] + A[2] * A[0]
                    R.append(round(tot / A[2], 2))
                    R.append(round(tot / A[0], 2))
                    R.append(round(tot / A[1], 2))
                    ans1 = "Zab = " + str(R[0]) + " ohm"
                    ans2 = "Zbc = " + str(R[1]) + " ohm"
                    ans3 = "Zca = " + str(R[2]) + " ohm"
                    draw_text2(ans1, screen, 18, 400, 345, YELLOW, font_name1)
                    draw_text2(ans2, screen, 18, 400, 385, YELLOW, font_name1)
                    draw_text2(ans3, screen, 18, 400, 425, YELLOW, font_name1)
                    draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN, font_name1)
            # Operation 3
            if x > 75 and x < 91 and y > 291 and y < 308:
                main_page = False
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                op2_rect = op2.get_rect()
                op2_rect.center = (360, 150)
                yparam_rect.center = (200, 330)
                screen.blit(op2, op2_rect)
                screen.blit(yparam, yparam_rect)
                draw_text("Y -> Z Conversion", screen, 18, 360, 20, GREEN, font_name1)
                A = []
                input_value("Y11  =  ", 100, 400, 150, 405, GREEN, font_name1)
                if running: input_value("Y12  =  ", 100, 440, 150, 445, GREEN, font_name1)
                if running: input_value("Y21  =  ", 100, 480, 150, 485, GREEN, font_name1)
                if running: input_value("Y22  =  ", 100, 520, 150, 525, GREEN, font_name1)
                if running: 
                    try:
                        det = A[0] * A[3] - A[1] * A[2]
                        Z = []
                        Z.append(round(A[3] / det, 2))
                        Z.append(round(-A[1] / det, 2))
                        Z.append(round(-A[2] / det, 2))
                        Z.append(round(A[0] / det, 2))
                        zparam_rect.center = (500, 330)
                        screen.blit(zparam, zparam_rect)
                        draw_text2("Z11 =  " + str(Z[0]), screen, 18, 400, 400, YELLOW, font_name1)
                        draw_text2("Z12 =  " + str(Z[1]), screen, 18, 400, 440, YELLOW, font_name1)
                        draw_text2("Z21 =  " + str(Z[2]), screen, 18, 400, 480, YELLOW, font_name1)
                        draw_text2("Z22 =  " + str(Z[3]), screen, 18, 400, 520, YELLOW, font_name1)
                    except:
                        draw_text("Z PARAMETERS DOESN'T EXIST", screen, 18, 360, 580, YELLOW, font_name1)
                draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN, font_name1)
            # Operation 4
            if x > 75 and x < 91 and y > 390 and y < 407:
                main_page = False
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                op2_rect = op2.get_rect()
                op2_rect.center = (360, 150)
                zparam_rect.center = (200, 330)
                screen.blit(op2, op2_rect)
                screen.blit(zparam, zparam_rect)
                draw_text("Z -> Y Conversion", screen, 18, 360, 20, GREEN, font_name1)
                A = []
                input_value("Z11  =  ", 100, 400, 150, 405, GREEN, font_name1)
                if running: input_value("Z12  =  ", 100, 440, 150, 445, GREEN, font_name1)
                if running: input_value("Z21  =  ", 100, 480, 150, 485, GREEN, font_name1)
                if running: input_value("Z22  =  ", 100, 520, 150, 525, GREEN, font_name1)
                if running: 
                    try:
                        det = A[0] * A[3] - A[1] * A[2]
                        Z = []
                        Z.append(round(A[3] / det, 2))
                        Z.append(round(-A[1] / det, 2))
                        Z.append(round(-A[2] / det, 2))
                        Z.append(round(A[0] / det, 2))
                        yparam_rect.center = (500, 330)
                        screen.blit(yparam, yparam_rect)
                        draw_text2("Y11 =  " + str(Z[0]), screen, 18, 400, 400, YELLOW, font_name1)
                        draw_text2("Y12 =  " + str(Z[1]), screen, 18, 400, 440, YELLOW, font_name1)
                        draw_text2("Y21 =  " + str(Z[2]), screen, 18, 400, 480, YELLOW, font_name1)
                        draw_text2("Y22 =  " + str(Z[3]), screen, 18, 400, 520, YELLOW, font_name1)
                    except:
                        draw_text("Y PARAMETERS DOESN'T EXIST", screen, 18, 360, 580, YELLOW, font_name1)
                draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 600, GREEN, font_name1)
            # Operation 5
            if main_page and  x > 75 and x < 91 and y > 540 and y < 557:
                main_page = False
                screen.fill(BLACK)
                screen.blit(background3, background3_rect)
                op5_newrect = op5.get_rect()
                op5_newrect.center = (360, 150)
                draw_text("Series RLC Circuit Analysis", screen, 18, 360, 20, GREEN, font_name1)
                screen.blit(op5, op5_newrect)
                A = []
                input_value("ENTER the Resistance of the RLC Circuit(ohm): ", 210, 280, 430, 285, GREEN, font_name1)
                if running: input_value("ENTER the Inductance of the RLC Circuit (mH): ", 210, 310, 430, 315, GREEN, font_name1)
                if running: input_value("ENTER the Capacitance of the RLC Circuit (uF): ", 212, 340, 430, 345, GREEN, font_name1)
                if running: input_value("ENTER the frequency of the sinusoidal wave(HZ): ", 215, 370, 430, 375, GREEN, font_name1)
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
                    draw_text2(chr(969) + " = " + str(omega) + " rad/s", screen, 18, 100, 440, RED, font_name1)
                    draw_text2("XL = " + str(I_rx) + " ohms", screen, 18, 100, 480, RED, font_name1)
                    draw_text2("XC = " + str(C_rx) + " ohms", screen, 18, 100, 520, RED, font_name1)
                    draw_text2("Z = " + str(Z_imp) + " ohms", screen, 18, 100, 560, RED, font_name1)
                    draw_text2(chr(981) + " = " + str(phase_rad) + " rad  = " + str(phase_deg) + "deg", screen, 18, 350, 440, RED, font_name1)
                    draw_text2("Resonant frequency fo = " + str(res_freq) + " HZ", screen, 18, 350, 480, RED, font_name1)
                    draw_text2("Q-factor Q = " + str(q_fact), screen, 18, 350, 520, RED, font_name1)
                    draw_text2("Bandwidth = " + str(band) + " Hz", screen, 18, 350, 560, RED, font_name1)
                    pygame.display.flip()
                    plt.xlabel('frequency(fo)')
                    plt.ylabel('Impedence (ohm)')
                    plt.plot(x_axis, y_axis, color = 'red')
                    plt.annotate('Resonance', (res_freq, A[0]), color = 'blue')
                    plt.scatter(res_freq, A[0])
                    plt.title('Resonance Graph')
                    plt.show()
                    draw_text("PRESS 0 TO RETURN TO MAIN PAGE!!", screen, 18, 360, 640, GREEN, font_name1)
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                main_page = True
                var = [YELLOW] * 5
    if main_page == True:
        screen.fill(BLACK)
        screen.blit(background2, background2_rect)
        draw_text("CLICK ON THE YELLOW BUTTON!!", screen, 18, 360, 10, RED, font_name1)
        draw_text("PI to T network conversion", screen, 18, 220, 70, WHITE, font_name1)
        draw_text("T to PI network conversion", screen, 18, 220, 160, WHITE, font_name1)
        draw_text("Y to Z port conversion", screen, 18, 200, 290, WHITE, font_name1)
        draw_text("Z to Y port conversion", screen, 18, 200, 390, WHITE, font_name1)
        draw_text("Series RLC circuit solver", screen, 18, 210, 540, WHITE, font_name1)
        pygame.draw.circle(screen, var[0], (84, 81), 10)
        pygame.draw.circle(screen, var[1], (84, 171), 10)
        pygame.draw.circle(screen, var[2], (84, 301), 10)
        pygame.draw.circle(screen, var[3], (84, 401), 10)
        pygame.draw.circle(screen, var[4], (84, 551), 10)
    pygame.display.flip()
pygame.quit()