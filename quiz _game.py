import random
import tkinter as tk

questions = [
    {
        "question": "What is the capital of India?",
        "choices": ["A) Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
        "answer": "A"
    },
    {
        "question": "What is the largest animal in the world?",
        "choices": ["A) Elephant", "B) Whale", "C) Giraffe", "D) Dinosaur"],
        "answer": "B"
    },
    {
        "question": "Who is the author of Harry Potter series?",
        "choices": ["A) J.R.R. Tolkien", "B) George R.R. Martin", "C) J.K. Rowling", "D) C.S. Lewis"],
        "answer": "C"
    },
    {
        "question": "What is the name of the largest bone in the human body?",
        "choices": ["A) Humerus", "B) Femur", "C) Tibia", "D) Fibula"],
        "answer": "B"
    },
    {
        "question": "What is the name of the smallest planet in the solar system?",
        "choices": ["A) Mercury", "B) Venus", "C) Mars", "D) Pluto"],
        "answer": "A"
    }
]

random.shuffle(questions)

window = tk.Tk()
window.title("Quiz Game")
window.geometry("400x300")

frame = tk.Frame(window)
frame.pack()

question_label = tk.Label(frame, text=questions[0]["question"], wraplength=300)
question_label.pack()

user_answer = tk.StringVar()

radio_buttons = []
for i in range(4):
    radio_button = tk.Radiobutton(frame, text=questions[0]["choices"][i], variable=user_answer, value=questions[0]["choices"][i][0])
    radio_button.pack()
    radio_buttons.append(radio_button)

feedback_label = tk.Label(frame, text="")
feedback_label.pack()

score = 0
index = 0

def check_answer():
    global score, index, questions
    answer = user_answer.get()

    if answer == questions[index]["answer"]:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect! The correct answer is {questions[index]['answer']}", fg="red")
    for radio_button in radio_buttons:
        radio_button.config(state=tk.DISABLED)
    next_button.config(state=tk.NORMAL)

def next_question():
    global score, index, questions
    index += 1
    if index < len(questions):
        question_label.config(text=questions[index]["question"])
        for i in range(4):
            radio_buttons[i].config(text=questions[index]["choices"][i], value=questions[index]["choices"][i][0])
        user_answer.set("")
        feedback_label.config(text="")
        for radio_button in radio_buttons:
            radio_button.config(state=tk.NORMAL)
        next_button.config(state=tk.DISABLED)
    else:
        percentage = score / len(questions) * 100
        question_label.config(text=f"You have completed the quiz!\nYour score is {score} out of {len(questions)}.")
        if percentage >= 80:
            feedback_label.config(text="Excellent!", fg="green")
        elif percentage >= 50:
            feedback_label.config(text="Good!", fg="Blue")
        else:
            feedback_label.config(text="Try again!", fg="red")
        for radio_button in radio_buttons:
            radio_button.config(state=tk.DISABLED)
        next_button.config(state=tk.DISABLED)

next_button = tk.Button(frame, text="Next", command=next_question, state=tk.DISABLED)
next_button.pack()

check_button = tk.Button(frame, text="Check", command=check_answer)
check_button.pack()

next_question()

window.mainloop()