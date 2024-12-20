import tkinter as tk
from Src.Controller.Controller import solve_sudoku

class SudokuView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

    def create_grid(self):
        """Create Sudoku Grid"""
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.root, width = 2, font = ("Arial", 16), justify = "center")
                cell.grid(row = row, column = col, padx = 1, pady = 1)

                """Thicker borders for the 3x3 squares"""
                if row % 3 == 0  and row != 0:
                    cell.grid(pady = (8, 1))
                if col % 3 == 0  and col != 0:
                    cell.grid(padx = (8, 1))

                self.cells[row][col] = cell

    def update_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                if grid[row][col] != 0:
                    self.cells[row][col].insert(0, str(grid[row][col]))
                    self.cells[row][col].config(state = "disabled")

    def get_input(self):
        """Get the user's current input from the grid."""
        return [[int(self.cells[row][col].get()) if self.cells[row][col].get().isdigit() else 0
                 for col in range(9)] for row in range(9)]

