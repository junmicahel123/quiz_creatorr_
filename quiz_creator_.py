# pseudocode
# use def for questionare
    # use while loop for first loop
        # ask for user input
        # ask for question
        # ask for choices
        # ask for the correct answer
# use def to save the data into file
    # use file.write function to store
    #


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
    file = open('quiz_creator_data_.txt', 'w')
    entry = str(questions)
    file.write(entry)
    file.close()


questionare()
            
