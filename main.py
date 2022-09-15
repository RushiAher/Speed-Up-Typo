import pygame
import sys
import random
import time

pygame.init()

Display_size = width, height = 640,480

game_window = pygame.display.set_mode((Display_size))
pygame.display.set_caption("speed up typo")

clock = pygame.time.Clock()
fps = 30

pygame.display.update()

font=pygame.font.SysFont(None,50)


white=(255,255,255)
red=(204, 0, 0)
black=(0,0,0)
yellow=(255,205,42)
# pink=(255,0,255)
pink=(180, 237, 227)
green=(157, 213, 42)
blue=(172, 84, 170)
gray = (203, 209, 208)
# gray = (102, 102, 102)
orange_yellow = (151, 168, 165)
orange_red = (255, 102, 0)

wlc_img = pygame.image.load("wlc.jpg").convert_alpha()
white_img = pygame.image.load("white.png").convert_alpha()
logo = pygame.image.load("logo.png").convert_alpha()
bg = pygame.image.load("background.jpg").convert_alpha()

input_rect = pygame.Rect(175,270,300,60)
reset_rect = pygame.Rect(55,400,150,45)
start_rect = pygame.Rect(255,400,150,45)
exit_rect = pygame.Rect(455,400,150,45)
quit_rect = pygame.Rect(400,400,150,45)
play_again_rect = pygame.Rect(100,400,150,45)


total_char = 1
num_char = 0
score = 0

def text_screen(text,color,x,y,size):
    font = pygame.font.SysFont(None, size)
    text_scr = font.render(text, True, color)
    # text_rect = text_scr.get_rect(center = (width/2, height/2))
    game_window.blit(text_scr, (x,y))

def text_generator():
    global total_char
    with open("words.txt", 'r') as f:

        for line in f:
            lst = line.split()
        word = random.choice(lst)
        f.close()
        total_char+=len(word)
        return word


def Welcome_Screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()

            else:
                game_window.blit(wlc_img,(0,0))
                pygame.display.update()
                clock.tick(fps)
def Game_Over():
    global total_char
    global num_char
    global score
    while True:
        
        game_window.blit(bg, (0, 0))
        game_window.blit(logo, (20, 20))

        wpm = int(num_char / 5)
        accuracy = (num_char / total_char) * 100
        
        
        text_screen("Time Over!", white, 235, 130, 50)
        text_screen("Score: " + str(score), red, 245, 200, 40)
        text_screen("Speed:" + str(wpm) + " wpm", red, 245, 250, 40)
        text_screen("Accuracy :" + str("{:.2f}".format(accuracy)) + "%", red, 245, 300, 40)
        pygame.draw.ellipse(game_window, orange_yellow, quit_rect)
        pygame.draw.ellipse(game_window, orange_yellow, play_again_rect)
        text_screen("Play", black, play_again_rect.x + 40, play_again_rect.y + 10, 40)
        text_screen("Quit", black, quit_rect.x + 40, quit_rect.y + 10, 40)
        
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (400< x < 550) and (400<y<445):
                        sys.exit()
                    elif (100 < x < 250) and (400 < y < 445):
                        score = 0
                        num_char = 0
                        total_char = 1
                        Main_Game()

        pygame.display.update()
    
  


def Main_Game():
    time_up = False
    exit_game = False
    user_text = ""
    text_word = text_generator()
    wpm = 0
    count = 3
    passed_time = 0
    timer_started = False
    global num_char
    global score
    global total_char
    wrong_char_count = 0
    accuracy = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]



                elif event.key == pygame.K_SPACE:
                    if text_word == user_text:
                        num_char += len(user_text)
                        score+=10

                    else:
                        wrong_char_count+=len(user_text)
                        score -= 5

                    user_text = ''


                    text_word = text_generator()
                    pygame.display.update()
                    clock.tick(fps)
                else:
                    user_text += event.unicode
                    


                if (timer_started == False and user_text !=' '):
                    timer_started = True
                    start_time = pygame.time.get_ticks()


            x, y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (55 < x < 205 and 400 < y < 445):
                        passed_time=0

                        wrong_char_count = 0
                        num_char = 0
                        total_char = 1
                        score = 0
                        timer_started = False
                        user_text = ""
                        text_word = text_generator()

                    elif (255 < x < 405 and 400 < y < 445):
                        while count!=0:
                            game_window.blit(bg,(0,0))
                            game_window.blit(logo,(20,20))
                            text_screen("Type or Die!",red,width/2.7,100,40)
                            text_screen(str(count),white,width/2.14,height/2.2,100)

                            pygame.display.update()
                            time.sleep(1)

                            count-=1


                        wrong_char_count = 0
                        total_char = 1

                        num_char = 0
                        count = 3
                        timer_started = True
                        if timer_started:
                            start_time = pygame.time.get_ticks()

                    elif (455 < x < 605 and 400 < y < 445):
                        exit_game=True
                        sys.exit()

        if timer_started:
            passed_time = pygame.time.get_ticks() - start_time

        game_window.blit(bg,(0,0))
        game_window.blit(logo,(20,20))
        # game_window.fill(black)
        pygame.draw.rect(game_window,pink,input_rect,5)
        pygame.draw.ellipse(game_window,orange_yellow,reset_rect)
        pygame.draw.ellipse(game_window,orange_yellow,start_rect)
        pygame.draw.ellipse(game_window,orange_yellow,exit_rect)

        countdown = (60-passed_time / 1000)
        if countdown>10:
            text_screen(str("{:.2f}".format(countdown)),green,550,40,40)
        else:
            text_screen(str("{:.2f}".format(countdown)),red,550,40,40)

        text_screen("Score: " + str(score), gray, 275, 40, 40)
        text_screen(user_text,white,input_rect.x + 10, input_rect.y + 15,50)
        text_screen('Reset',black,reset_rect.x + 40, reset_rect.y + 10,40)
        text_screen('Start',black,start_rect.x + 40, start_rect.y + 10,40)
        text_screen('Quit',black,exit_rect.x + 40, exit_rect.y + 10,40)

        text_src = font.render(text_word,True,black)
        text_rect = text_src.get_rect(center = (width/2,height/3))
        temp_surface = pygame.Surface(text_src.get_size())
        if user_text not in text_word:

            temp_surface.fill((red))
        else:
            temp_surface.fill((gray))
        game_window.blit(temp_surface,text_rect)
        game_window.blit(text_src,text_rect)

        if countdown<=0:
            Game_Over()
            break

        pygame.display.update()














while True:
    Welcome_Screen()
    Main_Game()
