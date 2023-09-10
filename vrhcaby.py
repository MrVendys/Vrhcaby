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
    global playerTurn
    playerTurn = True
    clock = pygame.time.Clock()
    run = True
    global AIAlreadyPlay
    AIAlreadyPlay = False
    draw()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if(playerTurn):
                #Hraje hráč
                print("Hraje hráč")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    print(playerTurn)
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
                            managePiece(playerW.playerBar.listOfPieces[0])
                    else:         
                        # Kliknutí na hrací kámen      
                        for piece in playerW.listOfPieces:
                            if (pygame.draw.circle(WIN, piece.color, piece.positions, piece.radius).collidepoint(click_x, click_y)):
                                managePiece(piece)
                                break
            else:
                #Hraje počítač
                #board.drawAIplays(WIN)
                if(AIAlreadyPlay == False):
                    AIPlay()
                    time.sleep(3)
                    draw()
def AIPlay():
    global AIAlreadyPlay
    AIAlreadyPlay = True
    #když vyhodím jeden, tak ten můj se považuje za černý
    #posune figurku do domečku
    #vyhodí hráčovu figurku
    #posune se svojí figurkou
    index = 0
    succes = False
    while(succes == False):
        piece = playerB.listOfPieces[index].allSpikes[-1].listOfPieces[-1]

        if(len(playerB.playerBar.listOfPieces) > 0):
            managePiece(playerB.playerBar.listOfPieces[0])
        else:
            managePiece(piece)
        print("id spiku počátku: ",piece.allSpikes.index(piece.allSpikes[-1]))
        print("kostka: ",board.dice1.numberOnDice)
        print("id spkiku",piece.allSpikes.index(piece.allSpikes[-1])+board.dice1.numberOnDice)
        succes = lookOnSpike(board.boardList[piece.allSpikes.index(piece.allSpikes[-1]) + board.dice1.numberOnDice])
        print("Succes je: ",succes)
        if(succes == False):
            succes = lookOnSpike(board.boardList[piece.allSpikes.index(piece.allSpikes[-1]) + board.dice2.numberOnDice])
            if(succes == False):
                pass
            else:
                break
        else:
            succes = True
            break
    AIAlreadyPlay = False
def lookOnSpike(spike: Spike):
    if(len(spike.listOfPieces) == 0):
        manageSpike(spike)
        return True
    if(spike.listOfPieces[0].color == (0,0,0) or (spike.listOfPieces[0].color == (255,255,255) and len(spike.listOfPieces)<2)):
        manageSpike(spike)
        return True
    else:
        return False
def nextTurn():
    print("Next turn")
    """
    if(board.dice1.numberOnDice == 0 and board.dice2.numberOnDice == 0):
        global playerTurn
        if(playerTurn == True):
            playerTurn = False
        else: 
            playerTurn = True
        board.throwDices() 
    """
    global playerTurn
    if(playerTurn == True):
        playerTurn = False
    else: 
        playerTurn = True
    #board.throwDices() 
    
def managePiece(piece: Piece):
    global highlightedPiece
    if(highlightedPiece != None):
        removeHighlight()
    if(playerTurn):
        highlight(piece.allSpikes[-1].listOfPieces[-1])
        draw()
    else:
        highlightedPiece = piece
def manageSpike(spike):
    #Spike je prázdný
   if(len(spike.listOfPieces)==0):
       movePiece(spike) 
       #Na spike je jeden kámen
   elif(len(spike.listOfPieces)==1):
       if(spike.listOfPieces[0].color == (0,0,0)):
           popedPiece = spike.removePiece()
           if(popedPiece != None):
               #kámen se vyhodí a dá se na bar
               playerB.playerBar.addPiece(popedPiece)
       movePiece(spike)
       #Na spike je víc kamenů
   elif(len(spike.listOfPieces)>1 and len(spike.listOfPieces) < 5 and spike.listOfPieces[0].color == (255,255,255)):
       movePiece(spike)
   elif(not(playerTurn)):
       return False
     
   removeHighlight()
   draw()
def draw():
    WIN.fill(WIN_COLOR)
    board.drawGameBoard(WIN)
    pygame.display.update()

def movePiece(spike):
    global highlightedPiece
    highlightedPiece.allSpikes[-1].removePiece()
    difference = abs(spike.id - highlightedPiece.allSpikes[-1].id)
    #useDice(difference)
    spike.addPiece(highlightedPiece)
    highlightedPiece.addSpike(spike)
    nextTurn()  
def useDice(number: int):
    if(number == board.dice1.numberOnDice):
        board.dice1.numberOnDice = 0
    elif (number == board.dice2.numberOnDice):
        board.dice2.numberOnDice = 0
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
