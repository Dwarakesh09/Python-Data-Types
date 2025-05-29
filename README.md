# Python Data Types

This repository demonstrates the main built-in data types in Python and how to work with them. Understanding these data types is fundamental for any Python programmer, as they form the basis for storing and manipulating data in your programs.

## Table of Contents

- [Numeric Types](#numeric-types)
- [Sequence Types](#sequence-types)
- [Mapping Type](#mapping-type)
- [Set Types](#set-types)
- [Boolean Type](#boolean-type)
- [None Type](#none-type)
- [Other Types](#other-types)
- [Examples](#examples)
- [How to Use](#how-to-use)
- [License](#license)

---

## Numeric Types

- **int**: Integer values, e.g., `42`, `-7`
- **float**: Floating-point numbers, e.g., `3.14`, `-0.001`
- **complex**: Complex numbers, e.g., `2 + 3j`

## Sequence Types

- **str**: Strings of characters, e.g., `"hello"`, `'Python'`
- **list**: Ordered, mutable collections, e.g., `[1, 2, 3]`, `["a", "b", "c"]`
- **tuple**: Ordered, immutable collections, e.g., `(1, 2, 3)`
- **range**: Sequence of numbers, e.g., `range(5)`

## Mapping Type

- **dict**: Key-value pairs, e.g., `{"name": "Alice", "age": 30}`

## Set Types

- **set**: Unordered collection of unique elements, e.g., `{1, 2, 3}`
- **frozenset**: Immutable set, e.g., `frozenset([1, 2, 3])`

## Boolean Type

- **bool**: Boolean values, `True` or `False`

## None Type

- **NoneType**: Represents the absence of a value, `None`

## Other Types

- **bytes**: Immutable sequence of bytes, e.g., `b"abc"`
- **bytearray**: Mutable sequence of bytes, e.g., `bytearray([50, 100, 76])`
- **memoryview**: A memory view object

---

## Examples

```python
# Numeric Types
x = 5               # int
y = 3.14            # float
z = 2 + 3j          # complex

# Sequence Types
name = "Python"     # str
items = [1, 2, 3]   # list
coords = (10, 20)   # tuple
numbers = range(5)  # range

# Mapping Type
person = {"age": 25, "city": "NY"}  # dict

# Set Types
flags = {True, False}            # set
frozen = frozenset([1, 2, 3])    # frozenset

# Boolean Type
is_active = True

# None Type
nothing = None

# Other Types
data = b"abc"                    # bytes
arr = bytearray([50, 100, 76])   # bytearray
mv = memoryview(b"abc")          # memoryview
```

---

## How to Use

This repository can be used as a reference for Python’s built-in data types. Check out the example scripts for demonstrations on how to create and manipulate each data type.

---

## License

This project is licensed under the MIT License.
