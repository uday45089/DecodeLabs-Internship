score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().casefold()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. Which planet is known as the Red Planet? ").strip().casefold()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer = input("\n3. What is the largest ocean on Earth? ").strip().casefold()

if answer == "pacific ocean" or answer == "pacific":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Pacific Ocean.")

print("\nQuiz Completed!")
print(f"Your final score is {score}/3.")
