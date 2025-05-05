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