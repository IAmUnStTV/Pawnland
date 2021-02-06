import chess
import chess.svg
import webbrowser as web

ans = str(input('What chess piece do you want (Rook, Pawn, King, Queen, Knight or Bishop)? '))

if ans == 'Rook':
    cp = chess.svg.piece(chess.Piece.from_symbol("R"))
elif ans == 'Pawn':
    cp = chess.svg.piece(chess.Piece.from_symbol("P"))
elif ans == 'King':
    cp = chess.svg.piece(chess.Piece.from_symbol("K"))
elif ans == 'Queen':
    cp = chess.svg.piece(chess.Piece.from_symbol("Q"))
elif ans == 'Knight':
    cp = chess.svg.piece(chess.Piece.from_symbol("N"))
elif ans == 'Bishop':
    cp = chess.svg.piece(chess.Piece.from_symbol("B"))
else:
    cp = 'Error: Couldn\'t read, please run code again'

f = open("svgtest.html", "w")
html = '''
<html>
<head>
<title>SVG Test:'''+ ans +'''</title>
</head>
<body>
<h1>SVG Test In HTML:'''+ ans +'''
<p>A '''+ ans +''' should appear below</p>'''+ cp +'''
</body>
</html>'''
f.write(html)
f.close()
web.open('svgtest.html')
