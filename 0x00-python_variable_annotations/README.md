# Python Variable Annotations

## Tasks

### 0-add.py
- Returns type-annotated sum of two floats as float
	- Used with:
		- 0main.py

### 1-concat.py
- Returns type-annotated concat of two strings as string
	- Used with:
		- 1main.py

### 2-floor.py
- Returns type-annotated floor (rounded-down int) from float
	- Used with:
		- 2main.py

### 3-to_str.py
- Returns type-annotated string from float
	- Used with:
		- 3main.py

### 4-define_variables.py
- Define variables with specific values and types
	- Used with:
		- 4main.py

### 5-sum_list.py
- Returns type-annotated sum of list of floats as float
	- Used with:
		- 5main.py

### 6-sum_mixed_list.py
- Returns type-annotated sum of list of ints and floats as float
	- Used with:
		- 6main.py

### 7-to_kv.py
- Returns type-annotated tuple where first index is string and second is int or float
	- Used with:
		- 7main.py

### 8-make_multiplier.py
- Returns type-annotated function that multiplies float by float
	- Used with:
		- 8main.py

### 9-element_length.py
- Duck-type so doesn't matter what types are as long as has specific features
	- Used with:
		- 9main.py

## pep8

### Install pep8:

```
sudo apt-get install pep8
```

### Use pep8:

```
$ pep8 filename.py
```

## mypy

### Install mypy:

```
sudo apt-get install -y python3-pip
python3 -m pip install mypy
```

OR

```
pip3 install mypy
```

OR

```
sudo apt-get install mypy
```

### Use mypy:

```
mypy filename.py
```

## Typing Basics

### Basic
- Any - specify can take any type
- Optional - specify optional parameter, sometimes with =default

### Special
- -> None (for no return)
- Vector = List[type] - to define type variable
- T = TypeVar('T') - generic/flexible if List[T] where all indices should be the same type but don't know type

### Data Structures
- List[type], Dict[type], Set[type]
- Tuple[specify, each, index, type]
- Iterable: used for anything that can be iterated through, regardless of index
- Sequence: used for list, tuple, str only - can be indexed

### Combo
- Union[firstType, secondType] - if can accept different types
- List[Union[float, int]] - if list can accept different types at different indices

### Function
- Callable[[argType, argType], returnType]
- Lambda uses Callable but often declared as variable (esp. when returning)

## Learning Objectives

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy
