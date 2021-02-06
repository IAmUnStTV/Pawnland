import chess
import chess.svg
import webbrowser as web

rook = chess.svg.piece(chess.Piece.from_symbol("R"))
f = open("svgtest.html", "w")
html = '''
<html>
    <head>
        <title>SVG Test: Rook</title>
    </head>
    <body>
        <h1>SVG Test In HTML: Rook</h1>
        <p>A rook should appear below</p>''' + rook +'''
    </body>
</html>'''
f.write(html)
f.close()

#open and read the file after the appending:
web.open('svgtest.html')
