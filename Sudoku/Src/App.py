import tkinter as tk
from Src.Controller.Controller import solve_sudoku
import Src.View.View
from Src.Config import INPUT_FILE_PATH, OUTPUT_FILE_PATH, PROVER9_BIN_PATH


def main():
    """
    TODO: Start gui, get input from user, etc. Call Controller.solve_sudoku(matrix) then display the solved puzzle
    """
    """Main function to run the Sudoku View"""
    root = tk.Tk()  # Initialize the Tkinter root window
    app = Src.View.View.SudokuView(root)  # Create an instance of SudokuView

    # Example Sudoku grid (can be replaced with loading logic from INPUT_FILE_PATH)
    example_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # example_grid = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]

    app.update_grid(example_grid)  # Update the grid with the example puzzle

    # Solve the Sudoku puzzle using the Controller
    def solve_and_update():
        grid_input = app.get_input()# Get the current input from the GUI
        print(grid_input)
        try:
            solved_grid = solve_sudoku(grid_input)  # Call to the Controller
            app.update_grid(solved_grid)  # Update the GUI with the solved puzzle
            print("Solved Sudoku Grid:")
            for row in solved_grid:
                print(row)
        except Exception as e:
            print(f"Error solving Sudoku: {e}")

    # Button to get the current grid input
    get_input_button = tk.Button(root, text="Get Input", command=lambda: print(app.get_input()))
    get_input_button.grid(row=10, column=0, columnspan=4, pady=10)  # Place below the grid

    # Button to solve the Sudoku
    solve_button = tk.Button(root, text="Solve", command=solve_and_update)
    solve_button.grid(row=10, column=5, columnspan=4, pady=10)  # Place below the grid

    root.mainloop()  # Run the Tkinter main loop


if __name__ == "__main__":
    main()