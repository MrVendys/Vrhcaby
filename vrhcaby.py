# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


class player:
    def __init__(self, color: str):
        self.listOfPieces = [piece(color) for _ in range(16)]


class board:
    def __init__(self):
        self.boardList = []
        for i in range(24):
            self.boardList.append([None for _ in range(5)])


class piece:
    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor


gameBoard = board()
Venca = player("black")
Stepan = player("white")
print(Venca.listOfPieces[0].pieceColor)
