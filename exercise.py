# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()



# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    while True:
        letter = input('Enter a letter (a-z or A-Z), or type "quit": ')
        print(f'The user entered {letter}')

        if letter == 'quit':
            print('Till next time, byebye!')
            break
        elif letter in 'aeiouAEIOU':
            print(f'The letter {letter} is a vowel')        
        else: print(f'The letter {letter} is a consonant')

# Call the function
# check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    while True:
        try:
            age = int(input('Please enter your age: '))
            print(f'You have entered {age} as your age')

            if age < 0:
                print('This is an invalid age. Please enter a valid age')            
            elif age >= 18:
                print('You are eligible to vote')
                break
            else: 
                print('You have not meet the required age to vote')
                break
        except ValueError:
            print('Invalid input. Please enter numbers only.')


# Call the function
# check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    while True:
        try:
            dogAge = int(input("Input a dog's age: "))
            print(f'You have input dog\'s age as {dogAge}')

            if dogAge < 0:
                print('Invalid age')
            elif 3 > dogAge >= 0:
                first2years = dogAge * 10
                print(f"The dog's age in dog years is {first2years}")
                break
            else:
                after2years = ((dogAge - 2) * 7) + (2 * 10)
                print(f"The dog's age in dog years is {after2years}")
                break
                

        except ValueError:
            print('Invalid input. Please enter numbers only')

# Call the function
# calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    while True:
        
            temperature = input('Is it cold (yes/no): ').strip().lower()
            print(f'You answered {temperature}')
            raining = input('Is it raining? (yes/no): ').strip().lower()
            print(f'You answered {raining}')

            if temperature not in ['yes', 'no'] or raining not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no' only.")
                
            elif temperature == 'yes' and raining == 'yes':
                print('Wear a waterproof coat.')
                break
            elif temperature == 'yes' and raining == 'no':
                print('Wear a warm coat.')
                break
            elif temperature == 'no' and raining == 'yes':
                print('Carry an umbrella.')
                break
            else:
                print('Wear light clothing')
                break
      
           
# Call the function
# weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    while True:
        month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
        print(f'You have entered the month {month}')
        day = int(input("Enter the day of the month: "))
        print(f'You have entered the day {day}')

        if month not in ['Dec', 'Jan', 'Feb', 'Mar','Apr', 'May', 'Jun','Jul', 'Aug', 'Sep','Oct', 'Nov',]:
            print('You have entered an invalid month. Please key in month in <mmm> format')
            continue
        if day >= 32:
            print('You have entered an invalid day. Please key in day in <dd> format')
            continue
        if month == 'Feb' and day > 29:
            print(f'You have entered an invalid day for the month {month}. Please key in a value of 1-29 days only')
            continue

        if month in ['Dec', 'Jan', 'Feb', 'Mar']:
            if month == 'Dec' and day < 21:
                season = 'Fall'
              
            elif month == 'Mar' and day > 19:
                season = 'Spring'
                
            else:
                season = 'Winter'
               
        elif month in ['Apr', 'May', 'Jun']:
            if month == 'Jun' and day > 21:
                season = 'Summer'
                
            else:
                season = 'Spring'
                
        elif month in ['Jul', 'Aug', 'Sep']:
            if month == 'Sep' and day >= 22:
                season = 'Fall'
                
            else: 
                season = 'Summer'
                
        elif month in ['Oct', 'Nov',]:
                season = 'Fall'
                
         
        print(f'{month} {day:02d} is in {season}.')
        break


# Call the function
# determine_season()



# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    answer = 42
    
    while True:
        try:
            guess = int(input('I am thinking of a number between 1 to 100. You have 5 tries. Make a guess!: '))

            if guess > 100:
                print("Invalid input. Please key a number between 1-100 only")
                continue

            for x in range(6):
            
                if x == 1 and guess == answer:
                    print(f'Wow, your guess of {guess}, is spot on. Are you a mind-reader?')
                    break
                elif x == 1 and guess != answer:                  
                    if guess < answer:
                        guess = int(input(f'Hint: Your guess of of {guess} is too low! 4 more tries!: '))
                        
                    else:
                        guess = int(input(f'Hint: Your guess of of {guess} is too high! 4 more tries!: '))
                        
                elif x == 2 and guess != answer:
                    if guess < answer:
                        guess = int(input(f'Hint: Your guess of of {guess} is too low! 3 more tries!: '))
                        
                    else:
                        guess = int(input(f'Hint: Your guess of of {guess} is too low! 3 more tries!: '))
                        
                elif x == 3 and guess != answer:
                    if guess < answer:
                        guess = int(input(f'Hint: Your guess of of {guess} is too low! 2 more tries!: '))
                    else:
                        guess = int(input(f'Hint: Your guess of of {guess} is too low! 2 more tries!: '))

                elif x == 4 and guess != answer:
                    if guess < answer:
                        guess = int(input(f'Hint: Your guess of of {guess} is too low! Last chance!: '))
                    else:
                        guess = int(input(f'Hint: Your guess of of {guess} is too high! Last chance!: '))
                elif x == 5 and guess != answer:
                    print("Sorry, you failed to guess the number in five attempts.")
                    return
                elif guess == answer:
                    print(f'Congratulations, your guess of {guess}, is correct')
                    return

        except ValueError:
                print("Invalid input. Please key a number between 1-100 only")
                continue
 


# Call the function
guess_number()