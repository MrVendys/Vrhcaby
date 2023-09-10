# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


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
    playerB = Player("black")
    playerW = Player("white")
    global board
    board = GameBoard(playerB, playerW) 
    board.dice1.numberOnDice = 1
    board.dice2.numberOnDice = 2
    #board.dice1.throw()
    #board.dice2.throw()
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
    draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if(playerOnTurn == playerW):
                #Hraje hráč
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    #Klik myší
                    for spike in highlightedSpikes:
                        if(pygame.draw.polygon(WIN, spike.color, spike.position).collidepoint(click_x, click_y) == True and spike.isHighlighted == True):
                            manageSpike(spike)
                            click_x = 0
                            click_y = 0
                            break
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
                                break
            else:
                #Hraje počítač
                #board.drawAIplays(WIN)
                if(AIAlreadyPlay == False):
                    AIPlay()
                    draw()
def AIPlay():
    global AIAlreadyPlay
    global highlightedPiece
    global index
    AIAlreadyPlay = True
    #posune figurku do domečku
    #vyhodí hráčovu figurku
    #posune se svojí figurkou
    succes = False
    while(succes == False):
        piece = playerB.listOfPieces[index].allSpikes[-1].listOfPieces[-1]
        readyToHome = []
        for piece in playerB.listOfPieces:
            for spike in range(18,23):
                if(spike.allSpikes[-1].id == spike.id):
                    readyToHome.append(True)
                    return

        if(len(readyToHome) != 12):
            if(len(playerB.playerBar.listOfPieces) > 0):
                highlightPiece(playerB.playerBar.listOfPieces[0])
                succes = manageSpike(board.boardList[playerB.playerBar.id + board.dice1.numberOnDice])
            else:
                highlightPiece(piece)
                succes = manageSpike(board.boardList[highlightedPiece.allSpikes[-1].id + board.dice1.numberOnDice])
            if(succes == False):
                if(len(playerB.playerBar.listOfPieces) > 0):
                    succes = manageSpike(board.boardList[playerB.playerBar.id + board.dice2.numberOnDice])
                else:
                    succes = manageSpike(board.boardList[highlightedPiece.allSpikes[-1].id + board.dice2.numberOnDice])
                if(succes == False):
                    index += 1
                    if index >= len(playerB.listOfPieces):
                        index = 0
                else:
                    break
            else:
                succes = True
                break
        else:
            pass
            #podívej se na kostku a na každý vrchní pieace a jestli může do domečku
    AIAlreadyPlay = False
def lookOnSpike(spike: Spike):
    if(len(spike.listOfPieces) == 0):
        print("Je to 1. true")
        manageSpike(spike)
        return True
    if((spike.listOfPieces[0].color == (0,0,0) and len(spike.listOfPieces)<5)):
        print("je to 2. true")
        manageSpike(spike)
        return True
    if(spike.listOfPieces[0].color == (255,255,255) and len(spike.listOfPieces)<2):
        print("je to 3. true")
        manageSpike(spike)
        return True
    elif(spike.listOfPieces[0].color == (255,255,255 and len(spike.listOfPieces) > 1)):
        return False
    else:
        return False
def nextTurn():
    print("Next turn")
    """
    if(board.dice1.numberOnDice == 0 and board.dice2.numberOnDice == 0):
        global playerOnTurn
        global playerW
        global playerB
        if(playerOnTurn == playerW):
            playerOnTurn = playerB
        else: 
            playerOnTurn = playerW
        board.throwDices() 
    """
    
    global playerOnTurn
    global playerW
    global playerB
    
    if(playerOnTurn == playerW):
        playerOnTurn = playerB
    else: 
        playerOnTurn = playerW
    #board.throwDices() 
    
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
def manageSpike(spike):
    #Spike je prázdný
    if(len(spike.listOfPieces)==0):
        movePiece(spike)
        print("Na spiku nebyl kamen")
        return True
        #Na spike je jeden kámen
    elif(len(spike.listOfPieces)==1):
            if(spike.listOfPieces[0].color != highlightedPiece.color):
                #kámen se vyhodí a dá se na bar
                player = playerW if playerOnTurn == playerB else playerB
                poppedPiece = spike.removePiece()
                player.playerBar.addPiece(poppedPiece)
                poppedPiece.allSpikes.append( player.playerBar) 
            movePiece(spike)
            print("Na spiku byl jeden kamen kamen")
            return True
        #Na spike je víc kamenu
    elif(len(spike.listOfPieces)>1 and len(spike.listOfPieces) < 5 and spike.listOfPieces[0].color == playerOnTurn.listOfPieces[0].color):
        movePiece(spike)
        print("Na spiku bylo více kamenu stejne barvy")
        return True
    if(playerOnTurn == playerB):
        print("Na spiku bylo vice kamenu opacne barvy")
        return False
    removeHighlight()
    draw()
def draw():
    WIN.fill(WIN_COLOR)
    board.drawGameBoard(WIN)
    pygame.display.update()

def movePiece(spike):
   
    global highlightedPiece
    print("Hello 2 ",highlightedPiece.allSpikes.index(highlightedPiece.allSpikes[-1]))
    highlightedPiece.allSpikes[-1].removePiece()
    difference = abs(spike.id - highlightedPiece.allSpikes[-1].id)
    #useDice(board.dice1 if difference == board.dice1.numberOnDice else board.dice2)
    spike.addPiece(highlightedPiece)
    print("Spike id ",highlightedPiece.allSpikes.index(highlightedPiece.allSpikes[-1]))
    highlightedPiece.addSpike(spike)
    nextTurn()  
def useDice(dice: Dice):
        dice.numberOnDice = 0
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
    if(board.dice1.numberOnDice != 0):
        highlightSpike1 = piece.allSpikes[-1].id - board.dice1.numberOnDice if piece.allSpikes[-1].id - board.dice1.numberOnDice >= 0 else 0
        highlightedSpikes.append(board.boardList[highlightSpike1])
        board.boardList[highlightSpike1].isHighlighted = True
    if(board.dice2.numberOnDice != 0):
        highlightSpike2 = piece.allSpikes[-1].id - board.dice2.numberOnDice if piece.allSpikes[-1].id - board.dice2.numberOnDice >= 0 else 0    
        highlightedSpikes.append(board.boardList[highlightSpike2])
        board.boardList[highlightSpike2].isHighlighted = True    
    
    #TODO Highlightni domeček
    
main()
