import tkinter as tk

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


def main():
    """Main function to run the Sudoku View"""
    root = tk.Tk()  # Initialize the Tkinter root window
    app = SudokuView(root)  # Create an instance of SudokuView

    # Example Sudoku grid
    example_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    app.update_grid(example_grid)  # Update the grid with the example puzzle
    root.mainloop()  # Run the Tkinter main loop

if __name__ == "__main__":
    main()