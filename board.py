
import pygame
from constants import PIECES, SQUARE_SIZE, ROWS, COLS, BROWN, WHITE, RED, GREEN
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.green_left = PIECES
        self.winner_red = 0
        self.winner_green = 0
        self.create_board()

    def draw_squares(self, screen):
        """
        Drawing brown squares on board
        """
        screen.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                sq = SQUARE_SIZE
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                pygame.draw.rect(screen, BROWN, (x, y, sq, sq))

#     def add_pieces_around(self, row, col):
#         if not isinstance(self.board[row][col-1], Piece):
#             self.board[row][col-1] = Piece(row, col-1, GREEN)
#             self.green_left -= 1
#         elif not isinstance(self.board[row+1][col], Piece):
#             self.board[row+1][col] = Piece(row, col, GREEN)
#             self.green_left -= 1
#         else:
#             pass

#     # def add_pieces_around(self, row, col, step):
#     #     for i in range(step):
#     #         self.board[row + i][col - 1] = Piece(row + i, col - 1, GREEN)
#     #         self.green_left -= 1

#     def create_board(self):
#         """
#         create self.board which consists lists of rows,
#         inside of each list of rows, there're pieces or empty square (0)
#         """
#         # for row in range(ROWS):
#         #     self.board.append([0] * COLS)  # Utworzenie wiersza z COLS elementami o wartości 0
#         # print(self.board)


#         self.board = [[0] * COLS for _ in range(ROWS)]

# # Dodanie pionków do planszy
#         self.board[0][COLS-1] = Piece(0, COLS-1, GREEN)
#         self.green_left -= 1

#         # Dodanie kolejnych 5 pionków wokół pierwszego pionka
#         for i in range(1, 6):
#             self.add_pieces_around(0, COLS-1, i)
#         print(self.board)






    def create_board(self):
        """
        create self.board which consists lists of rows,
        inside of each of list of rows there're pieces or empty square (0)
        """
        constant = PIECES // 4
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):

                if PIECES == 6:
                    max_piec_in_row = PIECES//2
                    if col >= COLS - max_piec_in_row and row < max_piec_in_row:
                        if col >= COLS - max_piec_in_row + row:
                            self.board[row].append(Piece(row, col, GREEN))
                        else:
                            self.board[row].append(0)
                    elif row >= ROWS-max_piec_in_row and col < max_piec_in_row:
                        if row >= ROWS - max_piec_in_row + col:
                            self.board[row].append(Piece(row, col, RED))
                        else:
                            self.board[row].append(0)
                    else:
                        self.board[row].append(0)

                elif PIECES == 13 or PIECES == 19:
                    if col >= COLS - constant - 1:
                        if row <= PIECES // 4:
                            if row == 0:
                                self.board[row].append(Piece(row, col, GREEN))
                            elif col >= COLS - 2 - constant + row:
                                self.board[row].append(Piece(row, col, GREEN))
                            else:
                                self.board[row].append(0)
                        else:
                            self.board[row].append(0)
                    elif row >= ROWS - constant - 1:
                        if col <= constant:
                            if col == 0:
                                self.board[row].append(Piece(row, col, RED))
                            elif row >= ROWS - 2 - constant + col:
                                self.board[row].append(Piece(row, col, RED))
                            else:
                                self.board[row].append(0)
                        else:
                            self.board[row].append(0)
                    else:
                        self.board[row].append(0)
                else:
                    raise ValueError("Number of pieces can be 6, 13 or 19")

        print(self.board)



    def check_winner(self):
        constant = PIECES // 4
        for row in range(ROWS):
            for col in range(COLS):
                if PIECES == 6:
                    max_piec_in_row = PIECES//2
                    if col >= max_piec_in_row and row < max_piec_in_row:
                        if col >= COLS - max_piec_in_row + row:
                            if self.board[row] == (Piece(row, col, RED)):
                                self.red_left -= 1
                    elif row >= max_piec_in_row and col < max_piec_in_row:
                        if row >= ROWS - max_piec_in_row + col:
                            if self.board[row] == (Piece(row, col, GREEN)):
                                self.green_left -= 1

                elif PIECES == 13 or PIECES == 19:
                    if col >= COLS - constant - 1:
                        if row <= PIECES // 4:
                            if row == 0:
                                self.board[row] == (Piece(row, col, RED))
                                self.red_left -= 1
                            elif col >= COLS - 2 - constant + row:
                                if self.board[row] == (Piece(row, col, RED)):
                                    self.red_left -= 1

                    elif row >= ROWS - constant - 1:
                        if col <= constant:
                            if col == 0:
                                if self.board[row] == (Piece(row, col, GREEN)):
                                    self.green_left -= 1
                            elif row >= ROWS - 2 - constant + col:
                                if self.board[row] == (Piece(row, col, GREEN)):
                                    self.green_left -= 1

        if self.winner_green == self.green_left:
            return GREEN
        elif self.winner_red == self.red_left:
            return RED

    #     return None

    def draw(self, screen):
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    # def remove(self, pieces):
    #     for piece in pieces:
    #         self.board[piece.row][piece.col] = 0

    def move(self, piece, row, col):
        """
        Swaping positions of piece and "0" in empty square
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_options_of_move(self, piece):
        """
        Start (min_jump) from row of the piece, stop (max_jump) for 2 rows
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        col = piece.col
        row = piece.row
        # (4,5): [(2,3)]

        # traverse left up
        moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))

        # traverse right up
        moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        # traverse left down
        moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))

        # traverse right down
        moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))

        # go up
        # wczesenije bylo max(row-3, -1)
        moves.update(self._up(row-1, max(row-3, -1), -1, piece.color, col))

        # go down
        moves.update(self._down(row+1, min(row+3, ROWS), 1, piece.color, col))

        # go right
        moves.update(self._right(col+1, min(col+3, COLS), 1, piece.color, row))

        # go left
        moves.update(self._left(col-1, max(col-3, -1), -1, piece.color, row))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))

                break
            else:
                last = [current]
            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            else:
                last = [current]
            right += 1
        return moves

    def _up(self, start, stop, step, color, up, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if up < 0:
                break

            current = self.board[r][up]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, up)] = last + skipped
                else:
                    moves[(r, up)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._up(r+step, row, step, color, up, skipped=last))
                break
            else:
                last = [current]
        return moves

    def _down(self, start, stop, step, color, down, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if down >= ROWS:
                break

            current = self.board[r][down]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, down)] = last + skipped
                else:
                    moves[(r, down)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._down(r+step, row, step, color, down, skipped=last))

                break
            else:
                last = [current]
        return moves

    def _right(self, start, stop, step, color, right_row, skipped=[]):
        moves = {}
        last = []
        for c in range(start, stop, step):
            if c > COLS:
                break

            current = self.board[right_row][c]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(right_row, c)] = last + skipped
                else:
                    moves[(right_row, c)] = last
                if last:
                    if step == -1:
                        row = max(c-3, 0)
                    else:
                        row = min(c+3, ROWS)

                    # moves.update(self._left(c+step, row, step, color, right_row, skipped=last))
                    moves.update(self._right(c+step, row, step, color, right_row, skipped=last))
                break
            else:
                last = [current]

        return moves

    def _left(self, start, stop, step, color, left_row, skipped=[]):
        moves = {}
        last = []
        for c in range(start, stop, step):
            if c < 0:
                break

            current = self.board[left_row][c]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(left_row, c)] = last + skipped
                    # print(moves)
                else:
                    moves[(left_row, c)] = last
                    # print(f"{moves} 3")
                if last:
                    if step == -1:
                        row = max(c-3, 0)
                    else:
                        row = min(c+3, ROWS)
                    # print(f"{moves} 2")

                    moves.update(self._left(c+step, row, step, color, left_row, skipped=last))
                    # moves.update(self._right(c+step, row, step, color, left_row, skipped=last))
                break
            else:
                last = [current]
        print(moves)
        return moves
