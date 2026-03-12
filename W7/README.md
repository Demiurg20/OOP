# Calculator Application (PyQt MVC)

## About the Project

This project is a simple calculator application built with Python and PyQt5.

The calculator can perform basic arithmetic operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

The program follows the **Model-View-Controller (MVC)** design pattern.

---

## MVC Structure

### Model (Calculator)

The `Calculator` class contains the main logic of the application.

It stores the current mathematical expression and performs calculations.

Main methods:
- add_to_expression()
- remove_last_character()
- clear_expression()
- calculate()
- get_expression()

---

### View + Controller (CalculatorWindow)

The `CalculatorWindow` class manages the graphical interface and user interaction.

It contains:
- Buttons for digits (0–9)
- Buttons for operators (+ - * /)
- Equals button (=)
- Clear button (C)
- Display field (QLineEdit)

This class connects user actions with the calculator logic.

---

## Features

- Simple graphical calculator
- Supports basic arithmetic operations
- Clear button to reset the expression
- Error handling (for example division by zero)
- MVC architecture

---

## How to Run

1. Install Python 3

2. Install PyQt5
  
  ## pip install PyQt5

3. Run the program

 ## python main.py

---

## Example Input / Output

Example:

Input: 5 + 3
Output: 8

Input: 10/0
Output: Error: Division by zero

---

## Screenshots

Screenshots of different calculations are included in the `screenshots` folder.

Examples:
- Basic addition
- Multiplication
- Division
- Error example

---

## Author

Islambek Asylbekov