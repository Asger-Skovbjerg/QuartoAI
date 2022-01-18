import numpy as np


class Quarto:

    def __init__(self):
        self.board = np.zeros((4, 4, 5))
        self.pieces = None

    def init_pieces(self):
        pieces = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        pieces.append(np.array([1, i, j, k, l], ndmin=2))
        self.pieces = np.concatenate(pieces, axis=0)

    def place_piece(self, piece, position):
        self.board[position] = piece
        self._check_if_won()

    def _check_if_won(self):
        for x in range(4):
            if self.board[x, :, 0].sum() == 4:
                if self._check_slice_for_victory(self.board[x, :, :]):
                    print("VICTORY")
                    print(self.board)

    def _check_slice_for_victory(self, board_slice):
        for quality in range(1, 5):
            slice_sum = board_slice[:, quality].sum()
            if slice_sum == 0 or slice_sum == 4:
                return True
        return False
