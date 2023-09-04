# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


import time
import pygame
import pygame.gfxdraw
from gameBoard import GameBoard
from piece import Piece
from player import Player

WIN = pygame.display.set_mode((850,800))
WIN_COLOR = (222,184,135)
FPS = 60
pygame.display.set_caption("Vrhcaby")


        
def main():
    playerB = Player("black")
    playerW = Player("white")
    global board
    board = GameBoard(playerB, playerW) 
    board.dice1.numberOnDice = 4
    board.dice2.numberOnDice = 5
    #board.dice1.throw()
    #board.dice2.throw()
    global highlightedSpikes
    global highlightedPiece
    highlightedSpikes = []
    highlightedPiece = None
    global playerTurn
    playerTurn = True
    clock = pygame.time.Clock()
    run = True
    draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if(playerTurn):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    print(playerTurn)
                    #Klik myší
                    for spike in highlightedSpikes:
                        if(pygame.draw.polygon(WIN, spike.color, spike.position).collidepoint(click_x, click_y) == True and spike.isHighlighted == True):
                            #Spike je prázdný
                            if(len(spike.queueOfPieces)==0):
                                movePiece(spike) 
                                #Na spike je jeden kámen
                                nextTurn() 
                            elif(len(spike.queueOfPieces)==1):
                    
                                if(spike.queueOfPieces[0].color == (0,0,0)):
                                    popedPiece = spike.removePiece()
                                    if(popedPiece != None):
                                        #kámen se vyhodí a dá se na bar
                                        playerB.playerBar.addPiece(popedPiece)
                                movePiece(spike)
                                nextTurn() 
                                #Na spike je víc kamenů
                            elif(len(spike.queueOfPieces)>1 and len(spike.queueOfPieces) < 5 and spike.queueOfPieces[0].color == (255,255,255)):
                                movePiece(spike)
                                nextTurn() 
                            removeHighlight()
                            click_x = 0
                            click_y = 0
                            
                            draw()
                            break
                        draw()
                    if(len(playerW.playerBar.listOfPieces)>0):
                        # Kliknutí na hrací kámen na baru
                        if(pygame.draw.rect(WIN,(0,0,0),playerW.playerBar.position,5).collidepoint(click_x, click_y)):
                            highlight(playerW.playerBar.listOfPieces[0])
                            draw()
                    else:         
                        # Kliknutí na hrací kámen      
                        for piece in playerW.listOfPieces:
                            if (pygame.draw.circle(WIN, piece.color, piece.positions, piece.radius).collidepoint(click_x, click_y)):
                                if(highlightedPiece != None):
                                    removeHighlight()
                                
                                highlight(piece.allSpikes[-1].queueOfPieces[-1])
                                draw()
                                break
            else:
                print("Hraje bot")  
                time.sleep(3) 
                nextTurn()   
                draw()
        
def nextTurn():
    global playerTurn
    if(playerTurn == True):
        playerTurn = False
    else: 
        playerTurn = True
    board.throwDices()
       
def draw():
    WIN.fill(WIN_COLOR)
    board.drawGameBoard(WIN)
    pygame.display.update()

def movePiece(spike):
    global highlightedSpikes
    global highlightedPiece
    highlightedPiece.allSpikes[-1].removePiece()
    spike.addPiece(highlightedPiece)
    highlightedPiece.addSpike(spike) 

def removeHighlight():
    global highlightedSpikes
    global highlightedPiece
    for spike in highlightedSpikes:
        spike.isHighlighted = False
    highlightedSpikes = []
    highlightedPiece.isHighlighted = False
    highlightedPiece = None
    
    
def highlight(piece):
    global highlightedPiece
    piece.isHighlighted = True
    highlightedPiece = piece

    
    piece.isHighlighted = True
    highlightSpike1 = piece.allSpikes[-1].id + board.dice1.numberOnDice
    highlightSpike2 = piece.allSpikes[-1].id + board.dice2.numberOnDice

    if(highlightSpike1 < len(board.boardList)):
        highlightedSpikes.append(board.boardList[highlightSpike1])
        board.boardList[highlightSpike1].isHighlighted = True
    if(highlightSpike2 < len(board.boardList)):
        highlightedSpikes.append(board.boardList[highlightSpike2])
        board.boardList[highlightSpike2].isHighlighted = True    
    
    #TODO Highlightni domeček
    
main()
