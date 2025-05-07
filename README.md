# Connect Four: Score Attack! (PyQt6 Edition)

This project is a Python implementation of a Connect Four-style game with a unique scoring system, featuring a graphical user interface (GUI) built with PyQt6. Instead of simply aiming for the first four-in-a-row, players accumulate a score based on the number of horizontal, vertical, and diagonal connections of four tokens they make throughout the game.

## Features

*   **Graphical User Interface (GUI)**: A playable game board built using PyQt6.
*   **Interactive Board**: Click a column to drop your token.
*   **Visual Feedback**: Placed tokens are visually represented with Yellow and Red colors.
*   **Live Score Display**: The window title dynamically updates to show the current scores for Yellow (Y) and Red (R) players after each move.
*   **Classic Grid**: Standard 6x7 Connect Four game board.
*   **Two Players**: "Yellow" (Y) and "Red" (R) players take turns.
*   **Turn-Based Gameplay**: Players alternate placing their tokens.
*   **Gravity**: Tokens fall to the lowest available spot in the selected column.
*   **Column Full Detection**: Prevents placing tokens in a full column (handled by backend).
*   **Scoring System (Backend)**:
    *   Players earn points for every set of four identical tokens connected horizontally, vertically, or diagonally.
    *   The scoring logic allows for overlapping connections and sequences longer than four to contribute to the score.

## Project Structure

The project is organized into three main Python files:

1.  **`main.py` (Game Logic Engine - Backend):**
    *   Contains the `Game` class which manages:
        *   The 6x7 game board state.
        *   The current player's turn ('Y' or 'R').
    *   Handles the core game mechanics:
        *   `make_move(col)`: Places a token in the specified column, applies gravity, and switches turns. Returns the `(row, col)` of the placed token or `None` if the column is full.
        *   `get_token(row, col)`: Retrieves the token at a board position.
    *   Implements the scoring logic:
        *   `check(color)`: Calculates the total score for a player.
        *   `all_row(color)`, `all_col(color)`, `all_x(color)`: Sum scores from rows, columns, and diagonals respectively.
        *   Helper functions (`Row_check`, `col_check`, `diagonal_check`, `x_diagonal_check`, `valid`): Perform detailed checks for scoring sequences.
    *   Prints scores to the console after each move (in addition to the GUI update).

2.  **`ui_form.py` (GUI Definition - Frontend Layout):**
    *   Contains the `Ui_Widget` class.
    *   Defines the visual layout of the game window using PyQt6 widgets.
    *   Sets up a 6x7 grid of `QPushButton` objects, each representing a slot on the Connect Four board.
    *   *Note: The game logic methods like `Row_check` in this file are placeholders, as the actual logic is in `main.py`.*

3.  **`widget.py` (Application Controller & Main Executable):**
    *   Contains the `Widget` class, which inherits from `QWidget`.
    *   Acts as the central controller that connects the game logic (`main.py`) with the UI definition (`ui_form.py`).
    *   Initializes an instance of `Game` (from `main.py`) and `Ui_Widget` (from `ui_form.py`).
    *   **`setup_ui_connections()`**: Connects the `clicked` signal of each `QPushButton` in the grid to the `make_move()` method. A lambda function is used to pass the column index of the clicked button.
    *   **`make_move(col)`**:
        *   Calls `self.game.make_move(col)` from the backend to process the move.
        *   Updates the window title with the current scores using `self.game.check('Y')` and `self.game.check('R')`.
        *   If the move is valid and a token is placed:
            *   Retrieves the token type ('Y' or 'R') using `self.game.get_token(row, col)`.
            *   Updates the stylesheet of the corresponding `QPushButton` in the UI to display the token's color (Yellow or Red).
    *   Contains the `if __name__ == "__main__":` block to launch the PyQt6 application.

## How It Works

1.  When `widget.py` is executed, it creates a `QApplication` and an instance of our `Widget` class.
2.  The `Widget` class initializes:
    *   The game logic engine (`Game` from `main.py`).
    *   The UI layout (`Ui_Widget` from `ui_form.py`), which creates the grid of buttons.
3.  `setup_ui_connections()` in `widget.py` links each button's click event. When any button in the grid is clicked, it triggers the `Widget.make_move(col)` method, passing the column index of the *top-most button in that column* (as all buttons in a column are connected to drop a token in that column).
4.  Inside `Widget.make_move(col)`:
    *   The game engine's `self.game.make_move(col)` is called. This updates the internal game board, determines the actual row where the token lands, and switches the player turn.
    *   The window title is immediately updated to reflect the new scores.
    *   If the move was successful, the specific button `(row, col)` where the token landed is identified.
    *   The `setStyleSheet` method is used on that button to change its background color to yellow or red, visually representing the placed token.
5.  The game continues with players clicking columns to make their moves.

## Prerequisites

*   Python 3.x
*   PyQt6:
    ```bash
    pip install PyQt6
    ```

## How to Run

1.  Ensure all three Python files (`main.py`, `ui_form.py`, and `widget.py`) are in the same directory.
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the files.
4.  Run the main application script:
    ```bash
    python widget.py
    ```
5.  The "Connect Four: Score Attack!" game window will appear. Click on any button in a column to drop your token. The window title will display the current scores.

## Potential Enhancements

*   **Visual Indication of Current Player**: Display whose turn it is on the GUI.
*   **Game Reset Button**: Add a button to clear the board and start a new game.
*   **Win/Game Over Condition**:
    *   Define a target score to win.
    *   Detect when the board is full and declare a winner based on scores or a draw.
    *   Display game over messages.
*   **More Sophisticated Visuals**: Use custom images for tokens instead of just background colors.
*   **Error Handling/Feedback**: Provide visual feedback if a player tries to play in a full column.
*   **Animation**: Animate the token dropping.
*   **AI Opponent**: Integrate an AI to play against.
*   **Refined UI Layout**: Use Qt Designer for more complex layouts and add dedicated score labels instead of just using the window title.
