import secrets
import string

# Define character pool
characters = string.ascii_letters + string.digits + string.punctuation

# Ask user for password length
while True:
    try:
        length = int(input("Enter password length (15-64 characters): "))

        if length < 15:
            print("Password must be at least 15 characters long.")
        elif length > 64:
            print("Password must not exceed 64 characters.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")

# Generate password using secrets.choice()
password = ''.join(secrets.choice(characters) for _ in range(length))

print("\nGenerated Secure Password:")
print(password)
