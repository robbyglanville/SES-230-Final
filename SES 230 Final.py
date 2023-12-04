#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import random


# In[17]:


def game():
    Mode = int(input("""Enter the mode you are playing:
    Type 1 for Player versus Player: 
    Type 2 for Player versus Computer: 
    Type 3 for Computer versus Computer: """))
    if Mode == 1:
        Player_v_Player()
    if Mode == 2:
        Player_v_Computer()
    if Mode == 3:
        Computer_v_Computer()

def Player_v_Player():
    Player1_board = 1
    Player2_board = 1
    while Player1_board or Player2_board <= 100:
        n1 = int(input("Player 1: Enter a number to roll the dice: "))
        
        #Player 1's Turn:
        n1 = random.randrange(1,7)
        print("Player 1 rolled a", n1)
        Player1_board = Player1_board + n1
        
        #Chutes for Player 1:
        if Player1_board == 16:
            Player1_board = 6
            print("Player 1 hit a chute at position 16 and moves back 10 spaces")       
        elif Player1_board == 48:
            Player1_board = 26
            print("Player 1 hit a chute at position 48 and moves back 22 spaces")        
        elif Player1_board == 49:
            Player1_board = 11
            print("Player 1 hit a chute at position 49 and moves back 38 spaces")            
        elif Player1_board == 56:
            Player1_board = 53
            print("Player 1 hit a chute at position 56 and moves back 3 spaces")    
        elif Player1_board == 62:
            Player1_board = 19
            print("Player 1 hit a chute at position 62 and moves back 43 spaces")    
        elif Player1_board == 64:
            Player1_board = 60
            print("Player 1 hit a chute at position 64 and moves back 4 spaces")    
        elif Player1_board == 87:
            Player1_board = 24
            print("Player 1 hit a chute at position 87 and moves back 63 spaces")        
        elif Player1_board == 93:
            Player1_board = 73
            print("Player 1 hit a chute at position 93 and moves back 20 spaces")      
        elif Player1_board == 95:
            Player1_board = 75
            print("Player 1 hit a chute at position 95 and moves back 20 spaces")    
        elif Player1_board == 98:
            Player1_board = 78
            print("Player 1 hit a chute at position 98 and moves back 20 spaces")
        
        #Ladders for Player 1:
        if Player1_board == 1:
            Player1_board = 38
            print("Player 1 hit a ladder at position 1 and moves forward 37 spaces")       
        elif Player1_board == 4:
            Player1_board = 14
            print("Player 1 hit a ladder at position 4 and moves forward 10 spaces")        
        elif Player1_board == 9:
            Player1_board = 31
            print("Player 1 hit a ladder at position 9 and moves forward 22 spaces")
        elif Player1_board == 21:
            Player1_board = 42
            print("Player 1 hit a ladder at position 21 and moves forward 21 spaces")            
        elif Player1_board == 28:
            Player1_board = 84
            print("Player 1 hit a ladder at position 28 and moves forward 56 spaces")    
        elif Player1_board == 36:
            Player1_board = 44
            print("Player 1 hit a ladder at position 36 and moves forward 8 spaces")    
        elif Player1_board == 51:
            Player1_board = 67
            print("Player 1 hit a ladder at position 51 and moves forward 16 spaces")    
        elif Player1_board == 71:
            Player1_board = 91
            print("Player 1 hit a ladder at position 71 and moves forward 20 spaces")        
        elif Player1_board == 80:
            Player1_board = 100
            print("Player 1 hit a ladder at position 80 and moves forward 20 spaces")      
       
        if Player1_board >= 100:
            Player1_board = 100
            win = 1
            print("Player 1 is at", Player1_board, "out of 100")
            break
        print("Player 1 is at", Player1_board, "out of 100")
        
        #Player 2's Turn:
        n2 = int(input("Player 2: Enter a number to roll the dice: "))
        n2 = random.randrange(1,7)
        print("Player 2 rolled a", n2)
        Player2_board = Player2_board + n2
        
        #Chutes for Player 2:
        if Player2_board == 16:
            Player2_board = 6
            print("Player 2 hit a chute at position 16 and moves back 10 spaces")       
        elif Player2_board == 48:
            Player2_board = 26
            print("Player 2 hit a chute at position 48 and moves back 22 spaces")        
        elif Player2_board == 49:
            Player2_board = 11
            print("Player 2 hit a chute at position 49 and moves back 38 spaces")            
        elif Player2_board == 56:
            Player2_board = 53
            print("Player 2 hit a chute at position 56 and moves back 3 spaces")    
        elif Player2_board == 62:
            Player2_board = 19
            print("Player 2 hit a chute at position 62 and moves back 43 spaces")    
        elif Player2_board == 64:
            Player2_board = 60
            print("Player 2 hit a chute at position 64 and moves back 4 spaces")    
        elif Player2_board == 87:
            Player2_board = 24
            print("Player 2 hit a chute at position 87 and moves back 63 spaces")        
        elif Player2_board == 93:
            Player2_board = 73
            print("Player 2 hit a chute at position 93 and moves back 20 spaces")      
        elif Player2_board == 95:
            Player2_board = 75
            print("Player 2 hit a chute at position 95 and moves back 20 spaces")    
        elif Player2_board == 98:
            Player2_board = 78
            print("Player 2 hit a chute at position 98 and moves back 20 spaces")
        
        #Ladders for Player 2:
        if Player2_board == 1:
            Player2_board = 38
            print("Player 2 hit a ladder at position 1 and moves forward 37 spaces")       
        elif Player2_board == 4:
            Player2_board = 14
            print("Player 2 hit a ladder at position 4 and moves forward 10 spaces")        
        elif Player2_board == 9:
            Player2_board = 31
            print("Player 2 hit a ladder at position 9 and moves forward 22 spaces")
        elif Player2_board == 21:
            Player2_board = 42
            print("Player 2 hit a ladder at position 21 and moves forward 21 spaces")            
        elif Player2_board == 28:
            Player2_board = 84
            print("Player 2 hit a ladder at position 28 and moves forward 56 spaces")    
        elif Player2_board == 36:
            Player2_board = 44
            print("Player 2 hit a ladder at position 36 and moves forward 8 spaces")    
        elif Player2_board == 51:
            Player2_board = 67
            print("Player 2 hit a ladder at position 51 and moves forward 16 spaces")    
        elif Player2_board == 71:
            Player2_board = 91
            print("Player 2 hit a ladder at position 71 and moves forward 20 spaces")        
        elif Player2_board == 80:
            Player2_board = 100
            print("Player 2 hit a ladder at position 80 and moves forward 20 spaces")
            
        if Player2_board >= 100:
            Player2_board = 100
            win = 2
            print("Player 2 is at", Player2_board, "out of 100")
            break
        print("Player 2 is at", Player2_board, "out of 100")
    if win == 1:
        print("Player 1 wins!")
    if win == 2:
        print("Player 2 wins!")
        
def Player_v_Computer():
    Player1_board = 1
    Player2_board = 1
    while Player1_board or Player2_board <= 100:
        n1 = int(input("Player 1: Enter a number to roll the dice: "))
        
        #Player 1's Turn:
        n1 = random.randrange(1,7)
        print("You rolled a", n1)
        Player1_board = Player1_board + n1
        
        #Chutes for Player 1 (you):
        if Player1_board == 16:
            Player1_board = 6
            print("You hit a chute at position 16 and moves back 10 spaces")       
        elif Player1_board == 48:
            Player1_board = 26
            print("You hit a chute at position 48 and moves back 22 spaces")        
        elif Player1_board == 49:
            Player1_board = 11
            print("You hit a chute at position 49 and moves back 38 spaces")            
        elif Player1_board == 56:
            Player1_board = 53
            print("You hit a chute at position 56 and moves back 3 spaces")    
        elif Player1_board == 62:
            Player1_board = 19
            print("You hit a chute at position 62 and moves back 43 spaces")    
        elif Player1_board == 64:
            Player1_board = 60
            print("You hit a chute at position 64 and moves back 4 spaces")    
        elif Player1_board == 87:
            Player1_board = 24
            print("You hit a chute at position 87 and moves back 63 spaces")        
        elif Player1_board == 93:
            Player1_board = 73
            print("You hit a chute at position 93 and moves back 20 spaces")      
        elif Player1_board == 95:
            Player1_board = 75
            print("You hit a chute at position 95 and moves back 20 spaces")    
        elif Player1_board == 98:
            Player1_board = 78
            print("You hit a chute at position 98 and moves back 20 spaces")
        
        #Ladders for Player 1 (you):
        if Player1_board == 1:
            Player1_board = 38
            print("You hit a ladder at position 1 and moves forward 37 spaces")       
        elif Player1_board == 4:
            Player1_board = 14
            print("You hit a ladder at position 4 and moves forward 10 spaces")        
        elif Player1_board == 9:
            Player1_board = 31
            print("You hit a ladder at position 9 and moves forward 22 spaces")
        elif Player1_board == 21:
            Player1_board = 42
            print("You hit a ladder at position 21 and moves forward 21 spaces")            
        elif Player1_board == 28:
            Player1_board = 84
            print("You hit a ladder at position 28 and moves forward 56 spaces")    
        elif Player1_board == 36:
            Player1_board = 44
            print("You hit a ladder at position 36 and moves forward 8 spaces")    
        elif Player1_board == 51:
            Player1_board = 67
            print("You hit a ladder at position 51 and moves forward 16 spaces")    
        elif Player1_board == 71:
            Player1_board = 91
            print("You hit a ladder at position 71 and moves forward 20 spaces")        
        elif Player1_board == 80:
            Player1_board = 100
            print("You hit a ladder at position 80 and moves forward 20 spaces")      
        if Player1_board >= 100:
            Player1_board = 100
            win = 1
            print("You are at", Player1_board, "out of 100")
            break
        print("You are at", Player1_board, "out of 100")
        
        #The Computer's Turn:
        n2 = random.randrange(1,7)
        print("The computer rolled a", n2)
        Player2_board = Player2_board + n2
        
        #Chutes for Player 2 (the computer):
        if Player2_board == 16:
            Player2_board = 6
            print("The Computer hit a chute at position 16 and moves back 10 spaces")       
        elif Player2_board == 48:
            Player2_board = 26
            print("The Computer hit a chute at position 48 and moves back 22 spaces")        
        elif Player2_board == 49:
            Player2_board = 11
            print("The Computer hit a chute at position 49 and moves back 38 spaces")            
        elif Player2_board == 56:
            Player2_board = 53
            print("The Computer hit a chute at position 56 and moves back 3 spaces")    
        elif Player2_board == 62:
            Player2_board = 19
            print("The Computer hit a chute at position 62 and moves back 43 spaces")    
        elif Player2_board == 64:
            Player2_board = 60
            print("The Computer hit a chute at position 64 and moves back 4 spaces")    
        elif Player2_board == 87:
            Player2_board = 24
            print("The Computer hit a chute at position 87 and moves back 63 spaces")        
        elif Player2_board == 93:
            Player2_board = 73
            print("The Computer hit a chute at position 93 and moves back 20 spaces")      
        elif Player2_board == 95:
            Player2_board = 75
            print("The Computer hit a chute at position 95 and moves back 20 spaces")    
        elif Player2_board == 98:
            Player2_board = 78
            print("The Computer hit a chute at position 98 and moves back 20 spaces")
        
        #Ladders for Player 2 (the computer):
        if Player2_board == 1:
            Player2_board = 38
            print("The Computer hit a ladder at position 1 and moves forward 37 spaces")       
        elif Player2_board == 4:
            Player2_board = 14
            print("The Computer hit a ladder at position 4 and moves forward 10 spaces")        
        elif Player2_board == 9:
            Player2_board = 31
            print("The Computer hit a ladder at position 9 and moves forward 22 spaces")
        elif Player2_board == 21:
            Player2_board = 42
            print("The Computer hit a ladder at position 21 and moves forward 21 spaces")            
        elif Player2_board == 28:
            Player2_board = 84
            print("The Computer hit a ladder at position 28 and moves forward 56 spaces")    
        elif Player2_board == 36:
            Player2_board = 44
            print("The Computer hit a ladder at position 36 and moves forward 8 spaces")    
        elif Player2_board == 51:
            Player2_board = 67
            print("The Computer hit a ladder at position 51 and moves forward 16 spaces")    
        elif Player2_board == 71:
            Player2_board = 91
            print("The Computer hit a ladder at position 71 and moves forward 20 spaces")        
        elif Player2_board == 80:
            Player2_board = 100
            print("The Computer hit a ladder at position 80 and moves forward 20 spaces")
        if Player2_board >= 100:
            Player2_board = 100
            win = 2
            print("The Computer is at", Player2_board, "out of 100")
            break
        print("The Computer is at", Player2_board, "out of 100")
    if win == 1:
        print("Player 1 wins!")
    if win == 2:
        print("The Computer wins!")
        
def Computer_v_Computer():
    Player1_board = 1
    Player2_board = 1
    while Player1_board or Player2_board <= 100:
        
        #Player 1's Turn:
        n1 = random.randrange(1,7)
        print("Player 1 rolled a", n1)
        Player1_board = Player1_board + n1
        
        #Chutes for Player 1:
        if Player1_board == 16:
            Player1_board = 6
            print("Player 1 hit a chute at position 16 and moves back 10 spaces")       
        elif Player1_board == 48:
            Player1_board = 26
            print("Player 1 hit a chute at position 48 and moves back 22 spaces")        
        elif Player1_board == 49:
            Player1_board = 11
            print("Player 1 hit a chute at position 49 and moves back 38 spaces")            
        elif Player1_board == 56:
            Player1_board = 53
            print("Player 1 hit a chute at position 56 and moves back 3 spaces")    
        elif Player1_board == 62:
            Player1_board = 19
            print("Player 1 hit a chute at position 62 and moves back 43 spaces")    
        elif Player1_board == 64:
            Player1_board = 60
            print("Player 1 hit a chute at position 64 and moves back 4 spaces")    
        elif Player1_board == 87:
            Player1_board = 24
            print("Player 1 hit a chute at position 87 and moves back 63 spaces")        
        elif Player1_board == 93:
            Player1_board = 73
            print("Player 1 hit a chute at position 93 and moves back 20 spaces")      
        elif Player1_board == 95:
            Player1_board = 75
            print("Player 1 hit a chute at position 95 and moves back 20 spaces")    
        elif Player1_board == 98:
            Player1_board = 78
            print("Player 1 hit a chute at position 98 and moves back 20 spaces")
        
        #Ladders for Player 1:
        if Player1_board == 1:
            Player1_board = 38
            print("Player 1 hit a ladder at position 1 and moves forward 37 spaces")       
        elif Player1_board == 4:
            Player1_board = 14
            print("Player 1 hit a ladder at position 4 and moves forward 10 spaces")        
        elif Player1_board == 9:
            Player1_board = 31
            print("Player 1 hit a ladder at position 9 and moves forward 22 spaces")
        elif Player1_board == 21:
            Player1_board = 42
            print("Player 1 hit a ladder at position 21 and moves forward 21 spaces")            
        elif Player1_board == 28:
            Player1_board = 84
            print("Player 1 hit a ladder at position 28 and moves forward 56 spaces")    
        elif Player1_board == 36:
            Player1_board = 44
            print("Player 1 hit a ladder at position 36 and moves forward 8 spaces")    
        elif Player1_board == 51:
            Player1_board = 67
            print("Player 1 hit a ladder at position 51 and moves forward 16 spaces")    
        elif Player1_board == 71:
            Player1_board = 91
            print("Player 1 hit a ladder at position 71 and moves forward 20 spaces")        
        elif Player1_board == 80:
            Player1_board = 100
            print("Player 1 hit a ladder at position 80 and moves forward 20 spaces") 
            
        if Player1_board >= 100:
            Player1_board = 100
            win = 1
            print("Player 1 is at", Player1_board, "out of 100")
            break
        print("Player 1 is at", Player1_board, "out of 100")
        
        #Player 2's Turn:
        n2 = random.randrange(1,7)
        print("Player 2 rolled a", n2)
        Player2_board = Player2_board + n2
        
        #Chutes for Player 2 here
        if Player2_board == 16:
            Player2_board = 6
            print("Player 2 hit a chute at position 16 and moves back 10 spaces")       
        elif Player2_board == 48:
            Player2_board = 26
            print("Player 2 hit a chute at position 48 and moves back 22 spaces")        
        elif Player2_board == 49:
            Player2_board = 11
            print("Player 2 hit a chute at position 49 and moves back 38 spaces")            
        elif Player2_board == 56:
            Player2_board = 53
            print("Player 2 hit a chute at position 56 and moves back 3 spaces")    
        elif Player2_board == 62:
            Player2_board = 19
            print("Player 2 hit a chute at position 62 and moves back 43 spaces")    
        elif Player2_board == 64:
            Player2_board = 60
            print("Player 2 hit a chute at position 64 and moves back 4 spaces")    
        elif Player2_board == 87:
            Player2_board = 24
            print("Player 2 hit a chute at position 87 and moves back 63 spaces")        
        elif Player2_board == 93:
            Player2_board = 73
            print("Player 2 hit a chute at position 93 and moves back 20 spaces")      
        elif Player2_board == 95:
            Player2_board = 75
            print("Player 2 hit a chute at position 95 and moves back 20 spaces")    
        elif Player2_board == 98:
            Player2_board = 78
            print("Player 2 hit a chute at position 98 and moves back 20 spaces")
        
        #Ladders for Player 2 here
        if Player2_board == 1:
            Player2_board = 38
            print("Player 2 hit a ladder at position 1 and moves forward 37 spaces")       
        elif Player2_board == 4:
            Player2_board = 14
            print("Player 2 hit a ladder at position 4 and moves forward 10 spaces")        
        elif Player2_board == 9:
            Player2_board = 31
            print("Player 2 hit a ladder at position 9 and moves forward 22 spaces")
        elif Player2_board == 21:
            Player2_board = 42
            print("Player 2 hit a ladder at position 21 and moves forward 21 spaces")            
        elif Player2_board == 28:
            Player2_board = 84
            print("Player 2 hit a ladder at position 28 and moves forward 56 spaces")    
        elif Player2_board == 36:
            Player2_board = 44
            print("Player 2 hit a ladder at position 36 and moves forward 8 spaces")    
        elif Player2_board == 51:
            Player2_board = 67
            print("Player 2 hit a ladder at position 51 and moves forward 16 spaces")    
        elif Player2_board == 71:
            Player2_board = 91
            print("Player 2 hit a ladder at position 71 and moves forward 20 spaces")        
        elif Player2_board == 80:
            Player2_board = 100
            print("Player 2 hit a ladder at position 80 and moves forward 20 spaces")
       
        if Player2_board >= 100:
            Player2_board = 100
            win = 2
            print("Player 2 is at", Player2_board, "out of 100")
            break
        print("Player 2 is at", Player2_board, "out of 100")
    if win == 1:
        print("Player 1 wins!")
    if win == 2:
        print("Player 2 wins!")


# In[18]:


game()


# In[41]:


def Question():
    g = int(input("Enter the number of games to play: "))
    G1 = 0
    G2 = 0
    Player1_board = 1
    Player2_board = 1
    for i in range(g):
        Player1_board = 1
        Player2_board = 1
        while Player1_board or Player2_board <= 100:
            
            #Player 1's Turn:
            n1 = random.randrange(1,3)
            if n1 == 2:
                n1 = 6
            #print("Player 1 rolled a", n1)
            Player1_board = Player1_board + n1
            
            #Chutes for Player 1:
            if Player1_board == 16:
                Player1_board = 6
                #print("Player 1 hit a chute at position 16 and moves back 10 spaces")       
            elif Player1_board == 48:
                Player1_board = 26
                #print("Player 1 hit a chute at position 48 and moves back 22 spaces")        
            elif Player1_board == 49:
                Player1_board = 11
                #print("Player 1 hit a chute at position 49 and moves back 38 spaces")            
            elif Player1_board == 56:
                Player1_board = 53
                #print("Player 1 hit a chute at position 56 and moves back 3 spaces")    
            elif Player1_board == 62:
                Player1_board = 19
                #print("Player 1 hit a chute at position 62 and moves back 43 spaces")    
            elif Player1_board == 64:
                Player1_board = 60
                #print("Player 1 hit a chute at position 64 and moves back 4 spaces")    
            elif Player1_board == 87:
                Player1_board = 24
                #print("Player 1 hit a chute at position 87 and moves back 63 spaces")        
            elif Player1_board == 93:
                Player1_board = 73
                #print("Player 1 hit a chute at position 93 and moves back 20 spaces")      
            elif Player1_board == 95:
                Player1_board = 75
                #print("Player 1 hit a chute at position 95 and moves back 20 spaces")    
            elif Player1_board == 98:
                Player1_board = 78
                #print("Player 1 hit a chute at position 98 and moves back 20 spaces")
        
            #Ladders for Player 1:
            if Player1_board == 1:
                Player1_board = 38
                #print("Player 1 hit a ladder at position 1 and moves forward 37 spaces")       
            elif Player1_board == 4:
                Player1_board = 14
                #print("Player 1 hit a ladder at position 4 and moves forward 10 spaces")        
            elif Player1_board == 9:
                Player1_board = 31
                #print("Player 1 hit a ladder at position 9 and moves forward 22 spaces")
            elif Player1_board == 21:
                Player1_board = 42
                #print("Player 1 hit a ladder at position 21 and moves forward 21 spaces")            
            elif Player1_board == 28:
                Player1_board = 84
                #print("Player 1 hit a ladder at position 28 and moves forward 56 spaces")    
            elif Player1_board == 36:
                Player1_board = 44
                #print("Player 1 hit a ladder at position 36 and moves forward 8 spaces")    
            elif Player1_board == 51:
                Player1_board = 67
                #print("Player 1 hit a ladder at position 51 and moves forward 16 spaces")    
            elif Player1_board == 71:
                Player1_board = 91
                #print("Player 1 hit a ladder at position 71 and moves forward 20 spaces")        
            elif Player1_board == 80:
                Player1_board = 100
                #print("Player 1 hit a ladder at position 80 and moves forward 20 spaces")
            if Player1_board >= 100:
                Player1_board = 100
                win = 1
                #print("Player 1 is at", Player1_board, "out of 100")
                break
            #print("Player 1 is at", Player1_board, "out of 100")
            
            #Player 2's Turn:
            n2 = random.randrange(2,4)
            if n2 == 3:
                n2 = 5
            #print("Player 2 rolled a", n2)
            Player2_board = Player2_board + n2
            
            #Chutes for Player 2 here
            if Player2_board == 16:
                Player2_board = 6
                #print("Player 2 hit a chute at position 16 and moves back 10 spaces")       
            elif Player2_board == 48:
                Player2_board = 26
                #print("Player 2 hit a chute at position 48 and moves back 22 spaces")        
            elif Player2_board == 49:
                Player2_board = 11
                #print("Player 2 hit a chute at position 49 and moves back 38 spaces")            
            elif Player2_board == 56:
                Player2_board = 53
                #print("Player 2 hit a chute at position 56 and moves back 3 spaces")    
            elif Player2_board == 62:
                Player2_board = 19
                #print("Player 2 hit a chute at position 62 and moves back 43 spaces")    
            elif Player2_board == 64:
                Player2_board = 60
                #print("Player 2 hit a chute at position 64 and moves back 4 spaces")    
            elif Player2_board == 87:
                Player2_board = 24
                #print("Player 2 hit a chute at position 87 and moves back 63 spaces")        
            elif Player2_board == 93:
                Player2_board = 73
                #print("Player 2 hit a chute at position 93 and moves back 20 spaces")      
            elif Player2_board == 95:
                Player2_board = 75
                #print("Player 2 hit a chute at position 95 and moves back 20 spaces")    
            elif Player2_board == 98:
                Player2_board = 78
                #print("Player 2 hit a chute at position 98 and moves back 20 spaces")
        
            #Ladders for Player 2 here
            if Player2_board == 1:
                Player2_board = 38
                #print("Player 2 hit a ladder at position 1 and moves forward 37 spaces")       
            elif Player2_board == 4:
                Player2_board = 14
                #print("Player 2 hit a ladder at position 4 and moves forward 10 spaces")        
            elif Player2_board == 9:
                Player2_board = 31
               #print("Player 2 hit a ladder at position 9 and moves forward 22 spaces")
            elif Player2_board == 21:
                Player2_board = 42
                #print("Player 2 hit a ladder at position 21 and moves forward 21 spaces")            
            elif Player2_board == 28:
                Player2_board = 84
               # print("Player 2 hit a ladder at position 28 and moves forward 56 spaces")    
            elif Player2_board == 36:
                Player2_board = 44
                #print("Player 2 hit a ladder at position 36 and moves forward 8 spaces")    
            elif Player2_board == 51:
                Player2_board = 67
                #print("Player 2 hit a ladder at position 51 and moves forward 16 spaces")    
            elif Player2_board == 71:
                Player2_board = 91
                #print("Player 2 hit a ladder at position 71 and moves forward 20 spaces")        
            elif Player2_board == 80:
                Player2_board = 100
                #print("Player 2 hit a ladder at position 80 and moves forward 20 spaces")
            if Player2_board >= 100:
                Player2_board = 100
                win = 2
                break
        if win == 1:
            G1 = G1 + 1
        if win == 2:
            G2 = G2 + 1
    print("Player 1 won", G1, "times, and Player 2 won", G2, "times")


# In[43]:


Question()

