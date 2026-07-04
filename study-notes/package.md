# Python packages

- __main__.py allows packages to be executed as a script
- __init__.py declares the directory as a package to python and allows to run set up code.
```txt
my_app/
├── __init__.py  # Runs on 'import my_app'
├── __main__.py  # Runs on 'python -m my_app'
├── core.py
└── utils.py
```
# Python Packages and Imports

Package imports and resolution can seem confusing at first, but the entire system becomes much simpler once you understand a few core concepts.

## `__main__.py`

`__main__.py` allows a package to be executed as a script.

For example:

```bash
python -m package
```

When Python executes the package, it looks for and runs `package/__main__.py`. Think of it as the package's entry point.

---

## `__init__.py`

`__init__.py` marks a directory as a regular Python package (although namespace packages are also supported).

It serves several purposes:

- Initializes the package.
- Executes **once per interpreter session** on the first import.
- Provides a place to expose the package's public API.

Example:

```python
# graphics/__init__.py

from .graph2d.plot2d import Plot2D
from .graph3d.plot3d import Plot3D

__all__ = ["Plot2D", "Plot3D"]
```

This allows consumers to write:

```python
from graphics import Plot2D, Plot3D
```

instead of importing from internal modules.

---

## Prefer Absolute Imports

When working with packages, prefer fully qualified imports:

```python
from package.subpackage.module import MyClass
```

Absolute imports are:

- Easier to read
- More explicit
- Less fragile during refactoring

---

## Relative Imports

Python also supports relative imports within packages.

```python
from .module import Foo
from ..common import Logger
```

Rules:

- `.` refers to the current package.
- `..` moves up one package level.
- Additional dots continue moving upward.

Relative imports are useful for communication between closely related modules inside the same package.

---

## Don't Run Package Modules Directly

Avoid executing package modules directly:

```bash
python package/module.py
```

Instead, run them as modules:

```bash
python -m package.module
```

This ensures Python understands the package hierarchy and resolves imports correctly.

---

## What `-m` Actually Does

The `-m` flag tells Python to locate and execute the target as a **module** rather than as a standalone file.

Doing so:

- Places the project correctly on `sys.path`.
- Sets the module's package context (`__package__`).
- Allows both absolute and relative imports to work as expected.

Without `-m`, Python treats the file as an isolated script, which is why imports often fail.

---

# The Core Mental Model

The most important idea to remember is:

> **Modules exist within a package hierarchy, not in isolation.**

Most import problems occur because the two execution models are mixed:

- Running a file as a standalone script.
- Running a module as part of a package.

As projects grow, it's best to think of everything as belonging to a package. Doing so makes imports predictable, keeps the codebase organized, and naturally scales to larger applications.

In short:

- Use `__init__.py` to define package boundaries and expose the public API.
- Use `__main__.py` to provide an executable entry point.
- Prefer absolute imports.
- Use relative imports for closely related modules.
- Execute package modules with `python -m`, not by running their files directly.