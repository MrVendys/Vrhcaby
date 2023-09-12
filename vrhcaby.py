import time
import pygame
import pygame.gfxdraw
from dice import Dice
from gameBoard import GameBoard
from piece import Piece
from player import Player
from spike import Spike

WIN = pygame.display.set_mode((850,800))
WIN_COLOR = (222,184,135)
FPS = 60
pygame.display.set_caption("Vrhcaby")


        
def main():
    global playerB
    global playerW
    playerB = Player()
    playerW = Player()
    global board
    board = GameBoard(playerB, playerW) 
    board.dice1.throw()
    board.dice2.throw()
    global highlightedSpikes
    global highlightedPiece
    highlightedSpikes = []
    highlightedPiece = None
    global playerOnTurn
    playerOnTurn = playerW
    clock = pygame.time.Clock()
    run = True
    global AIAlreadyPlay
    AIAlreadyPlay = False
    global index
    index = 0
    global succes
    global succesCounter
    global playerWIsReady
    playerWIsReady = False
    global playerBIsReady
    playerBIsReady = False
    draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            draw()
                #Hraje hráč
            if(playerOnTurn == playerW):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_RIGHT):
                    skipTurn()
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    click_x, click_y = event.pos
                    #Klik myší
                    if(pygame.draw.rect(WIN,(0,0,0),board.homeW.position).collidepoint(click_x, click_y) and board.homeW.isHighlighted):
                        manageHome()
                    for spike in highlightedSpikes:
                        # Kliknutí na spike
                        if(pygame.draw.polygon(WIN, spike.color, spike.position).collidepoint(click_x, click_y) == True and spike.isHighlighted == True):
                            manageSpike(spike)
                            click_x = 0
                            click_y = 0
                            draw()
                    if(len(playerW.playerBar.listOfPieces)>0):
                        # Kliknutí na hrací kámen na baru
                        if(pygame.draw.rect(WIN,(0,0,0),playerW.playerBar.position,5).collidepoint(click_x, click_y)):
                            highlightPiece(playerW.playerBar.listOfPieces[0])
                    else:         
                        # Kliknutí na hrací kámen      
                        for piece in playerW.listOfPieces:
                            if (pygame.draw.circle(WIN, piece.color, piece.positions, piece.radius).collidepoint(click_x, click_y)):
                                highlightPiece(piece)
            else:
                #Hraje počítač
                board.drawAIplays(True)
                draw()
                if(AIAlreadyPlay == False):
                    index = 0
                    AIPlay()
                
def AIPlay():
    global succesCounter
    succesCounter = []
    global AIAlreadyPlay
    global index
    global succes
    AIAlreadyPlay = True
    succes = False
    if(playerOnTurn != playerB):
        return
    if(len(succesCounter) >= 3):
        skipTurn()
        return
    while(succes == False):
        if(board.dice1.numberOnDice !=0 or board.dice2.numberOnDice != 0):
            #AI zkusí hrát s první kostkou
            if(playerB.listOfPieces[index].id == playerB.listOfPieces[index].allSpikes[-1].listOfPieces[-1].id):
                lookOnSpike(board.dice1.numberOnDice) if board.dice1.numberOnDice !=0 else False
            else:
                succes = False
            if(succes == False):
               #AI zkusí hrát s druhou kostkou
                if(playerB.listOfPieces[index].id == playerB.listOfPieces[index].allSpikes[-1].listOfPieces[-1].id):
                    lookOnSpike(board.dice2.numberOnDice) if board.dice2.numberOnDice !=0 else False
                else:
                    succes = False
                if(succes == False):
                   index += 1
                   if index >= len(playerB.listOfPieces):
                       index = 0
                       skipTurn()
                else:
                   break
            else:
                break
        else:
            succes = True
            AIAlreadyPlay = True

def lookOnSpike(dice):
        global index
        global succes
        global succesCounter
        if(len(playerB.playerBar.listOfPieces) > 0):
            highlightPiece(playerB.playerBar.listOfPieces[0])
            manageSpike(board.boardList[playerB.playerBar.id + dice])
            if(succes == False):
                succesCounter.append(False)
        else:
            highlightPiece(playerB.listOfPieces[index])
            if(playerBIsReady):
                manageHome()
            elif(highlightedPiece.allSpikes[-1].id + dice < 24):
                manageSpike(board.boardList[highlightedPiece.allSpikes[-1].id + dice])
            else:
                succes = False
                pass
        

def manageHome():
    home = None
    global succes
    if(playerOnTurn == playerW):
        if(highlightedPiece.allSpikes[-1].id - board.dice1.numberOnDice == -1):
            useDice(board.dice1)
            home = board.homeW
        elif(highlightedPiece.allSpikes[-1].id - board.dice2.numberOnDice == -1):
            useDice(board.dice2)
            home = board.homeW
    else:
        if(highlightedPiece.allSpikes[-1].id + board.dice1.numberOnDice == 24):
            useDice(board.dice1)
            home = board.homeB
        elif(highlightedPiece.allSpikes[-1].id + board.dice2.numberOnDice == 24):
            useDice(board.dice2)
            home = board.homeB
        else:
            succes = False
            return
    highlightedPiece.allSpikes[-1].removePiece()
    home.addPiece(highlightedPiece)
    succes = True
    removeHighlight()
    draw()
    nextTurn()
def manageSpike(spike):
    #Spike je prázdný
    global succes
    if(len(spike.listOfPieces)==0):
        succes = True
        movePiece(spike)
        #Na spike je jeden kámen
    elif(len(spike.listOfPieces)==1):
            if(spike.listOfPieces[0].color != highlightedPiece.color):
                #kámen se vyhodí a dá se na bar
                player = playerW if playerOnTurn == playerB else playerB
                poppedPiece = spike.removePiece()
                player.playerBar.addPiece(poppedPiece)
                poppedPiece.allSpikes.append( player.playerBar) 
            succes = True
            movePiece(spike)
        #Na spike je víc kamenu
    elif(len(spike.listOfPieces)>1 and len(spike.listOfPieces) < 5 and spike.listOfPieces[0].color == playerOnTurn.listOfPieces[0].color):
        succes = True
        movePiece(spike)
    else:
        if(playerOnTurn == playerW):
            skipTurn()
        if(playerOnTurn == playerB):
            succes = False
    draw()
def checkHome():
    global playerWIsReady
    global playerBIsReady
    filtered_list = []
    if(playerOnTurn == playerW):
        for i in range(0,6):
            list = ([item for item in board.boardList[i].listOfPieces if item.color == (255,255,255)])
            filtered_list = filtered_list + list
        if(len(filtered_list) == 15):
            playerWIsReady = True
    if(playerOnTurn == playerB):
        for i in range(18,23):
            list = ([item for item in board.boardList[i].listOfPieces if item.color == (0,0,0)])
            filtered_list = filtered_list + list
        if(len(filtered_list) == 15):
            playerBIsReady = True
def movePiece(spike):
    if(playerOnTurn == playerB):
        time.sleep(2)
    global highlightedPiece
    highlightedPiece.allSpikes[-1].removePiece()
    difference = abs(spike.id - highlightedPiece.allSpikes[-1].id)
    useDice(board.dice1 if difference == board.dice1.numberOnDice else board.dice2)
    spike.addPiece(highlightedPiece)
    highlightedPiece.addSpike(spike)
    removeHighlight()
    checkHome()
    draw()
    nextTurn()
def useDice(dice: Dice):
    dice.numberOnDice = 0
def highlightPiece(piece: Piece):
    global highlightedPiece
    global playerW
    if(highlightedPiece != None):
        removeHighlight()
    if(playerOnTurn == playerW):
        highlight(piece.allSpikes[-1].listOfPieces[-1])
        draw()
    else:
        highlightedPiece = piece
def removeHighlight():
    global highlightedSpikes
    global highlightedPiece
    for spike in highlightedSpikes:
        spike.isHighlighted = False
    highlightedSpikes = []
    highlightedPiece.isHighlighted = False
    highlightedPiece = None
    board.homeW.isHighlighted = False
    
def highlight(piece):
    global highlightedPiece
    global readyToHome
    piece.isHighlighted = True
    highlightedPiece = piece
    if(board.dice1.numberOnDice != 0):
        highlightSpike1 = piece.allSpikes[-1].id - board.dice1.numberOnDice
        if(playerWIsReady and highlightSpike1 == -1):
            #highlight domeček
            board.homeW.isHighlighted = True
            return
        elif(highlightSpike1 >= 0):
            highlightedSpikes.append(board.boardList[highlightSpike1])
            board.boardList[highlightSpike1].isHighlighted = True
    if(board.dice2.numberOnDice != 0):
        highlightSpike2 = piece.allSpikes[-1].id - board.dice2.numberOnDice   
        if(playerWIsReady and highlightSpike2 == -1):
            #highlight domeček
            board.homeW.isHighlighted = True
            return
        elif(highlightSpike2 >= 0):
            highlightedSpikes.append(board.boardList[highlightSpike2])
            board.boardList[highlightSpike2].isHighlighted = True  
def nextTurn():
    global AIAlreadyPlay
    if(board.dice1.numberOnDice == 0 and board.dice2.numberOnDice == 0):
    
        global playerOnTurn
        global playerW
        global playerB
        if(playerOnTurn == playerW):
            board.drawAIplays(True)
            playerOnTurn = playerB
        else: 
            board.drawAIplays(False)
            playerOnTurn = playerW
        board.throwDices() 
        draw()
    elif(playerOnTurn == playerB):
        AIAlreadyPlay = False
    else:
        AIAlreadyPlay = False
def skipTurn():
    global AIAlreadyPlay
    useDice(board.dice1)
    useDice(board.dice2)
    AIAlreadyPlay = False
    nextTurn()
def draw():
    WIN.fill(WIN_COLOR)
    board.drawGameBoard(WIN)
    pygame.display.update()
    
main()
