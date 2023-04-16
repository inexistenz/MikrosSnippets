#!/usr/bin/env python3

import unittest

import tictactoe

EMPTY = [[0,0,0],
         [0,0,0],
         [0,0,0]]

DRAW = [[2,1,2],
        [1,1,2],
        [1,2,1]]

X_WIN_CONDITIONS = {
'x_win_diag_1': [[1,0,0],
                 [0,1,0],
                 [0,0,1]],

'x_win_diag_2': [[0,0,1],
                 [0,1,0],
                 [1,0,0]],

'x_win_row_top': [[1,1,1],
                  [0,0,0],
                  [0,0,0]],

'x_win_row_mid': [[0,0,0],
                  [1,1,1],
                  [0,0,0]],

'x_win_row_bot': [[0,0,0],
                  [0,0,0],
                  [1,1,1]],

'x_win_col_left': [[1,0,0],
                   [1,0,0],
                   [1,0,0]],

'x_win_col_mid': [[0,1,0],
                  [0,1,0],
                  [0,1,0]],

'x_win_col_right': [[0,0,1],
                    [0,0,1],
                    [0,0,1]]
}

O_WIN_CONDITIONS = {
'o_win_diag_1': [[2,0,0],
                 [0,2,0],
                 [0,0,2]],

'o_win_diag_2': [[0,0,2],
                 [0,2,0],
                 [2,0,0]],

'o_win_row_top': [[2,2,2],
                  [0,0,0],
                  [0,0,0]],

'o_win_row_mid': [[0,0,0],
                  [2,2,2],
                  [0,0,0]],

'o_win_row_bot': [[0,0,0],
                  [0,0,0],
                  [2,2,2]],

'o_win_col_left': [[2,0,0],
                   [2,0,0],
                   [2,0,0]],

'o_win_col_mid': [[0,2,0],
                  [0,2,0],
                  [0,2,0]],

'o_win_col_right': [[0,0,2],
                    [0,0,2],
                    [0,0,2]]
}


class TestCheckState(unittest.TestCase):

    def test_empty(self):
        result = tictactoe.check_state(EMPTY)
        self.assertEqual(result, -1)

    def test_x_win(self):
        for state in X_WIN_CONDITIONS.values():
            result = tictactoe.check_state(state)
            self.assertEqual(result, 1)

    def test_o_win(self):
        for state in O_WIN_CONDITIONS.values():
            result = tictactoe.check_state(state)
            self.assertEqual(result, 2)

    def test_draw(self):
        result = tictactoe.check_state(DRAW)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
