# Path Fun with Python

Let's explore ways to import modules from different folders into our main application.

## Scenario

We want to run a series of arithmetic operations using modules that implement a single operation.

This is the folder structure:
```
project/
|- more/
|--- addition.py
|- less/
|--- subtraction.py
|- calculator/
|--- calculator.py
```

* `addition.py` implements `add(op1, op2)`
* `subtraction` implements `subtract(op1, op2)`.

Inside calculator.py, we want to call `add` and `subtract`. To do this, we use the following imports in `calculator.py`:
```python
from addition import add
from subtraction import subtraction
```

And when we run `python project/calculator/calculator.py` we get the following error:
```python
ModuleNotFoundError: No module named 'addition'
```

## Package Method with __init__.py

Use `calculator` as a module with the following structure:

```
project_package/
|- __init.py__
|- addition/
|--- __init.py__
|--- addition.py
|- subtraction/
|--- __init.py__
|--- subtraction.py
|- calculator/
|--- __init.py__
|--- calculator.py
```

Each subdirectory is now a sub-module thanks to the `__init__.py` files.

We can use relative imports for the operations:
```python
from ..more.addition import add
from ..less.subtraction import subtract
```

Run `calculator.py` as a module:
```
path_fun$ python -m project_package.calculator.calculator
10 + 20 = 30
30 - 15 = 15
```

## Path Method with Shell Export

Use the following structure:
```
project_shell_path/
|- addition/
|--- addition.py
|- subtraction/
|--- subtraction.py
|- calculator/
|--- calculator.py
```

Add the project root path to the PYTHONPATH variable.
```bash
path_fun/project_shell_path$ export PYTHONPATH=$PYTHONPATH:$PWD
```

Import the operations this way:
```python
from more.addition import add
from less.subtraction import subtract
```

Run `calculator.py`:
```
path_fun$ python -m project_shell_path/calculator/calculator.py
10 + 20 = 30
30 - 15 = 15
```

## Path Method with Scripted Path Update 

Use the following structure:
```
project_script_path/
|- addition/
|--- addition.py
|- subtraction/
|--- subtraction.py
|- calculator/
|--- calculator.py
```

Add the project root path to the PYTHONPATH variable using the `sys` and `os` packages.
```python
import os
import sys
    
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
```

Import the operations this way:
```python
from more.addition import add
from less.subtraction import subtract
```

Run `calculator.py`:
```
path_fun$ python -m project_script_path/calculator/calculator.py
10 + 20 = 30
30 - 15 = 15
```
