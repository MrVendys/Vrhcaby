# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


import pygame
import pygame.gfxdraw
from gameBoard import GameBoard
from piece import Piece
from player import Player

WIDTH, HEIGHT = 850, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WIN_COLOR = (222,184,135)
FPS = 60
pygame.display.set_caption("Vrhcaby")
radius = 25
highlightedSpikes = []
highlightedPiece = None

        
def main():
    playerB = Player("black")
    playerW = Player("white")
    global board
    board = GameBoard(playerB, playerW) 
    board.dice1.numberOnDice = 3
    board.dice2.numberOnDice = 2

    #board.dice1.throw()
    #board.dice2.throw()
    global highlightedSpikes
    global highlightedPiece
    clock = pygame.time.Clock()
    run = True
    draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = event.pos
                print("Začátek alg", len(board.playerWBar.listOfPieces),highlightedPiece )
                
                for spike in highlightedSpikes:
                    if(pygame.draw.polygon(WIN, spike.color, spike.position).collidepoint(click_x, click_y) == True and spike.isHighlighted == True):
                        if(len(spike.queueOfPieces)==0):
                            #Spike je prázdný
                            highlightedPiece.allSpikes[-1].removePiece()
                            spike.addPiece(highlightedPiece)  
                            highlightedPiece.addSpike(spike)  
                            #Na spike je jeden kámen
                        elif(len(spike.queueOfPieces)==1):
                            if(spike.queueOfPieces[0].color == (0,0,0)):
                                popedPiece = spike.removePiece()
                                if(popedPiece != None):
                                    #kámen se vyhodí a dá se na bar
                                    board.playerBBar.addPiece(popedPiece)
                            highlightedPiece.allSpikes[-1].removePiece()
                            spike.addPiece(highlightedPiece)
                            highlightedPiece.addSpike(spike) 
                            #Na spike je víc kamenů
                        elif(len(spike.queueOfPieces)>1 and len(spike.queueOfPieces) < 5 and spike.queueOfPieces[0].color == (255,255,255)):
                            highlightedPiece.allSpikes[-1].removePiece()
                            spike.addPiece(highlightedPiece)

                            highlightedPiece.addSpike(spike) 
 
                        removeHighlight()
                        click_x = 0
                        click_y = 0
                    draw()
                if(len(board.playerWBar.listOfPieces)>0):
                    if(pygame.draw.rect(WIN,(0,0,0),board.playerWBar.position,5).collidepoint(click_x, click_y)):
                        print("Kámen na baru")
                        highlight(board.playerWBar.listOfPieces[0])
                        draw()
                else:               
                    for piece in board.playerPieceList:
                        if (pygame.draw.circle(WIN, piece.color, piece.positions, piece.radius).collidepoint(click_x, click_y)):
                            print("Highlight")
                            if(highlightedPiece != None):
                                removeHighlight()
                            # Kliknutí na hrací kámen
                            highlight(piece.allSpikes[-1].queueOfPieces[-1])
                            

                            draw()
                            break
                        else:
                            draw()
                

    pygame.quit()

       
def draw():
    WIN.fill(WIN_COLOR)
    board.drawGameBoard(WIN)
    pygame.display.update()

def reDraw():
    for spike in board.boardList:
        spike.reDrawItself()
        for piece in spike.queueOfPieces:
            piece.reDrawItself()
    pygame.display.update()
def removeHighlight():
    print("highlight odstraněn")
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
