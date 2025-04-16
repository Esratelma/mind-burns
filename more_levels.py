import tkinter as tk
from tkinter import messagebox
import webbrowser  # For opening a URL
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Track highest unlocked level and score
highest_unlocked_level = 1
score = 0
buttons = {}  # Stores level buttons

def show_question(level):
    question_window = tk.Toplevel()
    question_window.title(f"Level {level} - Question")
    question_window.geometry("500x450")
    question_window.config(bg="#015482")

    # Update question for Level 2
    if level == 2:
        question = tk.Label(question_window, text="৪. যদি P→=2i^+4j^−5k^ এবং Q→=i^+2j^+3k^ হয় তবে এদের মধ্যবর্তী কোণ নির্ণয় কর।", font=("Helvetica", 16), bg="#FAF9F6")
        question.pack(pady=20)
    else:
        question = tk.Label(question_window, text=" দুই সমমানেরে ভেক্টর একটি বিন্দুতে ক্রিয়াশীল। এদের লব্ধির মান যে কোন একটি ভেক্টরের মানের সমান হলে মধ্যবর্তী কোণ কত?", font=("Helvetica", 16), bg="#FAF9F6")
        question.pack(pady=20)

    # Score display
    score_label = tk.Label(question_window, text=f"Score: {score}", font=("Helvetica", 12, "bold"), bg="#FAF9F6")
    score_label.pack()

    # Updated options for Level 2
    if level == 2:
        options = [("78.51°", False), ("105.25°", False), ("11.49°", False), ("101.49°", True)]
    else:
        options = [("0°", False), ("45°", False), ("90°", False), ("120°", True)]
    
    option_buttons = []

    def check_answer(is_correct):
        global highest_unlocked_level, score
        if is_correct:
            messagebox.showinfo("Correct", "Correct Answer! Level Unlocked.")
            if level == highest_unlocked_level and level < 25:
                highest_unlocked_level += 1
            score += 1
            update_buttons()
            question_window.destroy()
        else:
            messagebox.showerror("Incorrect", "Wrong Answer. Try again.")
            question_window.destroy()

    def show_demo():
        if level == 2:
            # Instead of showing the demo, open a link
            webbrowser.open("https://phet.colorado.edu/sims/html/energy-skate-park/latest/energy-skate-park_all.html")  # Replace with your demo link
        else:
            # Vector Animation for other levels
            A = 1
            B = 1
            theta_deg = 120
            theta_rad = np.radians(theta_deg)

            A_vector = np.array([A, 0])
            B_vector = np.array([B * np.cos(theta_rad), B * np.sin(theta_rad)])
            R_vector = A_vector + B_vector

            # Set up the plot
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.set_xlim(-1.5, 2)
            ax.set_ylim(-1.5, 1.5)
            ax.set_aspect('equal')
            ax.grid(True)
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.set_title("Vector Addition Animation (120° between vectors)")

            # Create vector lines
            vec_a = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='r', label='Vector A')
            vec_b = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='b', label='Vector B')
            vec_r = ax.quiver(0, 0, 0, 0, angles='xy', scale_units='xy', scale=1, color='g', label='Resultant R')
            ax.legend()

            # Animation function
            def update(frame):
                if frame < 20:
                    # Draw A_vector gradually
                    vec_a.set_UVC(A_vector[0] * frame / 20, A_vector[1] * frame / 20)
                elif frame < 40:
                    # Draw B_vector gradually
                    vec_b.set_UVC(B_vector[0] * (frame - 20) / 20, B_vector[1] * (frame - 20) / 20)
                else:
                    # Draw resultant vector
                    vec_r.set_UVC(R_vector[0] * (frame - 40) / 20, R_vector[1] * (frame - 40) / 20)

            # Run animation
            ani = FuncAnimation(fig, update, frames=60, interval=100)

            plt.show()

    # Create option buttons and store in list
    for option_text, is_correct in options:
        btn = tk.Button(question_window, text=option_text, font=("Arial", 14),
                        width=15, command=lambda correct=is_correct: check_answer(correct))
        btn.pack(pady=5)
        option_buttons.append(btn)

    # Demo button
    demo_button = tk.Button(question_window, text="Show Demo", font=("Helvetica", 12, "bold"),
                           bg="#007fb3", bd=10, relief="groove", command=show_demo)
    demo_button.pack(pady=10)

    # Back button
    back_button = tk.Button(question_window, text="Back", font=("Helvetica", 12),
                            command=question_window.destroy, bg="#007fb3", relief="groove")
    back_button.pack(pady=10)

def on_level_click(level):
    if level > highest_unlocked_level:
        messagebox.showwarning("Locked", f"Level {level} is locked. Complete previous levels to unlock.")
    else:
        show_question(level)

def update_buttons():
    for level, btn in buttons.items():
        if level <= highest_unlocked_level:
            btn.config(state=tk.NORMAL, bg="#007bf3", fg="white")
        else:
            btn.config(state=tk.DISABLED, bg="gray")

def create_level_selection():
    global buttons
    window = tk.Tk()
    window.title("Level Selection")
    window.geometry("600x500")
    window.config(bg="#015482")

    title = tk.Label(window, text="Select a Level", font=("Helvetica", 20, "bold"), bg="#015482", fg="white")
    title.pack(pady=20)

    level_frame = tk.Frame(window, bg="#015482")
    level_frame.pack(pady=10)

    total_levels = 25
    columns = 5

    for level in range(1, total_levels + 1):
        btn = tk.Button(level_frame, text=str(level), width=8, height=3,
                        command=lambda lvl=level: on_level_click(lvl),
                        font=("Helvetica", 12))
        row = (level - 1) // columns
        col = (level - 1) % columns
        btn.grid(row=row, column=col, padx=10, pady=10)
        buttons[level] = btn

    update_buttons()
    window.mainloop()

create_level_selection()
