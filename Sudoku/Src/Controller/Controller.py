import sys
import subprocess
from Src.Model.GridToProverTransformations import put_in_input_file, get_from_output_file
from Src.App import INPUT_FILE_PATH, PROVER9_BIN_PATH, OUTPUT_FILE_PATH


def solve_sudoku(sudoku_matrix):
    """


    :param sudoku_matrix: UNSOLVED sudoku puzzle as matrix
    :return: SOLVED sudoku puzzle as matrix
    """

    put_in_input_file(sudoku_matrix, INPUT_FILE_PATH)
    command = f"{PROVER9_BIN_PATH}/mace4 -f {INPUT_FILE_PATH} > {OUTPUT_FILE_PATH}"
    subprocess.run(command, shell=True, check=True, capture_output=True)
    solution = get_from_output_file(OUTPUT_FILE_PATH)

    return solution