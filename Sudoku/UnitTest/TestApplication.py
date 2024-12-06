import unittest
from Src.Controller.Controller import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def test_solve_sudoku(self):

        input_matrix = [
            [2, 0, 0, 3, 0, 0, 4, 0, 0],
            [0, 3, 0, 0, 4, 0, 0, 5, 0],
            [0, 0, 4, 0, 0, 5, 0, 0, 6],
            [7, 0, 0, 5, 0, 0, 6, 0, 0],
            [0, 8, 0, 0, 6, 0, 0, 7, 0],
            [0, 0, 9, 0, 0, 7, 0, 0, 8],
            [9, 0, 0, 1, 0, 0, 8, 0, 0],
            [0, 1, 0, 0, 2, 0, 0, 9, 0],
            [0, 0, 2, 0, 0, 3, 0, 0, 5]
        ]

        expected_output = [
            [2, 5, 6, 3, 9, 1, 4, 8, 7],
            [8, 3, 7, 6, 4, 2, 9, 5, 1],
            [1, 9, 4, 8, 7, 5, 2, 3, 6],
            [7, 2, 1, 5, 3, 8, 6, 4, 9],
            [4, 8, 5, 2, 6, 9, 1, 7, 3],
            [3, 6, 9, 4, 1, 7, 5, 2, 8],
            [9, 7, 3, 1, 5, 4, 8, 6, 2],
            [5, 1, 8, 7, 2, 6, 3, 9, 4],
            [6, 4, 2, 9, 8, 3, 7, 1, 5]
        ]


        result = solve_sudoku(input_matrix)

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
