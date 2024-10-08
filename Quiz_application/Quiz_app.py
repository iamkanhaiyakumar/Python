import random
import sys

# Sample question pool (expand to 20 as needed)
questions = {
    "Python": [
        {"question": "What is the output of: print(2 ** 3)?", "choices": ["6", "9", "8"], "answer": 3},
        {"question": "What is the correct file extension for Python files?", "choices": [".pt", ".pyt", ".py"], "answer": 3},
        {"question": "Which function is used to get the length of a list?", "choices": ["size()", "len()", "count()"], "answer": 2},
        {"question": "Which of the following is immutable in Python?", "choices": ["List", "Dictionary", "Tuple"], "answer": 3},
        {"question": "How do you create a dictionary?", "choices": ["{}", "[]", "()"], "answer": 1},
        {"question": "Which of the following is used to define a function in Python?", "choices": ["function", "def", "lambda"], "answer": 1},
        {"question": "Which data type is mutable in Python?", "choices": ["Tuple", "List", "String"], "answer": 1},
        {"question": "What is the output of 'print(type(10))' in Python?", "choices": ["int", "float", "str"], "answer": 0},
        {"question": "How do you start a loop in Python?", "choices": ["for", "while", "loop"], "answer": 0},
    ],
    "DSA": [
        {"question": "What is the time complexity of binary search?", "choices": ["O(log n)", "O(n)", "O(n^2)"], "answer": 1},
        {"question": "Which data structure works on FIFO?", "choices": ["Stack", "Queue", "Tree"], "answer": 2},
        {"question": "Which is the best sorting algorithm in terms of time complexity?", "choices": ["Merge Sort", "Bubble Sort", "Selection Sort"], "answer": 1},
        {"question": "What is the worst-case time complexity of Quick Sort?", "choices": ["O(n log n)", "O(n^2)", "O(n)"], "answer": 2},
        {"question": "Which of the following uses a graph?", "choices": ["HashMap", "Binary Tree", "DFS"], "answer": 3},
    ],
    "C++": [
        {"question": "Which of the following is a correct variable declaration in C++?", "choices": ["int num;", "num int;", "int: num"], "answer": 1},
        {"question": "What is the size of an integer in C++?", "choices": ["2 bytes", "4 bytes", "8 bytes"], "answer": 2},
        {"question": "Which operator is used to access a member of a structure?", "choices": [".", "->", ":"], "answer": 1},
        {"question": "What is a default return type of a function?", "choices": ["void", "int", "float"], "answer": 2},
        {"question": "Which feature of OOP makes sure the private data can only be accessed through a function?", "choices": ["Abstraction", "Encapsulation", "Polymorphism"], "answer": 2},
    ],
    "Java": [
        {"question": "Which keyword is used to inherit a class in Java?", "choices": ["implements", "extends", "inherits"], "answer": 2},
        {"question": "Which method is used to start a thread in Java?", "choices": ["run()", "execute()", "start()"], "answer": 3},
        {"question": "What is the default value of an int variable?", "choices": ["null", "0", "undefined"], "answer": 2},
        {"question": "Which collection type does not allow duplicate elements?", "choices": ["List", "Set", "Map"], "answer": 2},
        {"question": "Which keyword is used to inherit a class in Java?", "choices": ["implements", "extends", "inherits"], "answer": 2},
        {"question": "Which method is used to start a thread in Java?", "choices": ["run()", "execute()", "start()"], "answer": 3},
        {"question": "Which of the following is not a feature of Java?", "choices": ["Object-Oriented", "Platform Dependent", "Secure"], "answer": 2},
    ]
}

# User data storage (in-memory)
users = {}

# Registration function
def register():
    print("===== Registration =====")
    username = input("Enter username: ")
    if username in users:
        print("Username already exists. Please login or choose a different username.")
        return register()
    password = input("Enter password: ")
    users[username] = password
    print("Registration successful!")

# Login function
def login():
    print("===== Login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if users.get(username) == password:
        print("Login successful!")
        start_quiz()
    else:
        print("Invalid username or password. Try again.")
        return login()

# Quiz function
def start_quiz():
    print("\n===== Welcome to the Quiz =====")
    
    # Select 5 random questions from the combined pool of questions
    all_questions = []
    for subject, subject_questions in questions.items():
        all_questions.extend(subject_questions)

    selected_questions = random.sample(all_questions, 5)

    # Start the quiz
    score = 0
    for i, q in enumerate(selected_questions):
        print(f"\nQ{i + 1}: {q['question']}")
        for idx, choice in enumerate(q['choices'], 1):
            print(f"{idx}. {choice}")
        
        answer = int(input("Your choice (1/2/3): "))
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['choices'][q['answer'] - 1]}")
    
    print(f"\nYour total score: {score}/5")
    exit_or_restart()

# Exit or Restart function
def exit_or_restart():
    choice = input("\nEnter 'exit' to quit or 'restart' to attempt the quiz again: ").lower()
    if choice == 'exit':
        print("Thank you for participating! Goodbye!")
        sys.exit()
    elif choice == 'restart':
        start_quiz()
    else:
        print("Invalid choice, exiting the program.")
        sys.exit()

# Main Program Loop
def main():
    while True:
        print("\n===== Welcome to the Quiz App =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
