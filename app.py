from tkinter import *
from tkinter import messagebox

# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title("Campus Placement Preparation App")
root.geometry("600x500")

score = 0

# ---------------- HOME SCREEN ----------------
def home():
    clear()
    Label(root, text="Campus Placement App", font=("Arial", 18, "bold")).pack(pady=20)

    Button(root, text="Aptitude", width=20, command=aptitude).pack(pady=10)
    Button(root, text="Interview Q&A", width=20, command=interview).pack(pady=10)
    Button(root, text="Notes", width=20, command=notes).pack(pady=10)
    Button(root, text="Quiz", width=20, command=quiz).pack(pady=10)

# ---------------- CLEAR SCREEN ----------------
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# ---------------- APTITUDE ----------------
def aptitude():
    clear()
    Label(root, text="Aptitude Questions", font=("Arial", 16, "bold")).pack()

    q1 = "What is 10% of 200?"
    Label(root, text=q1).pack()
    ans1 = Entry(root)
    ans1.pack()

    def check():
        if ans1.get() == "20":
            messagebox.showinfo("Result", "Correct Answer")
        else:
            messagebox.showerror("Result", "Wrong Answer")

    Button(root, text="Submit", command=check).pack(pady=10)
    Button(root, text="Back", command=home).pack()

# ---------------- INTERVIEW ----------------
def interview():
    clear()
    Label(root, text="Interview Questions", font=("Arial", 16, "bold")).pack()

    questions = [
        "Tell me about yourself",
        "What are your strengths?",
        "What is OOP?",
        "Why should we hire you?"
    ]

    for q in questions:
        Label(root, text="• " + q, anchor="w").pack()

    Button(root, text="Back", command=home).pack(pady=10)

# ---------------- NOTES ----------------
def notes():
    clear()
    Label(root, text="Notes Section", font=("Arial", 16, "bold")).pack()

    text = Text(root, height=15, width=60)
    text.pack()

    sample = """
C Programming Notes:
- Variables and Data Types
- Loops (for, while)
- Functions
- Arrays
- Pointers

DBMS Notes:
- SQL Commands
- Keys (Primary, Foreign)
- Normalization
"""
    text.insert(END, sample)

    Button(root, text="Back", command=home).pack()

# ---------------- QUIZ ----------------
def quiz():
    clear()
    global score
    score = 0

    Label(root, text="Quiz Section", font=("Arial", 16, "bold")).pack()

    q = Label(root, text="1. What is 2 + 2?")
    q.pack()
    ans = Entry(root)
    ans.pack()

    def submit():
        global score
        if ans.get() == "4":
            score += 1

        messagebox.showinfo("Score", f"Your Score: {score}/1")
        home()

    Button(root, text="Submit Quiz", command=submit).pack(pady=10)

    Button(root, text="Back", command=home).pack()

# ---------------- START APP ----------------
home()
root.mainloop()
