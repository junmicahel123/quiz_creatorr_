###
#START

#LOAD questions from 'quiz_creator_data_.txt'
#PARSE each block into:
#    - question text
 #   - 4 choices
  #  - correct answer (a–d)

#WHILE questions remain:
 #   SELECT a random question
  #  REMOVE it from the pool
   ##WAIT for user's answer

   # IF answer is correct:
    #    SHOW "Correct!"
 #   ELSE:
#        SHOW "Incorrect!" and the correct answer

#HOW "All questions answered" when done

import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")
root.configure(bg="#ecf0f1")

question_pool = ()
current_question = {}

question_label = tk.Label(root, text="", wraplength=450, font=("Arial", 14, "bold"), bg="#34495e", fg="white", pady=10)
question_label.pack(fill="x", padx=10, pady=20)

choice_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=40, command=lambda idx=i: check_answer(idx), bg="#3498db", fg="white", cursor="hand2")
    btn.pack(pady=5)
    choice_buttons.append(btn)


if question_pool:
    ()
else:
    messagebox.showwarning("Empty", "No questions available in the file.")
    root.destroy()

root.mainloop()