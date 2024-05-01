# Python Quines

This repository contains several Python scripts that demonstrate the concept of a "quine," which is a non-trivial computer program that prints its own source code as output.

## What is a Quine?

A quine is a self-replicating program that, when executed, produces a copy of its own source code as output. This seemingly paradoxical concept was first theorized by John von Neumann and has become a recreational programming challenge among computer scientists and programmers.

## Repository Contents

1. **quine.py**: A simple quine program that prints its own source code.

2. **0.py**: A more advanced quine that not only prints its own source code but also creates new Python files containing a modified version of itself. **WARNING: DO NOT RUN THIS FILE UNLESS YOU UNDERSTAND ITS IMPLICATIONS, AS IT COULD POTENTIALLY FILL UP YOUR DISK SPACE.**

3. **0_safe.py**: A safer version of `0.py` that demonstrates the same concept but without the risk of creating an excessive number of files on your system.

## Usage

To run the quine programs, navigate to the repository directory and execute the desired Python script:

```bash
python quine.py
python 0_safe.py
```
**Note**: As mentioned earlier, running `0.py` is not recommended unless you fully understand its behavior and potential consequences.

## Understanding the Code

The code in these scripts leverages Python's string manipulation capabilities and file handling operations to achieve the self-replicating behavior. The core idea is to define a string variable containing the program's source code and then write that string to a new file, effectively creating a copy of the program.

The more advanced versions (`0.py` and `0_safe.py`) use recursion and file numbering to create multiple copies of the program, each with a slightly modified version of the source code.

## Purpose

These quine programs serve as educational examples and programming challenges to explore concepts like self-reference, recursion, and string manipulation. They are not intended for practical use but rather for learning and entertainment purposes.

## Contribution

While contributions to this repository are welcome, please ensure that any added code adheres to the principles of quines and does not introduce any harmful or unintended behavior.