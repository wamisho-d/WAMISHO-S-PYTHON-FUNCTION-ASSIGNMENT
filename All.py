# Question 1 Task 1: Create functions for each arithmetic operation.
def add(x,y): 
 return x + y

def subtract(x,y): 
 return x - y

def multiply(x,y): 
 return x * y

def divide(x,y): 
 return x / y
 if y == 0:
  return Error 
 else: x/y

# Question 1 Task 2: Implement user input to receive numbers and an operation choice.
 def user_input():
  num = int(input("Enter the first number"))
  num = int(input("Enter the second number"))
  operation = input("choice an operation (+,-,*,/)")
  return num1, num2, operation  
  
  ValueError
 print("invalid input. Enter numeric values" )
 return user_input

# Question 1 Task 3: Ensure your program can handle division by zero and other potential errors.
 
 def calculator():
  num1, num2, operation = user_input()
 if operation == "+":
   print(f" the result is: {add(num1,num2)}")

 elif operation == "-":
   print(f" the result is: {subtract(num1,num2)}")

 elif operation == "*":
   print(f" the result is: {multiply(num1,num2)}")

 elif operation == "/":
   if result == error:
    print(result)
   else:
    (f"the result is: {result}")
 else:
  print("invalid operation. choice an operation (+,-,*,/)")

# Question 2 Task 1: Write a function that lets the user add items to a list.
  def add_items(shopping_list):
   items = input("Enter items to shopping list to add:")
   shopping_list.append(items)
   print(f"{items} have been added to shopping list.")

   # Question 2 Task 2: Include a feature to remove items from the list.
   def remove_items(shopping_list):
    items = input("Enter items to shopping list to remove:")
    if items in shopping_list:
     shopping_list.remove(items)
     print(f"{items} have been removed to shopping list.")
    else:
     print(f"(items) are not in shopping list.")
 # Question 2 Task 3: Add a function that prints out the entire list in a formatted way.
     def print_list(shopping_list):
      print("\nShopping_list:")
      for items in shopping_list:
       print(f"-{items}")
def main():
    shopping_list = []
    while True:
        print("\nOptions:")
        print("1. Add items")
        print("2. Remove items")
        print("3. Show list")
        print("4. Exit")
  
        choice = input("Enter your choice(1-4):")
        if choice == "1":
          print("add_items")
        elif choice == "2":
         print("remove items")
        elif choice == "3":
          print("show list")
        elif choice == "4":
          print("exiting the program")
          break
        else:
          print("invalid choice. Enter a number between 1 and 4.")

# Question 3 Task 1: Code a function to calculate the average grade.
def calculate_average(grades):
  if not grades:
    return 0
  return sum(grades)/len(grades)
# Question 3 Task 2: Implement a function to find the highest and lowest grade.
def find_highest_lowest(grades):
  if not grades:
    return None, None
  highest = max(grades)
  lowest = min(grades)
  return highest, lowest
  
# Question 3 Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

def categorize_grades(grades):
  letter_grades = []
  for grade in grades:
     if grades >= 95:
      letter_grades.append("A")
     elif grades >= 85:
      letter_grades.append("B")
     elif grades >= 75:
      letter_grades.append("C")
     elif grades >= 65:
      letter_grades.append("D")
     else:
      letter_grades.append("F")
  return letter_grades

# Question 4 Task 1: Develop a list of questions and answers.
questions = [
    {"question": "What is the capital of United States?", "answer": "Washington D.C."},
    {"question": "What is the derivative of f(x) = 8x^5 + 3x^18?","answer":"40x^4 + 54x^17"},
    {"question": "where are you from?", "answer": "England"}
]
  

# Question 4 Task 2: Write a function that quizzes the user and takes their answers.

def quiz_user(questions):
 user_answers = []
 for question in questions:
    user_answer = input(question(questions) + " ")
    user_answer.append(user_answer)
    return user_answer

# Question 4 Task 3: Score the quiz and give the user feedback on their performance.

def Score_quiz(quiz_data, user_answers):
 score = 0
 for questions, right_answers in quiz_data.items():
   if user_answers.get(questions, "").stripe().lower() == right_answers.lower():
    score += 1
   return score
 
 def give_the_user_feedback(score, total_questions):
    print(f"you scored {score} out of {total_questions}.")
    percentage = (score/total_questions)*100 
    if percentage == 100:
       print(" you got all answers right")
    elif percentage >= 65:
       print("you passed")
    else:
       print("you failed")

   # Question 5 Task 1: Develop a function to log different fitness activities and their duration. 
def log_different_fitness_activities(activities, durations):
    log_different_fitness_activities = {}
    for activity, duration in zip(activities, durations):
     log_different_fitness_activities[activity] = duration
    return log_different_fitness_activities

# Question 5 Task 2: Write a simple function that estimates calories burned based on the activity and duration.
def calculate_calories_burnned(log_different_fitness_activities):
    total_calories_burnned = 0
    for duration in log_different_fitness_activities.values():
     total_calories_burnned += duration*3.5
    return total_calories_burnned

# Question 5 Task 3:Create a summary function that provides a report of all activities and total calories burned for the day.

def summary_report(log_different_fitness_activities):
    print("Activity Summary for the Day:")
    for activity, duration in log_different_fitness_activities.items():
        print(f"{activity}: {duration} minutes")
        total_calories = calculate_calories_burnned(log_different_fitness_activities)
    print(f"Total calories burned: {total_calories}")


   






  
