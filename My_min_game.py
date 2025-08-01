import random

number_true = random.randint(1, 100) # Генерація випадкового числа від 1 до 100

print("Guess a number from 1 to 100. You have 10 attempts.!")

# Кількість спроб
amount = 0
max_amount = 10

while amount < max_amount:
    try:
        enter = int(input(f"Attempt {amount + 1}: Enter number:"))
    except ValueError:
        print("Please enter a whole number.!")
        continue

    amount += 1

    if enter < number_true:
        print("Number is more!")
    elif enter > number_true:
        print("Number is smaller!")
    else:
        print(f"Congratulations! You guessed the number. {number_true} with {amount} attempts!")
        break
else:
    print(f"The attempts are over. The number you guessed was: {number_true}")