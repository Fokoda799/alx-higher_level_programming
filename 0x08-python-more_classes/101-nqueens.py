#!/usr/bin/python3
""" N queens """

import sys


class NQueens:
    """ N queens"""
    def __init__(self, N):
        self.N = N
        self.board = [0, 0] * N

    def safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row):
        if row == self.N:
            print([[i, self.board[i]] for i in range(self.N)])
            return

        for col in range(self.N):
            if self.safe(row, col):
                self.board[row] = col
                self.solve(row + 1)
                self.board[row] = 0


def main():
    """ Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return 1

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return 1

    if N < 4:
        print("N must be at least 4")
        return 1

    game_1 = NQueens(N)
    game_1.solve(0)


if __name__ == "__main__":
    main()
