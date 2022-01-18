from quarto import Quarto
import numpy as np

q = Quarto()
q.init_pieces()
# print(q.pieces)
# print(q.board)
positions = []
for x in range(4):
    for y in range(4):
        positions.append((x, y))
for piece, position in zip(q.pieces, positions):
    q.place_piece(piece, position)
print(q.board)
