# Unit Conversion Toolkit

A modular command-line application written in Python that performs common unit conversions across multiple measurement categories through an interactive menu-driven interface.

---

## Overview

The Unit Conversion Toolkit is a terminal-based utility designed to convert values between different measurement systems. The program groups conversions into logical categories and provides an easy-to-use menu for selecting the desired operation.

The project focuses on writing reusable conversion functions, documenting code with docstrings and type hints, and organizing a larger Python program into maintainable components.

---

## Features

### Temperature Conversions
- Fahrenheit → Celsius
- Celsius → Fahrenheit
- Celsius → Kelvin
- Fahrenheit → Kelvin
- Kelvin → Celsius
- Kelvin → Fahrenheit

### Distance Conversions
- Miles → Kilometers
- Kilometers → Miles
- Meter → Foot
- Foot → Meter

### Weight Conversions
- Pounds → Kilograms
- Kilograms → Pounds

---

## Project Structure

```
unit-conversion-toolkit/
│
├── conversion_toolkit.py
└── README.md
```

---

## How It Works

1. The user selects a conversion category.
2. The user chooses a specific conversion.
3. The program accepts a numerical input.
4. The appropriate conversion function is executed.
5. The converted value is displayed in the terminal.

---

## Example

```
MAIN MENU

1. Temperature
2. Distance
3. Weight
4. Exit

Enter what do you want to convert: 1

TEMPERATURE

1. Fahrenheit → Celsius
2. Celsius → Fahrenheit
3. Celsius → Kelvin
4. Fahrenheit → Kelvin
5. Kelvin → Celsius
6. Kelvin → Fahrenheit

Choose conversion: 2

Enter value: 25

Result: 77.0
```

---

## Programming Concepts Demonstrated

- Functions
- Parameters and return values
- Type hints
- Docstrings
- Variables
- User input
- Arithmetic operations
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Modular program design
- Menu-driven applications

---

## Technologies

- Python 3
- Standard Library only

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JebishaThapa/unit-conversion-toolkit.git
```

Navigate into the project directory:

```bash
cd unit-conversion-toolkit
```

Run the program:

```bash
python conversion_toolkit.py
```

---

## Future Improvements

- Add input validation for invalid numeric values
- Add additional unit categories (time, volume, area, speed)
- Improve output formatting
- Support continuous conversions without returning to the main menu
- Export conversion history to a text file
- Add automated unit tests

---

## Author

**Jebisha Thapa**
