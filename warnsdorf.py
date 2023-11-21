from tkinter import *
from tkinter import ttk
import time

def init():
    board = [[0]*8 for i in range(8)]

    return board


def onwardMoves(board,line,column):
    move = knightMoves(board, line, column)
    mini = move[0]
    for i in move:
        proch = knightMoves(board, i[0],i[1])
        if len(knightMoves(board, mini[0],mini[1])) > len(proch):
            mini = i
    return mini[0],mini[1]
    
def knightMoves(board,line,column):
    un,deux=[1,-1],[-2,2]
    liste=[]
    for x in deux :
        for y in un :
            if 0<= (line+x) < len(board) and 0<= (column + y) <len(board):
                if board[line+x][column+y] ==0 :
                    liste.append([line+x,column+y])
            if 0<= (line+y) < len(board) and 0<= (column + x) <len(board) :
                if board[line+y][column+x] ==0 :
                    liste.append([line+y,column+x])
    return liste
        
def knightsTour(board,line,column):
    l,c = line,column
    tot= len(board)**2
    val=1
    mouvement(l, c)   
    while val < tot :
        board[l][c] = val
        val+=1
        l,c = onwardMoves(board, l, c)
        mouvement(l, c)   
    board[l][c] = val
    mouvement(l, c)
    
def mouvement(line,column):
    positionX,positionY = 50*column,50*line
    canva.create_oval(positionX+10, positionY+10, positionX+40, positionY+40, width = 3)
    canva.pack()
    interface.update()
    time.sleep(0.25)
    
board = init()
interface = Tk()
width,height = 400,400
canva = Canvas(interface,width=width,height=height,background="white")
column = width/len(board)
for i in range(1,len(board)):
    ligne = canva.create_line(column*i,0,column*i,400)
    canva.pack()
row = height/len(board)
for i in range(1,len(board)):
    ligne = canva.create_line(0,row*i,400,row*i)
    canva.pack()
x=int(input("X: "))
y=int(input("Y: "))
knightsTour(board, y, x)
interface.mainloop()
