import pygame, os, sys
from pygame.locals import *
import random_words
from playsound import playsound

white = (255, 255, 255)

def initialize_game():
    pygame.init()
    word = random_words.get_random_word(3, 11).lower()
    wordModifiable = word
    wordDashes = len(word) * '-'
    print(word)
    screen = pygame.display.set_mode((800, 450))
    pygame.display.set_caption("The Hang Man")
    font = pygame.font.SysFont(None, 34)
    screen.fill(white)
    i = 1
    gameover = False
    image = pygame.image.load(str(i)+'.png')
    tex = font.render('word = '+wordDashes, True, (0, 0, 0))
    soundNum = 0
    return word, wordModifiable, wordDashes, screen, font, i, gameover, image, tex, soundNum

def determine_result(guess, wordModifiable, wordDashes, i, word):
    if len(guess) > 0 and guess in wordModifiable:
        index = 0
        while True:   # this part of the loop is to find the index to change a '-' to the letter (used for double occuring letters)
            index = word.index(guess, index)
            if wordDashes[index] == '-':
                break
            index = index + 1
        wordDashes = wordDashes[:index]+guess+wordDashes[index+1:]
        wordModifiable = wordModifiable.replace(guess, '', 1)
    else:
        if i < 10:
            i += 1
    return wordModifiable, wordDashes, i

def game_over_objects(screen, word):
    font = pygame.font.SysFont(None, 34)
    gameO = font.render('GAME OVER', True, (0, 0, 0))
    grec = create_rect(screen, gameO, True, True)
    answer = font.render('The word was '+word, True, (0, 0, 0))
    ansrec = create_rect(screen, answer, True, False)
    ansrec.centery = grec.centery + 20
    screen.blit(gameO, grec)
    screen.blit(answer, ansrec)
    return screen

def win(screen, word):
    font = pygame.font.SysFont(None, 50)
    winner = font.render('YOU WIN, GOOD JOB!', True, (50, 6, 22))
    winrec = create_rect(screen, winner, True, True)
    image = pygame.image.load('winner.png')
    screen.blit(winner, winrec)
    screen.blit(image, (800-200, 20))
    return screen, image

def create_rect(screen, rectable, alignx, aligny): # receive a rectable object and maybe align it and return the rect
    rec = screen.get_rect()
    recTab = rectable.get_rect()
    if alignx:
        recTab.centerx = rec.centerx
    if aligny:
        recTab.centery = rec.centery
    return recTab
    
def create_rectangle(screen, color1, color2, word, alignx, aligny, x = 0, y = 0):
    rec = screen.get_rect()
    if x == 0 and y == 0:
        rectangle = pygame.Rect(10, 10, rec.width/4, 30)
    else:
        rectangle = pygame.Rect(x, y, rec.width/4, 30)
    if alignx:
        rectangle.centerx = rec.centerx
    if aligny:
        rectangle.centery = rec.centery
    rectangle = pygame.draw.rect(screen, color1, rectangle)
    
    font = pygame.font.SysFont(None, 34)
    the_word = font.render(word, True, color2)
    the_wordrect = the_word.get_rect()
    the_wordrect.centerx = rectangle.centerx
    the_wordrect.centery = rectangle.centery
    screen.blit(the_word, the_wordrect)
    return screen, rectangle, the_word
    
def with_in_bounds(rectangle, x, y):
    if x > rectangle.left and x < rectangle.right and y < rectangle.bottom and y > rectangle.top:
        return True
    return False

def run_game():
    word, wordModifiable, wordDashes, screen, font, i, gameover, image, tex, soundNum = initialize_game()
    
    wor = font.render("Guess The Word, otherwise the guy will be hanged?", True, (100, 22, 39))
    worec = create_rect(screen, wor, True, False)
    worec.centery = 10
    screen.blit(wor, worec)
    screen.blit(tex, (20, 30))
    screen.blit(image, (800-200, 30))
    
    game_start = False
    play_again, ex, py_rec, ex_rec = None, None, None, None
    
    while True:
        screen.fill(white)
        if not game_start:
            screen, rectangle, play = create_rectangle(screen, (0, 200, 55), (180, 50, 100), 'PLAY', True, True)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if with_in_bounds(rectangle, mx, my):
                    game_start = True  
                if gameover and with_in_bounds(py_rec, mx, my):
                    word, wordModifiable, wordDashes, screen, font, i, gameover, image, tex, soundNum = initialize_game()
                    gameover = False
                if gameover and with_in_bounds(ex_rec, mx, my):
                    sys.exit()
            if event.type == pygame.KEYDOWN and not gameover and game_start:
                if event.key >= 97 and event.key <= 128:
                    guess = chr(event.key)
                    wordModifiable, wordDashes, i = determine_result(guess, wordModifiable, wordDashes, i, word)
                    if i == 10 or len(wordModifiable) == 0:
                        gameover = True
                    tex = font.render('word = '+wordDashes, True, (0, 0, 0) )
                    image = pygame.image.load(str(i)+'.png')
        if gameover:
            if len(wordModifiable) > 0:
                screen = game_over_objects(screen, word)
            else:
                screen, image = win(screen, word)
            screen, py_rec, play_again = create_rectangle(screen, (0, 200, 55), (180, 50, 100), 'PLAY AGAIN', False, False, 100, 330)
            screen, ex_rec, ex = create_rectangle(screen, (0, 200, 55), (180, 50, 100), 'EXIT', False, False, 101, 400)
            
        screen.blit(wor, worec)
        screen.blit(tex, (20, 30))
        screen.blit(image, (800-200, 20))
        pygame.display.update()
        if gameover:
            if soundNum == 0 and len(wordModifiable) == 0:
                playsound('iwin.mp3')
                soundNum += 1
            if soundNum == 0 and len(wordModifiable) > 0:
                playsound('chock.mp3')
                soundNum += 1
        
run_game()

    
    

