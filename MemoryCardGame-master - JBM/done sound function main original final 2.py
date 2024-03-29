from graphics import *
from random import *
from time import *
from platform import *
import pygame
from tkinter import messagebox
pygame.mixer.init()
# Add these imports at the top of your code if they are not already there

# Define the ExitButton function


def quit_game(win):
    win.close()
    exit()
    
def get_user_response(response_var, user_response):
    response_var.set(user_response)
    ask.quit()

def ask_yn(ynMessage):
    global ask
    ask = tk.Tk()
    ask.title("Alert ")

    response_var = tk.StringVar()

    question_label = tk.Label(ask, text=ynMessage)
    question_label.pack()

    button_frame = tk.Frame(ask)
    button_frame.pack()

    yes_button = tk.Button(button_frame, text="Yes", command=lambda: get_user_response(response_var, "Yes"), width=10, height=2)
    no_button = tk.Button(button_frame, text="No", command=lambda: get_user_response(response_var, "No"), width=10, height=2)
    cancel_button = tk.Button(button_frame, text="Cancel", command=lambda: get_user_response(response_var, "No"), width=10, height=2)

    yes_button.pack(side="left", padx=10)
    no_button.pack(side="left", padx=10)
    cancel_button.pack(side="left", padx=10)

    ask.mainloop()
    ask.destroy()
    return response_var.get()

def ExitButton(win):
    exit_button = Image(Point(750, 25), 'exit_button.png')
    exit_button.draw(win)

    while True:
        click_point = win.getMouse()
        # Check if the click is within the exit button's area
        if 725 <= click_point.getX() <= 775 and 0 <= click_point.getY() <= 50:
            win.close()
            exit()

# Inside your Main function:
# Uncomment the following line to create the Exit button.
# ExitButton(win)
def sound_button_function():
    global sound
    sound=not sound
    if (sound==True):
        messagebox.showinfo("Listen up!", "Listen up! Sound is now activated! ")
    else:
        messagebox.showinfo("Shhh...", "Shhh... Sound has been silenced. ")

def welcome_music():
    if(sound==True):
        pygame.mixer.music.load("jbm_music.mp3")
        pygame.mixer.music.play(-1)
    else:
        pass
    
def click_music():
    if(sound==True):
        pygame.mixer.music.load("click_sound.mp3")
        pygame.mixer.music.play(0)
    else:
        pass
def card_music():
    if(sound==True):
        pygame.mixer.music.load("cardopen.mp3")
        pygame.mixer.music.play(0)
    else:
        pass
def card_close():
    if(sound==True):
        pygame.mixer.music.load("card_close.mp3")
        pygame.mixer.music.play(0)
    else:
        pass   


def OsCheck():
    if(system() != 'Windows'):
        return(False)

def Welcome(win):

    welcome_music()
    background = Image(Point(randint(-200, 1000), randint(-200, 600)), 'bg.png')
    background.draw(win)      
    
    img1 = Image(Point(randint(50, 700), randint(-100, 500)), 'img1.png')
    img1.draw(win)
    click_music()               
    
    logo = Image(Point(400, 400/3), 'logo.png')
    logo.draw(win)
    click_music() 

    txt1 = Text(Point(400, 210), "Press Anywhere To Start Game")
    txt1.draw(win)
    click_music()                    
  
    win.getMouse()

    logo.undraw()
    txt1.undraw()
    
'''   
def QuitButton(win):
    button = Rectangle(Point(720, 10), Point(780, 40))
    button.setFill("red")
    button.draw(win)

    text = Text(Point(750, 25), "Quit")
    text.setSize(14)
    text.setStyle('bold')
    text.setTextColor("white")
    text.draw(win)

    while True:
        click_point = win.getMouse()
        if 720 <= click_point.getX() <= 780 and 10 <= click_point.getY() <= 40:
            win.close()
            exit()
'''            
            
def GameModePick(win):
    txt0 = Text(Point(400, 50), "Game Mode")
    txt0.setSize(36)
    txt0.setStyle('bold')
    txt0.draw(win)

    txt = Text(Point(400, 100), "Pick A Game Mode! Images Mode Or Numbers Mode!")
    txt.setSize(15)
    txt.draw(win)

    img1 = Image(Point(200,200), 'imagesmode.png')
    img1.draw(win)
    click_music()

    img2 = Image(Point(600,200), 'numbersmode.png')
    img2.draw(win)
    click_music()
    
    img4 = Image(Point(400,280), 'exit_button.png')
    img4.draw(win)
    click_music()
    
    gamemode = -1
    
    while(gamemode < 0):
        point = win.getMouse()
    
        if(point.x < 310 and point.x > 90 and point.y < 230 and point.y > 190):
            gamemode = 0
            click_music()
        elif(point.x < 480 and point.x > 320 and point.y < 310 and point.y > 250):
            gamemode = 1
            ynMessage='Are you sure want to close this game ? '
            resp=ask_yn(ynMessage)
            if resp=='Yes':
                quit_game(win)
            else:
                GameModePick(win)
        else:
            if(point.x < 720 and point.x > 470 and point.y < 230 and point.y > 190):
                gamemode = 1
                click_music()  
            else:
                gamemode = -1
                click_music()
    
                
    txt0.undraw()
    txt.undraw()
    img1.undraw()
    img2.undraw()
    img4.undraw()
            
    return(gamemode)
    


def Difficult(win):
    txt0 = Text(Point(400, 50), "level")
    txt0.setSize(36)
    txt0.setStyle('bold')
    txt0.draw(win)

    txt = Text(Point(400, 100), "Pick A level ! Easy Mode Or Normal Mode Or Hard Mode!")
    txt.setSize(15)
    txt.draw(win)

    img1 = Image(Point(200, 200), 'easy.png')
    img1.draw(win)
    
    img2 = Image(Point(400, 200), 'normal.png')    
    img2.draw(win)
    
    img3 = Image(Point(600, 200), 'hard.png')    
    img3.draw(win)
    
    img4 = Image(Point(400,280), 'exit_button.png')
    img4.draw(win)

    
    difficult = -1
    
    while(difficult < 0):
        point = win.getMouse()
        if(point.x < 250 and point.x > 150 and point.y < 230 and point.y > 150):
            difficult = 16
            click_music()

        else:
            if(point.x < 450 and point.x > 350 and point.y < 230 and point.y > 150):
                difficult = 24
                click_music()
            else:
                if(point.x < 650 and point.x > 550 and point.y < 230 and point.y > 150):
                    difficult = 32
                    click_music()
                elif(point.x < 480 and point.x > 320 and point.y < 320 and point.y > 250):
                    ynMessage='Are you sure want to close this game ? '
                    resp=ask_yn(ynMessage)
                    if resp=='Yes':
                        quit_game(win)
                    else:
                        Difficult(win)
                else:                
                    difficult = -1
                    click_music()
                
    txt0.undraw()
    txt.undraw()
    img1.undraw()
    img2.undraw()
    img3.undraw()
    img4.undraw()

    num_list = [i%(int(difficult/2)) for i in range(difficult)]
    shuffle(num_list)
    exposed = [False for i in range(difficult)]

    return(num_list, exposed, difficult)
    


    
def Init(win):
    background = Image(Point(randint(-200, 1000), randint(-200, 600)), 'bg.png')
    background.draw(win) 
    
    txt0 = Text(Point(90, 50), "Rules")
    txt0.setSize(36)
    txt0.setStyle('bold')
    txt0.draw(win)
    
    txt = Text(Point(380, 160), "In turn player chooses two cards and turns them face up. \n If they are the same number then player wins the pair and earn 1 KEY. \n If they are not the same number, they are turned face down again.\n There are 8 KEYS to earn. Use the least moves and time to win the game. \n Now Type in your name to start game!")
    txt.setSize(15)
    txt.draw(win)
    
    username = ""
    move = 0
    key = 0

    txt1 = Text(Point(800/1.5, 350), "Player Name: ")
    txt1.setSize(14)
    txt1.draw(win)
    
    entry1 = Entry(Point(800/1.5 + 130, 350), 15)
    entry1.setFill('white')
    entry1.draw(win)
        
    while(len(username) < 0 or username.isalpha() == False):
        win.getMouse()  
        username = entry1.getText()

    txt1.undraw()
    entry1.undraw()
    starttime = time()
    
    txt0.undraw()
    txt.undraw()
    background.undraw()
    
    return(username, move, key, starttime)

def ReadPicturesNames(t, gamemode):
    if(gamemode == 1):
        if(t == -1):
            a = 'cardback.png'
            
        else:
            a = 'card.png'
            
    else:
        if(gamemode == 0):
            if(t != -1):
                a = 'card_' + str(t) + '.png'
            else:
                a = 'cardback.png'
    
    return(a)

def DrawPictures(path, p, win, gamemode):
    img1 = Image(p, ReadPicturesNames(path, gamemode))
    img1.draw(win)
    
    
def DrawText(p, win, num_list, clicked_card):
    txt1 = Text(p, num_list[clicked_card - 1])
    txt1.setSize(24)
    txt1.setStyle('bold')
    txt1.draw(win)
    

    return(txt1)
    

def ScoreBoard(win, move, key, mouse):
    move_txt = Text(Point(45, 160), "Moves: ")
    move_txt.setStyle('bold')
    move_txt.draw(win)
    
    
    move_txt1 = Text(Point(80, 160), str(move))
    move_txt1.setStyle('bold')
    move_txt1.draw(win)
    
    
    key_txt = Text(Point(40, 180), "Key: " + str(key))
    key_txt.setStyle('bold')
    key_txt.draw(win)
    
    mouse_txt = Text(Point(105, 200), "Mouse Clicked: " + str(mouse.x) + "," + str(mouse.y))
    mouse_txt.setStyle('bold')
    mouse_txt.draw(win)
    
    mute_txt = Image(Point(50,280), 'sound.png')
    #mute_txt.setStyle('bold')
    mute_txt.draw(win)
    
    pause_txt = Image(Point(50,350), 'pause_button.png')
    #mute_txt.setStyle('bold')
    pause_txt.draw(win)
    return(move_txt, key_txt, mouse_txt, move_txt1)
    

    
def GameBoard(win, username, gamemode, difficult):

    txt1 = Text(Point(80, 40), str(username))
    txt1.setSize(30 - len(username))
    txt1.setStyle('bold')
    txt1.draw(win)
    
    card_point = []
    card_point1 = []
    card_point2 = []

    ''''
        elif(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
        not sound
        '''
    
    
    if(difficult == 32):
        plac = 50
    else:
        if(difficult == 24):
            plac = 100
        else:
            plac = 150
            
            
            
    for j in range(int(difficult/8)):
        
        for i in range(8):
            x = 225 + ((i + 1) * 60)
            y = plac + (j * 100)
            p = Point(x, y)
            DrawPictures(-1, p, win, gamemode)
            p1 = Point(x + 25, y + 40)
            p2 = Point(x - 25, y - 40)
            card_point.append(p)
            card_point1.append(p1)
            card_point2.append(p2)
      
    
    return(card_point, card_point1, card_point2) 


def DecideWhichCard(x, y, card_point1, card_point2 , difficult):
    for i in range(difficult):
        if(x < card_point1[i].x and x > card_point2[i].x and y < card_point1[i].y and y > card_point2[i].y):
            return(i + 1)
        
    return(-1)

def HasItBeenClickedBefore(clicked_card, exposed):
    if(exposed[clicked_card - 1] == False):
        card_close()
        return(False)
    else:
        return(True)
 
def CheckMacthes(c1, c2, num_list):
    if(num_list[c1] == num_list[c2]):
        card_close()
        return(True)
    else:
        return(False)


def Reuslt(win, gametime, username, difficult):
    if(difficult == 32):
        rank = [i.rstrip('\n') for i in open("playersScores_hard.txt", "r")]
        t = "Hard"
    else:
        if (difficult == 24):
            rank = [i.rstrip('\n') for i in open("playersScores_normal.txt", "r")]
            t = "Normal"
        else:
            rank = [i.rstrip('\n') for i in open("playersScores.txt", "r")]
            t = "Easy"
            
    ranking_txt = Text(Point(400, 30), "Rankings Of " + str(t) + " Mode")
    ranking_txt.setSize(20)
    ranking_txt.setStyle('bold')
    ranking_txt.draw(win)

    current = Text(Point(120, 200), str(t) + " Mode\n" + "Player Time: " + str(round(gametime,3)) + "s")
    current.setSize(14)
    current.setStyle('bold')
    current.draw(win)
      
    line = Line(Point(0, 50), Point(801, 50))
    line.draw(win)
    line.setWidth(2)
            
    
    rankings = sorted(rank) 
    t = 0
    
    while(t < len(rankings) and t < 10):
        txt1 = Text(Point(500, 80 + (t * 30)), "Rank " + str(t + 1) + ": " + str(rankings[t]))
        txt1.setSize(14)
        txt1.draw(win)
        t += 1

def InsertInsideTheTopPlayer(username, gametime, move, difficult):
    if(difficult == 32):
        rank_file = open("playersScores_hard.txt ", "a+")       
    else:
        if (difficult == 24):
            rank_file = open("playersScores_normal.txt ", "a+")
        else:
            rank_file = open("playersScores.txt ", "a+")

    rank_file.write(str(round(gametime,3)) + "s Name: " + str(username) + " Moves: " + str(move) + "\n")   
        
    rank_file.close()
     

def Main():
    global sound
    sound=True
    user_point = Point(200, 200)
    counter = 0
    card = []
    
    win = GraphWin("Memories Card Game", 800, 400) 

    if(OsCheck() == False):
        txt1 = Text(Point(400, 210), "Sorry This Game Only Works For Windows User.")
        txt1.setSize(24)
        txt1.setTextColor('red')
        txt1.draw(win)               
        win.getMouse()
        win.close()
        exit()

    Welcome(win)
    gamemode = GameModePick(win)
    num_list, exposed, difficult = Difficult(win)
    username, move, key, starttime = Init(win)
    move_txt, key_txt, mouse_txt, move_txt1 = ScoreBoard(win, move, key, user_point)
    card_point, card_point1, card_point2 = GameBoard(win, username, gamemode, difficult)
    
    msg = Text(Point(100, 300), "")
    msg.setSize(18)
    msg.setStyle('bold')
    msg.draw(win)
    
    while(key < int(difficult/2)):
        sound_point=(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270)
        if(counter < 2):        
            move_txt.undraw()
            key_txt.undraw()
            mouse_txt.undraw()   
            move_txt1.undraw()
            
            move_txt, key_txt, mouse_txt, move_txt1 = ScoreBoard(win, move, key, user_point)
            
            user_point = win.getMouse()

            msg.undraw()
            
            
                
    
            clicked_card = DecideWhichCard(user_point.x, user_point.y, card_point1, card_point2, difficult)
            if(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
                    sound_button_function()
                    
            if(clicked_card > 0):
                '''
                if(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
                    sound_button_function()
                    messagebox.showinfo("Listen up!", "2")'''
                if(HasItBeenClickedBefore(clicked_card, exposed) == False):
                    '''
                    if(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
                        sound_button_function()
                        messagebox.showinfo("Listen up!", "3")'''
                    counter += 1
                    card.append(clicked_card - 1)
                    DrawPictures(2, card_point[clicked_card - 1], win, gamemode)
                    if(gamemode == 1):
                        '''
                        if(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
                            sound_button_function()
                            messagebox.showinfo("Listen up!", "4")'''

                        txt1 = DrawText(card_point[clicked_card - 1], win, num_list, clicked_card)
                    else:
                        '''
                        if(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
                            sound_button_function()
                            messagebox.showinfo("Listen up!", "5")'''
                        DrawPictures(num_list[clicked_card - 1], card_point[clicked_card - 1], win, gamemode)
                        exposed[clicked_card - 1] = True
                else:
                    '''
                    if(user_point.x < 80 and user_point.x > 15 and user_point.y < 345 and user_point.y > 270):
                        sound_button_function()
                        messagebox.showinfo("Listen up!", "6")'''
                    msg.setText("Bad Choices!\n    Pick Another One!")
                    msg.setTextColor('red')
                    msg.draw(win)                    

        else:
            check = CheckMacthes(card[0], card[1], num_list)
            if(check == True):
                key += 1
                move += 1
                oo = ["Great!", "Nice!", "Cool!", "Awesome!"]
                msg.setText(oo[randint(0, 3)])
                msg.setTextColor('black')
                msg.draw(win)
                
            else:
                sleep(1)
                exposed[card[0]] = False
                exposed[card[1]] = False
                DrawPictures(-1, card_point[card[0]], win, gamemode)
                DrawPictures(-1, card_point[card[1]], win, gamemode)
                oo = ["Sorry!", "Try Again!"]
                msg.setText(oo[randint(0, 1)])
                msg.setTextColor('black')
                msg.draw(win)                
                move += 1
            card = []
            counter = 0            
            
    background = Image(Point(randint(-200, 1000), randint(-200, 600)), 'bg.png')
    background.draw(win)
    
    endtime = time()
    gametime = endtime - starttime
    rank_file = InsertInsideTheTopPlayer(username, gametime, move, difficult)
    Reuslt(win, gametime, username, difficult)
    
    
    win.getMouse()
    win.close()


Main()
