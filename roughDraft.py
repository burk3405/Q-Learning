import copy
import os
import random
import time

Gamma = 1 # Discount
livingReward = 0 # Living Reward

alpha = 0.95 # Learning Rate

Q = {}
for act in "^>v<":
    Q[(10,10),act] = 0.0
    Q[(-100,-100),act] = 0.0

for row in range(1,4):
    for col in range(1,6):
        for act in "^>v<":
            index = ((row,col),act)
            Q[index] = 0.0
            


def printWorld(s):
    for row in range(3,0,-1):
        for col in range(1,6):
            if (row,col) == (2,5) or row == 1:
                break
            print("%16.2f" %Q[((row,col),'^')], end='')
        print()
        print('%4s' %'', end = '')
        for col in range(1,6):
            if (row,col) == (2,5):
                print("%12.2f" %Q[((row,col),'v')], end='')
                continue
            elif row == 1:
                print("%12.2f" %Q[((row,col),'v')], end='    ')
                continue
                
            print("%8.2f" %Q[((row,col),'<')], end='')
            offset = "%8.2f"
            if (row,col) == s:
                print(" @", end='')
                offset = "%6.2f"
            print(offset %Q[((row,col),'>')], end='')
        print()
        for col in range(1,6):
            if (row,col) == (2,5) or row == 1:
                break
            print("%16.2f" %Q[((row,col),'v')], end='')
        print('\n-------------------------------------------------------------------------------------')

def isFree(loc):
    row, col = loc
    if row in range(1,3+1) and col in range(1,5+1):
        return True
    return False


def R(s,a,sp):
    if s == (2,5):
        return +10.0
    if s == (1,1):
        return -100.0
    if s == (1,2):
        return -100.0
    if s == (1,3):
        return -100.0
    if s == (1,4):
        return -100.0
    if s == (1,5):
        return -100.0
    return livingReward
    


def nextState(s,a):
    row, col = s
    if row == 1:
        return (-100,-100)
    elif s == (2,5):
        return (10,10)
    
    if a == '^': sp = (row+1,col)
    elif a == 'v': sp = (row-1,col)
    elif a == '<': sp = (row,col-1)
    elif a == '>': sp = (row,col+1)

    if isFree(sp):
        return sp
    else:
        return s
      


def main():
    global alpha
    ep = 1
    s = (2,1)
    while True:
        print('Episode', ep)
        printWorld(s)
        print('You are at',s)
        #a = input('Choose move: ')
        a = random.choice('^>v<')
        print('Random action is ', a)
        sp = nextState(s,a)

        # To be completeted from this point


        os. system('clear')

main()
