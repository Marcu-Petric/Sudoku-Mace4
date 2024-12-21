# Sudoku Solver Documentation

## Introduction

This Sudoku-solving application is designed to integrate a user-friendly interface with logic-solving capabilities. The core functionality is built around the Mace4 theorem prover.

Users interact with a graphical user interface (GUI) to input their Sudoku puzzles. The application processes the input puzzle by converting it into a Mace4-compatible input. Once the puzzle is formatted, the application invokes the Mace4 program to compute the solution. The solved puzzle is then parsed and displayed back to the user on the GUI.

The application employs a Model-View-Controller (MVC) architecture for modularity and maintainability. The core operations, including file transformations and subprocess handling, are implemented in Python, ensuring seamless interaction between the GUI and the logic-solving backend.

This project demonstrates the practical application of theorem provers in solving real-world problems and how easy it can be used when it is automated and combined with a user-friendly GUI.

## Design

<div align="center">
  <img src="https://github.com/user-attachments/assets/ce8f0457-2bd4-484a-844a-4154ed80fa7e" alt="Package Diagram">
</div>

### Model (`Src/Model`)

The Model component is responsible for the core application logic and data handling. It includes the following files:

- **`GridToProverTransformations.py`**: Handles the transformation of data between different formats, managing input and output files, and interacting with external programs.

### Controller (`Src/Controller`)

The Controller component is responsible for managing the interaction between the Model and the application logic. It includes the following file:

- **`Controller.py`**: Orchestrates the main processing workflow, coordinating the transformation and execution of tasks by calling appropriate functions from the Model.

### View (`Src/View`)

The View component is responsible for presenting data to the user. It renders the user interface by displaying the data provided by the controller and often interacts with templates. It includes the following file:

- **`View.py`**: Responsible for creating and managing the visual representation and user interaction of the Sudoku board.

### Sudoku Rules

#### Exactly one digit per row (maximum one AND minimum one)

$$
\forall r, c_1, c_2 \,  \big( \text{cell}(r, c_1) = \text{cell}(r, c_2) \rightarrow c_1 = c_2 \big) \land \forall r, \text{digit} \, \exists c \,  \big( \text{cell}(r, c) = \text{digit} \big)
$$

#### Exactly one digit per column (maximum one AND minimum one)

$$
\forall r, r_2, c \,  \big( \text{cell}(r_1, c) = \text{cell}(r_2, c) \rightarrow r_1 = r_2 \big) \land \forall c, \text{digit} \, \exists r \,  \big( \text{cell}(r, c) = \text{digit} \big)
$$

#### One digit in each region

Let `same_square(x, y)` be a function that is `TRUE` only when `x` and `y`, which represent either rows or columns, are in the same region.

$$
\forall r_1, r_2, c_1, c_2 \, \big( \text{same-square}(r\_1, r\_2) \land \text{same-square}(c\_1, c\_2) \land \text{cell}(r\_1, c\_1) = \text{cell}(r\_2, c\_2) \rightarrow r\_1 = r\_2 \land c\_1 = c\_2 \big)
$$


## Implementation

### Model

#### Function 1: `to_mace4_input`

```python
def to_mace4_input(m):
```

Converts a 2D matrix representing an unsolved Sudoku puzzle into a string formatted for Mace4. It outputs a string where each cell in the puzzle is expressed as `f(i, j) = x`.

#### Function 2: `insert_input_in_file_content`

```python
def insert_input_in_file_content(mace4functions, file_content):
```

Inserts the Mace4 formatted input string into the content of an input file at a placeholder, returning the updated file content.

#### Function 3: `put_in_input_file`

```python
def put_in_input_file(gui_matrix, path):
```

Reads an input file, inserts the Mace4 formatted input generated from the given matrix, and writes the modified content back to the file. Returns the initial content before modification.

#### Function 4: `reset_input`

```python
def reset_input(initial_file, path):
```

Resets the content of the input file to its original template state using the provided initial content.

#### Function 5: `to_grid`

```python
def to_grid(file_content, size):
```

Parses the content of the Mace4 output file and converts it into a 2D matrix of the specified size, organizing extracted numerical values into a matrix.

#### Function 6: `get_from_output_file`

```python
def get_from_output_file(path):
```

Reads the output file, retrieves its content, and returns it as a 2D matrix representing the solved Sudoku puzzle.

### Controller

#### Function 1: `solve_sudoku`

```python
def solve_sudoku(sudoku_matrix):
```

Runs the Mace4 program with the given Sudoku puzzle, retrieves the solution, and resets the input file to its initial state. Returns the solved puzzle as a matrix.

<div align="center">
  <img src="https://github.com/user-attachments/assets/14f882ae-750d-41f1-a98f-16c1b0fd79fe" alt="Solve Puzzle Sequence Diagram">
</div>


### View

#### Class: `SudokuView`

The `SudokuView` class handles the graphical user interface (GUI) for the Sudoku game using Tkinter. It is responsible for displaying the Sudoku grid, updating it with the puzzle data, and capturing user input.

#### Constructor: `__init__(self, root)`

Initializes the Tkinter window and creates a 9x9 grid of input fields.

#### Method: `create_grid(self)`

Creates the visual grid of the Sudoku puzzle on the Tkinter window.

#### Method: `update_grid(self, grid)`

Updates the displayed grid based on the current puzzle state.

#### Method: `get_input(self)`

Retrieves the user input from the grid.

## Results

After running the program, users can add the digits for their unsolved puzzle and press "Solve."

<div align="center">
  <img src="https://github.com/user-attachments/assets/88f842ff-1a43-4861-a71c-0ebf7e5f7bb5" alt="unsolved">
</div>

A correctly solved puzzle should appear.

<div align="center">
  <img src="https://github.com/user-attachments/assets/aadf83cd-e183-48c0-9eca-f36cfe39ebf4" alt="solved">
</div>

## Conclusion

The integration of Python and Mace4 enables a highly systematic and logical approach to solving Sudoku puzzles, leveraging first-order logic to deduce the correct placement of numbers in the grid efficiently.
