import unittest
from Src.GridToProverTransformations import insert_input_in_file_content, to_mace4_input, to_grid


class MyTestCase(unittest.TestCase):

    def test_to_mace4_input(self):
        # Given input: 2D list (Sudoku puzzle)
        test_matrix = [
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

        # Expected output as a formatted string
        expected_output = (
            "f(0,0) = 1.\n"
            "f(0,3) = 2.\n"
            "f(0,6) = 3.\n"
            "f(1,1) = 2.\n"
            "f(1,4) = 3.\n"
            "f(1,7) = 4.\n"
            "f(2,2) = 3.\n"
            "f(2,5) = 4.\n"
            "f(2,8) = 5.\n"
            "f(3,0) = 6.\n"
            "f(3,3) = 4.\n"
            "f(3,6) = 5.\n"
            "f(4,1) = 7.\n"
            "f(4,4) = 5.\n"
            "f(4,7) = 6.\n"
            "f(5,2) = 8.\n"
            "f(5,5) = 6.\n"
            "f(5,8) = 7.\n"
            "f(6,0) = 8.\n"
            "f(6,3) = 0.\n"
            "f(6,6) = 7.\n"
            "f(7,1) = 0.\n"
            "f(7,4) = 1.\n"
            "f(7,7) = 8.\n"
            "f(8,2) = 1.\n"
            "f(8,5) = 2.\n"
            "f(8,8) = 4.\n"
        )

        self.assertEqual(to_mace4_input(test_matrix), expected_output)

    def test_insert_input_in_file_content(self):
        # Given input for the function
        mace4_input = "f(0,0) = 1.\n"
        file_content = "TODO: insert input here"

        # Expected output after insertion
        expected_output = "f(0,0) = 1.\n"

        self.assertEqual(insert_input_in_file_content(mace4_input, file_content), expected_output)

    def test_to_grid(self):
        # Given content for the function
        file_content = (
            "function(f(_,_), [1,4,5,2,8,0,3,7,6,"
            "7,2,6,5,3,1,8,4,0,"
            "0,8,3,7,6,4,1,2,5,"
            "6,1,0,4,2,7,5,3,8,"
            "3,7,4,1,5,8,0,6,2,"
            "2,5,8,3,0,6,4,1,7,"
            "8,6,2,0,4,3,7,5,1,"
            "4,0,7,6,1,5,2,8,3,"
            "5,3,1,8,7,2,6,0,4])"
        )
        size = 9

        # Expected output: 2D matrix representation
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


        self.assertEqual(to_grid(file_content, size), expected_output)


if __name__ == '__main__':
    unittest.main()
