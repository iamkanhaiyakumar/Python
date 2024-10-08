# '''
# Name: Kanhaiya Kumar
# Enrollment Number: 0176AL221064
# Class Roll Number: 62
# LNCTE - CSE AIML 5th Semester, Section - A
# '''
# import random
# import json

# # Updated questions for Python, DSA, C++, and Java
# QUESTIONS = [
#     # Python Questions
#     {"question": "Which of the following is used to define a function in Python?", "choices": ["function", "def", "lambda"], "answer": 1},
#     {"question": "Which data type is mutable in Python?", "choices": ["Tuple", "List", "String"], "answer": 1},
#     {"question": "What is the output of 'print(type(10))' in Python?", "choices": ["int", "float", "str"], "answer": 0},
#     {"question": "How do you start a loop in Python?", "choices": ["for", "while", "loop"], "answer": 0},

#     # DSA Questions
#     {"question": "Which data structure is used for LIFO operations?", "choices": ["Queue", "Stack", "Array"], "answer": 1},
#     {"question": "Which algorithm is used to sort an array in O(n log n) time?", "choices": ["Bubble Sort", "Quick Sort", "Merge Sort"], "answer": 2},
#     {"question": "What is the worst-case time complexity of Binary Search?", "choices": ["O(n)", "O(log n)", "O(n^2)"], "answer": 1},
#     {"question": "Which data structure is used for BFS traversal?", "choices": ["Stack", "Queue", "Tree"], "answer": 1},

#     # C++ Questions
#     {"question": "Which of the following is the correct syntax to declare a pointer in C++?", "choices": ["int ptr*", "int* ptr", "int ptr&"], "answer": 1},
#     {"question": "Which feature in C++ allows the reusability of code?", "choices": ["Encapsulation", "Polymorphism", "Inheritance"], "answer": 2},
#     {"question": "What is the output of the following C++ code: 'cout << 2 + 2;'?", "choices": ["22", "4", "Error"], "answer": 1},
#     {"question": "Which operator is used to access a member function of a class in C++?", "choices": ["->", ".", "::"], "answer": 1},

#     # Java Questions
#     {"question": "Which method is used to start a thread in Java?", "choices": ["start()", "run()", "execute()"], "answer": 0},
#     {"question": "What is the size of an int variable in Java?", "choices": ["2 bytes", "4 bytes", "8 bytes"], "answer": 1},
#     {"question": "Which of the following is not a primitive type in Java?", "choices": ["int", "float", "String"], "answer": 2},
#     {"question": "Which of these keywords is used to inherit a class in Java?", "choices": ["super", "this", "extends"], "answer": 2},
    
#     # More Python/DSA/C++/Java questions can be added here (up to 20)
# ]

# # File to store user data
# USER_FILE = "users.json"

# # Helper functions to manage user registration and login
# def load_users():
#     try:
#         with open(USER_FILE, "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

# def save_users(users):
#     with open(USER_FILE, "w") as file:
#         json.dump(users, file)

# def register_user():
#     users = load_users()
#     username = input("Enter username: ")
#     if username in users:
#         print("Username already exists. Try again.")
#         return
#     password = input("Enter password: ")
#     users[username] = password
#     save_users(users)
#     print("Registration successful! Please login.")

# def login_user():
#     users = load_users()
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username in users and users[username] == password:
#         print(f"Welcome back, {username}!")
#         return True
#     else:
#         print("Invalid username or password. Please try again.")
#         return False

# # Function to conduct the quiz
# def attempt_quiz():
#     score = 0
#     random_questions = random.sample(QUESTIONS, 5)  # Select 5 random questions from the list
#     for i, q in enumerate(random_questions):
#         print(f"\nQ{i+1}: {q['question']}")
#         for idx, choice in enumerate(q['choices']):
#             print(f"{idx + 1}. {choice}")
#         answer = int(input("Choose the correct option (1/2/3): ")) - 1
#         if answer == q['answer']:
#             score += 1
#             print("Correct!")
#         else:
#             print("Wrong answer!")
#     print(f"\nYou scored {score} out of 5!")

# # Main function to run the quiz application
# def main():
#     while True:
#         print("\n--- QUIZ APPLICATION ---")
#         print("1. Register")
#         print("2. Login")
#         print("3. Attempt Quiz")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             register_user()
#         elif choice == "2":
#             if login_user():
#                 print("Login successful!")
#         elif choice == "3":
#             attempt_quiz()
#         elif choice == "4":
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

















# import random
# import sys

# # Sample questions for different subjects
# questions = {
#     "Python": [
#         {"question": "What is the output of: print(2 ** 3)?", "choices": ["6", "9", "8"], "answer": 3},
#         {"question": "What is the correct file extension for Python files?", "choices": [".pt", ".pyt", ".py"], "answer": 3},
#     ],
#     "DSA": [
#         {"question": "What is the time complexity of binary search?", "choices": ["O(log n)", "O(n)", "O(n^2)"], "answer": 1},
#         {"question": "Which data structure works on FIFO?", "choices": ["Stack", "Queue", "Tree"], "answer": 2},
#     ],
#     "C++": [
#         {"question": "Which of the following is a correct variable declaration in C++?", "choices": ["int num;", "num int;", "int: num"], "answer": 1},
#         {"question": "What is the size of an integer in C++?", "choices": ["2 bytes", "4 bytes", "8 bytes"], "answer": 2},
#     ],
#     "Java": [
#         {"question": "Which keyword is used to inherit a class in Java?", "choices": ["implements", "extends", "inherits"], "answer": 2},
#         {"question": "Which method is used to start a thread in Java?", "choices": ["run()", "execute()", "start()"], "answer": 3},
#     ]
# }

# # Store users for registration and login (in-memory dictionary)
# users = {}

# # Supportive quotes after wrong answers
# quotes = [
#     "Keep going, success is built on failures!",
#     "Mistakes are proof that you are trying!",
#     "Don’t worry, each wrong answer is a step closer to the right one!",
#     "Failure is the opportunity to begin again more intelligently!"
# ]

# # Registration function
# def register():
#     print("===== Registration =====")
#     username = input("Enter username: ")
#     if username in users:
#         print("Username already exists. Please login or choose a different username.")
#         return register()
#     password = input("Enter password: ")
#     users[username] = password
#     print("Registration successful!")

# # Login function
# def login():
#     print("===== Login =====")
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if users.get(username) == password:
#         print("Login successful!")
#         start_quiz()
#     else:
#         print("Invalid username or password. Try again.")
#         return login()

# # Quiz function
# def start_quiz():
#     print("\n===== Welcome to the Quiz =====")
    
#     subject_pool = ["Python", "DSA", "C++", "Java"]
#     selected_questions = []

#     # Randomly pick 5 questions from the pool of 20
#     while len(selected_questions) < 5:
#         subject = random.choice(subject_pool)
#         question = random.choice(questions[subject])
#         if question not in selected_questions:
#             selected_questions.append(question)
    
#     # Start quiz
#     score = 0
#     for i, q in enumerate(selected_questions):
#         print(f"\nQ{i + 1}: {q['question']}")
#         for idx, choice in enumerate(q['choices'], 1):
#             print(f"{idx}. {choice}")
        
#         answer = int(input("Your choice (1/2/3): "))
#         if answer == q['answer']:
#             print("Correct!")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is {q['choices'][q['answer'] - 1]}")
#             print(random.choice(quotes))  # Display random motivational quote
    
#     print(f"\nYour total score: {score}/5")
#     exit_or_restart()

# # Exit or Restart function
# def exit_or_restart():
#     choice = input("\nEnter 'exit' to quit or 'restart' to attempt the quiz again: ").lower()
#     if choice == 'exit':
#         print("Thank you for participating! Goodbye!")
#         sys.exit()
#     elif choice == 'restart':
#         start_quiz()
#     else:
#         print("Invalid choice, exiting the program.")
#         sys.exit()

# # Main Program Loop
# def main():
#     while True:
#         print("\n===== Welcome to the Quiz App =====")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Select an option (1/2/3): ")
        
#         if choice == '1':
#             register()
#         elif choice == '2':
#             login()
#         elif choice == '3':
#             print("Exiting...")
#             sys.exit()
#         else:
#             print("Invalid option, please try again.")

# if __name__ == "__main__":
#     main()
