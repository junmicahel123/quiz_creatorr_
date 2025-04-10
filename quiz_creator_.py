# pseudocode
# use def for questionare
    # use while loop for first loop
        # ask for user input
        # ask for question
        # ask for choices
        # ask for the correct answer
# use def to save the data into file
    # use with openn
    #

import tkinter as tk
from tkinter import messagebox

def questionare():
    number_of_items = 0
    questions = []
    while True:
        question = str(input("Please enter a question::  "))
        choices = []
        for i in range(4):
            choice = str(input(f"Enter the choices for {chr(97 + i)}::"))
        
            choices.append(choice)
        correct_answer = input("What is the correct answer? (A, B, C,)").strip().lower()

        questions.append({
            'Question': question,
            'Choices': choices,
            'Correct Answer': correct_answer 
        })
        number_of_items += 1
        continueum = input("Do you want to add another question?: (y/n)").strip().lower()
        if continueum == 'n':
            break
    
    save_questions_(questions)


def save_questions_(questions):
    with open('quiz_creator_data_.txt', 'w') as file:
        for i, q in enumerate(questions, 1):
            file.write(f"Question {i}: {q['Question']}\n")
            file.write(f"   a) {q['Choices'][0]}\n")
            file.write(f"   b) {q['Choices'][1]}\n")
            file.write(f"   c) {q['Choices'][2]}\n")
            file.write(f"   d) {q['Choices'][3]}\n")
            file.write(f"Correct Answer: {q['Correct Answer']}\n\n")
    print("Questions saved to quiz_creator_data_.txt")

questionare()


root = tk.Tk()
root.title("Quiz Question Creator")
root.geometry("450x500")
root.configure(bg="#f0f4f7")


header = tk.Label(root, text="QUIZ QUESTION CREATOR", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white", pady=10)
header.pack(fill="x")

main_frame = tk.Frame(root, bg="#f0f4f7", padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

tk.Label(main_frame, text="Enter your question:", font=("Arial", 11), bg="#f0f4f7").pack(anchor="w")
question_entry = tk.Entry(main_frame, width=50, font=("Arial", 10))
question_entry.pack(pady=5)

            
