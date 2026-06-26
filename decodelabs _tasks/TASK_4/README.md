# Quiz Game using Python

## Overview
This is a simple command-line Quiz Game developed in Python. The program asks the user three general knowledge questions, checks each answer, and maintains a score throughout the quiz. At the end, it displays the user's final score.

The project demonstrates the use of user input, conditional statements, string manipulation, and the accumulator pattern.

## Features
- Asks three quiz questions.
- Accepts user input.
- Removes unwanted spaces using `.strip()`.
- Ignores uppercase/lowercase differences using `.lower()`.
- Uses an accumulator (`score`) to keep track of correct answers.
- Displays feedback after every answer.
- Shows the final score using formatted string literals (f-strings).

## Concepts Used
- Variables
- User Input (`input()`)
- Conditional Statements (`if-else`)
- String Methods
  - `.strip()`
  - `.lower()`
- Accumulator Pattern (`score += 1`)
- Formatted Output (f-strings)

## Requirements
- Python 3.x

## How to Run

1. Save the program as `quiz_game.py`.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the program using:

```bash
python quiz_game.py
```

or

```bash
python3 quiz_game.py
```

## Sample Output

```
1. What is the capital of France?
Paris
Correct!

2. Which planet is known as the Red Planet?
mars
Correct!

3. What is the largest ocean on Earth?
pacific
Correct!

Quiz Completed!
Your final score is 3/3.
```

## Learning Outcomes
- Understand how to receive user input.
- Learn data normalization using string methods.
- Implement decision-making with if-else.
- Maintain application state using an accumulator.
- Display dynamic output using f-strings.

## Author
Uday Kiran