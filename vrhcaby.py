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
board = None
gamePiece = None
radius = 25


        
def main():
    playerB = Player("black")
    playerW = Player("white")
    global board
    board = GameBoard(playerB, playerW) 
    global gamePiece
    
    print(len(board.boardList))
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

            # Kontrola, na který kámen bylo kliknuto
            
                for piece in board.playerPieceList:
                    draw()
                    if piece.x - 25 <= click_x <= piece.x + 25 and piece.y - 25 <= click_y <= piece.y + 25:
                        # Kliknutí na hrací kámen
                        piece.color = (255, 200, 0)
                        print("Překreslil jsem se")
                    else:
                        piece.color = (255,255,255)
            #TODO podle hodu kostky udělat malé kolečko hráčovy barvy podle toho, kam s piece může pohnout
            # hodím 3.. na 3. spikeu se udělá malé bílé kolečko, když kliknu na ten spyke, piece se tam přemístí a kolečko zmizí
        draw()

    pygame.quit()

       
def draw():
    WIN.fill(WIN_COLOR)
    board.drawGameBoard(WIN)
    pygame.display.update()




main()
