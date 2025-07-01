# Python AI/ML Fundamentals Learning Repository

[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-2.3.1-orange.svg)](https://numpy.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.0-green.svg)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.3-red.svg)](https://matplotlib.org)

A comprehensive learning repository covering Python fundamentals, data structures, object-oriented programming, and data analysis with popular libraries like NumPy, Pandas, and Matplotlib. This repository is designed for beginners and intermediate learners who want to master Python programming and dive into data analysis and machine learning.

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Learning Modules](#learning-modules)
- [How to Run](#how-to-run)
- [Sample Datasets](#sample-datasets)
- [Key Features](#key-features)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This repository contains structured learning materials for Python programming with a focus on data analysis and machine learning fundamentals. Each module includes Jupyter notebooks with comprehensive examples, explanations, and hands-on exercises.

### What You'll Learn:
- **Python Fundamentals**: Variables, data types, operators, and basic syntax
- **Control Flow**: Conditional statements and loops
- **Data Structures**: Lists, tuples, sets, and dictionaries
- **Functions**: Regular functions, lambda functions, map, and filter
- **Modules & Packages**: Importing libraries and creating custom packages
- **File Handling**: Reading, writing, and manipulating files
- **Exception Handling**: Error handling and debugging
- **Object-Oriented Programming**: Classes, objects, inheritance, polymorphism, and encapsulation
- **Advanced Python**: Iterators and generators
- **Data Analysis**: NumPy for numerical computing, Pandas for data manipulation, and Matplotlib for visualization

## 🛠️ Prerequisites

- Basic understanding of programming concepts
- Python 3.12 or higher installed on your system
- Jupyter Notebook or JupyterLab for running `.ipynb` files
- Basic familiarity with command line/terminal

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd AiMlBasicPython
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Jupyter Notebook (if not already installed)
```bash
pip install jupyter
```

## 📂 Project Structure

```
AiMlBasicPython/
├── 01-Python/                           # Python Fundamentals
│   ├── 01-basics/                       # Basic Python syntax and rules
│   ├── 02-variables/                    # Variables and naming conventions
│   ├── 03-dataTypes/                    # Data types (int, float, string, bool)
│   ├── 04-operators/                    # Arithmetic, comparison, logical operators
│   └── 05-input-operation/              # User input and basic operations
│
├── 02-Control-flow/                     # Control Flow Structures
│   ├── 01-conditional-statements/       # if, elif, else statements
│   └── 02-loops-in-python/             # for and while loops
│
├── 03-inbuilt-data-structures/         # Python Data Structures
│   ├── 01-list/                        # Lists: creation, methods, operations
│   ├── 02-tuple/                       # Tuples: immutable sequences
│   ├── 03-sets/                        # Sets: unique collections
│   └── 04-dictionaries/                # Dictionaries: key-value pairs
│
├── 04-functions-in-python/             # Functions and Functional Programming
│   ├── 01-functions/                   # Function definition, parameters, return
│   ├── 02-lambda-function/             # Anonymous functions
│   ├── 03-map-function/                # map() function for transformations
│   └── 04-filter-function/             # filter() for conditional selection
│
├── 05-importing-modules-packages/      # Modules and Package Management
│   ├── 01-importing-from-made-libraries/ # Importing standard libraries
│   └── 02-making-custom-packages/      # Creating custom packages and modules
│
├── 06-File-handling/                   # File Operations
│   ├── 01app.ipynb                     # Basic file operations
│   ├── 02-file_path_os/                # File paths and OS operations
│   └── [Various example files]         # Sample files for practice
│
├── 07-Exception-handling/              # Error Handling
│   └── app.ipynb                       # Try-except blocks, custom exceptions
│
├── 08-Oops/                           # Object-Oriented Programming
│   ├── 01-classes-and-objects/        # Classes, objects, __init__ method
│   ├── 02-inheritence/                # Inheritance and method overriding
│   ├── 03-polymorphism/               # Polymorphism and method overloading
│   ├── 04-encapsulation/              # Private attributes and methods
│   └── 05-Abstraction/                # Abstract classes and methods
│
├── 09-Advance-Python/                 # Advanced Python Concepts
│   ├── 01-iterartors-in-python/       # Custom iterators and __iter__
│   └── 02-generator-in-python/        # Generators and yield keyword
│
└── 10-data-analysis-with-python/      # Data Analysis and Visualization
    ├── 01-Numpy/                      # NumPy for numerical computing
    │   ├── 01-Numpy-Intro/            # Introduction and installation
    │   ├── 02-Numpy-creating-array/   # Array creation methods
    │   ├── 03-Numpy-Array-Indexing/   # Array indexing and access
    │   ├── 04-Numpy-Array-Slicing/    # Array slicing operations
    │   ├── 05-Numpy-Data-Types/       # NumPy data types
    │   ├── 06-Numpy-Copy-vs-View/     # Copy vs View concepts
    │   ├── 07-Numpy-Array-Shape/      # Array shape manipulation
    │   ├── 08-Numpy-Array-Iterating/  # Iterating through arrays
    │   ├── 09-Numpy-Joining-Array/    # Concatenating arrays
    │   ├── 10-Numpy-Splitting-Array/  # Splitting arrays
    │   ├── 11-Numpy-Array-Search/     # Searching in arrays
    │   ├── 12-Numpy-Array-Sort/       # Sorting arrays
    │   └── 13-Numpy-Array-Filter/     # Filtering arrays
    │
    ├── 02-Pandas/                     # Pandas for data manipulation
    │   ├── 01-Pandas-Intro/           # Introduction to Pandas
    │   ├── 02-Pandas-Series/          # Pandas Series operations
    │   ├── 03-Pandas-Dataframes/      # DataFrame creation and operations
    │   ├── 04-Pandas-Read-CSV/        # Reading CSV files
    │   ├── 05-Pandas-Read-JSON/       # Reading JSON files
    │   ├── 06-Pandas-Analyzing-Data/  # Data analysis techniques
    │   ├── 07-Cleaning-Data/          # Data cleaning methods
    │   │   ├── 01-Cleaning-Empty-Cells/    # Handling missing data
    │   │   ├── 02-Cleaning-Wrong-Format/   # Data format corrections
    │   │   └── 03-Cleaning-Wrong-Data/     # Data validation and cleaning
    │   └── 08-Pandas-Correlations/    # Statistical correlations
    │
    └── 03-Matplotlib/                 # Matplotlib for data visualization
        ├── 01-Matplot-Intro/          # Introduction to Matplotlib
        ├── 02-Matplot-Pyplot/         # Pyplot interface
        ├── 03-Matplot-Line/           # Line plots
        ├── 04-Matplot-Labels/         # Adding labels and titles
        ├── 05-Matplot-Grid/           # Grid customization
        ├── 06-Matplot-Subplot/        # Multiple subplots
        ├── 07-Matplot-Scatter/        # Scatter plots
        ├── 08-Matplot-Bars/           # Bar charts
        ├── 09-Matplot-Histograms/     # Histograms
        └── 10-Matplot-PieCharts/      # Pie charts
```

## 📚 Learning Modules

### 1. Python Fundamentals (01-Python/)
Learn the basics of Python programming including syntax rules, variables, data types, and operators.

**Key Topics:**
- Case sensitivity and indentation rules
- Variable declaration and naming conventions
- Data types: integers, floats, strings, booleans
- Arithmetic, comparison, and logical operators
- User input and basic operations

### 2. Control Flow (02-Control-flow/)
Master conditional statements and loops for program flow control.

**Key Topics:**
- if, elif, else statements
- for and while loops
- Loop control: break, continue, pass
- Nested loops and conditions

### 3. Data Structures (03-inbuilt-data-structures/)
Understand Python's built-in data structures and their operations.

**Key Topics:**
- **Lists**: Mutable sequences, indexing, slicing, methods
- **Tuples**: Immutable sequences, packing/unpacking
- **Sets**: Unique collections, set operations
- **Dictionaries**: Key-value pairs, dictionary methods

### 4. Functions (04-functions-in-python/)
Learn about function definition, parameters, and functional programming concepts.

**Key Topics:**
- Function definition and calling
- Parameters: positional, keyword, default, *args, **kwargs
- Lambda functions (anonymous functions)
- map() and filter() functions
- Scope and lifetime of variables

### 5. Modules and Packages (05-importing-modules-packages/)
Understand how to work with modules and create custom packages.

**Key Topics:**
- Importing standard library modules
- Creating custom modules and packages
- Package structure and __init__.py files
- Module search path and PYTHONPATH

### 6. File Handling (06-File-handling/)
Learn to read, write, and manipulate files in Python.

**Key Topics:**
- File opening modes (read, write, append)
- Reading and writing text files
- Working with binary files
- File paths and OS operations
- Context managers (with statement)

### 7. Exception Handling (07-Exception-handling/)
Master error handling and debugging techniques.

**Key Topics:**
- try-except-else-finally blocks
- Common exception types
- Custom exception classes
- Debugging strategies

### 8. Object-Oriented Programming (08-Oops/)
Comprehensive coverage of OOP concepts in Python.

**Key Topics:**
- **Classes and Objects**: Class definition, object creation, __init__ method
- **Inheritance**: Single and multiple inheritance, super() function
- **Polymorphism**: Method overriding, duck typing
- **Encapsulation**: Private attributes, property decorators
- **Abstraction**: Abstract base classes, interfaces

### 9. Advanced Python (09-Advance-Python/)
Explore advanced Python concepts for efficient programming.

**Key Topics:**
- **Iterators**: Creating custom iterators, __iter__ and __next__
- **Generators**: Generator functions, yield keyword, memory efficiency

### 10. Data Analysis (10-data-analysis-with-python/)
Comprehensive data analysis toolkit using popular libraries.

#### NumPy (Numerical Computing)
- Array creation and manipulation
- Indexing, slicing, and broadcasting
- Mathematical operations and functions
- Linear algebra operations

#### Pandas (Data Manipulation)
- Series and DataFrame operations
- Data reading/writing (CSV, JSON)
- Data cleaning and preprocessing
- Statistical analysis and correlations

#### Matplotlib (Data Visualization)
- Basic plotting with pyplot
- Customizing plots with labels, grids, colors
- Multiple plot types: line, scatter, bar, histogram, pie
- Subplots and figure management

## 🏃‍♂️ How to Run

### Running Individual Notebooks

1. **Navigate to desired module:**
```bash
cd 01-Python/01-basics/
```

2. **Start Jupyter Notebook:**
```bash
jupyter notebook app.ipynb
```

3. **Or start JupyterLab:**
```bash
jupyter lab app.ipynb
```

### Running Python Scripts

For modules with `.py` files:
```bash
cd 05-importing-modules-packages/02-making-custom-packages/
python test.py
```

### Running All Notebooks (Advanced)

To run all notebooks in sequence:
```bash
# Install nbconvert if not already installed
pip install nbconvert

# Execute all notebooks
find . -name "*.ipynb" -exec jupyter nbconvert --to notebook --execute {} \;
```

## 📊 Sample Datasets

The repository includes several sample datasets for hands-on practice:

- **data.csv**: Fitness tracking data with Duration, Pulse, MaxPulse, and Calories
- **data.json**: JSON format data for JSON handling exercises
- **Various text files**: For file handling practice

## ✨ Key Features

- **📝 Interactive Notebooks**: All lessons are in Jupyter notebook format for hands-on learning
- **🔗 Progressive Learning**: Modules are structured from basic to advanced concepts
- **💡 Real Examples**: Practical examples and use cases throughout
- **📊 Data Analysis Focus**: Comprehensive coverage of NumPy, Pandas, and Matplotlib
- **🧹 Clean Code**: Well-commented code following Python best practices
- **🔧 Custom Packages**: Learn to create your own Python packages
- **📈 Visualization**: Data visualization techniques with Matplotlib
- **🎯 Practical Exercises**: Hands-on exercises with real datasets

## 🎯 Learning Path Recommendations

### For Complete Beginners:
1. Start with `01-Python/` (Python Fundamentals)
2. Move to `02-Control-flow/` (Control Flow)
3. Learn `03-inbuilt-data-structures/` (Data Structures)
4. Practice with `04-functions-in-python/` (Functions)

### For Intermediate Learners:
1. Review `05-importing-modules-packages/` (Modules)
2. Master `06-File-handling/` (File Operations)
3. Understand `07-Exception-handling/` (Error Handling)
4. Learn `08-Oops/` (Object-Oriented Programming)

### For Data Analysis Track:
1. Complete Python fundamentals (modules 1-8)
2. Learn `09-Advance-Python/` (Advanced Concepts)
3. Master `10-data-analysis-with-python/01-Numpy/` (NumPy)
4. Practice `10-data-analysis-with-python/02-Pandas/` (Pandas)
5. Visualize with `10-data-analysis-with-python/03-Matplotlib/` (Matplotlib)

## 🛡️ Best Practices Covered

- **Code Style**: PEP 8 compliance and readable code
- **Documentation**: Proper docstrings and comments
- **Error Handling**: Robust exception handling patterns
- **Testing**: Basic testing concepts and practices
- **Version Control**: Git workflow and best practices
- **Virtual Environments**: Dependency management

## 🔧 Troubleshooting

### Common Issues:

1. **Jupyter Notebook not starting:**
   ```bash
   pip install --upgrade jupyter
   ```

2. **Import errors:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Kernel issues:**
   ```bash
   python -m ipykernel install --user --name=venv
   ```

4. **Path issues with custom packages:**
   - Ensure you're in the correct directory
   - Check PYTHONPATH if needed

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Python Software Foundation for the amazing Python language
- NumPy, Pandas, and Matplotlib communities for excellent libraries
- Jupyter Project for interactive computing environment

---

**Happy Learning! 🚀**

For questions or support, please open an issue in the repository. 