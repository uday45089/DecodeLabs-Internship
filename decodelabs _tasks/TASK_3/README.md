# Secure Password Generator

## Description

This Python program generates strong and secure passwords based on a user-specified length. It follows modern password security recommendations by using the `secrets` module instead of the `random` module.

## Features

* User-defined password length
* Supports lengths between 15 and 64 characters
* Uses uppercase and lowercase letters
* Uses digits
* Uses special characters
* Cryptographically secure randomness with `secrets.choice()`

## Requirements

* Python 3.x

## Modules Used

* secrets
* string

## How to Run

1. Save the program as `password_generator.py`
2. Open a terminal.
3. Run:

```bash
python3 password_generator.py
```

4. Enter a password length between 15 and 64.
5. The program will generate and display a secure password.

## Example

Input:

```
Enter password length (15-64 characters): 18
```

Output:

```
Generated Secure Password:
x#7P@Lm9!Qa2&Zr5Kd
```

## Security Notes

* Uses `secrets.choice()` for secure random character selection.
* Follows NIST recommendations for longer passwords.
* Allows up to 64 characters for passphrase compatibility.

