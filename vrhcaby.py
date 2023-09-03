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
global highlightedSpikes
highlightedSpikes = []
global highlightedPiece
highlightedPiece = None

        
def main():
    playerB = Player("black")
    playerW = Player("white")
    global board
    board = GameBoard(playerB, playerW) 
    board.dice1.throw()
    board.dice2.throw()
    clock = pygame.time.Clock()
    run = True
    global highlightedSpikes
    highlightedSpikes = []
    global highlightedPiece
    highlightedPiece = None
    draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = event.pos

                if(len(highlightedSpikes) > 0):
                    for spike in highlightedSpikes:
                        if(pygame.draw.polygon(WIN, spike.color, spike.position).collidepoint(click_x, click_y) == True and len(spike.queueOfPieces)<=1):
                            popedPiece = spike.addPiece(highlightedPiece)
                            board.boardList[highlightedPiece.spikeId].removePiece()
                            if(popedPiece != None):
                                board.generateNewPiece(popedPiece)
                            removeHighlight()
                            highlightedPiece.isHighlighted = False
                            highlightedPiece = None
                            draw()
            
                for piece in board.playerPieceList:
                    if piece.x - 25 <= click_x <= piece.x + 25 and piece.y - 25 <= click_y <= piece.y + 25:
                        
                        # Kliknutí na hrací kámen
                        highlight(piece)
                        highlightedPiece = piece
                        

                        reDraw()
                        break
                    else:
                        draw()
            #TODO podle hodu kostky udělat malé kolečko hráčovy barvy podle toho, kam s piece může pohnout
            # hodím 3.. na 3. spikeu se udělá malé bílé kolečko, když kliknu na ten spyke, piece se tam přemístí a kolečko zmizí

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
    for spike in highlightedSpikes:
        spike.isHighlighted = False
    
    
def highlight(piece):
    highlightedSpikes.append(board.boardList[piece.spikeId + board.dice1.numberOnDice])
    highlightedSpikes.append(board.boardList[piece.spikeId + board.dice2.numberOnDice])
    board.boardList[piece.spikeId + board.dice1.numberOnDice].isHighlighted = True
    board.boardList[piece.spikeId + board.dice2.numberOnDice].isHighlighted = True
    piece.isHighlighted = True
    
main()
