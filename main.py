import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

# Initialize player data dictionary
player_data = {"name": "", "avatar": ""}

def set_crystal_background_and_center(window):
    window.configure(bg='#015482')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = screen_width // 2
    height = screen_height // 1
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def open_chapter_window(subject_window, subject_name):
    subject_window.withdraw()

    chapter_window = tk.Toplevel()
    chapter_window.title(f"{subject_name} - Chapters")
    set_crystal_background_and_center(chapter_window)
    chapter_window.configure(bg="#015482")

    tk.Label(chapter_window, text=f"{subject_name} - Select a Part",
             font=("Arial", 18, "bold"), bg="#A7C7E7", fg="#015482").pack(pady=30)

    part_frame = tk.Frame(chapter_window, bg="#FAF9F6")
    part_frame.pack(pady=10)

    def on_part_click(part):
        messagebox.showinfo("Part Selected", f"You selected {subject_name} - {part}")
        open_part_chapters(chapter_window)

    part1_btn = tk.Button(part_frame, text="Part 1", font=("Arial", 14, "bold"),
                          width=15, height=3, bg="#007fb3", fg="white",
                          command=lambda: on_part_click("Part 1"))
    part1_btn.grid(row=0, column=0, padx=20)

    part2_btn = tk.Button(part_frame, text="Part 2", font=("Arial", 14, "bold"),
                          width=15, height=3, bg="#007fb3", fg="white",
                          command=lambda: on_part_click("Part 2"))
    part2_btn.grid(row=0, column=1, padx=20)

    back_img = ImageTk.PhotoImage(Image.open("ba.png").resize((30, 30)))

    def go_back_to_subject():
        chapter_window.destroy()
        subject_window.deiconify()

    back_btn = tk.Button(chapter_window, image=back_img, text=" Back", compound="left",
                         font=("Arial", 12, "bold"), bg="gray", fg="white",
                         command=go_back_to_subject, padx=10, pady=5)
    back_btn.image = back_img
    back_btn.pack(pady=40)

def open_part_chapters(chapter_window):
    chapters_window = tk.Toplevel(chapter_window)
    chapters_window.title("Chapters")
    set_crystal_background_and_center(chapters_window)
    chapters_window.configure(bg="#015482")

    tk.Label(chapters_window, text="Select a Chapter",
             font=("Arial", 18, "bold"), bg="#A7C7E7", fg="#015482").pack(pady=30)

    chapter_frame = tk.Frame(chapters_window, bg="#015482")
    chapter_frame.pack(pady=10)

    # Load chapter image
    chapter_img = Image.open("5.png").resize((80, 80))
    chapter_icon = ImageTk.PhotoImage(chapter_img)

    def on_chapter_click(chapter):
        if chapter == 1:
            open_level_window(chapters_window, chapter)
        else:
            messagebox.showinfo("Chapter Selected", f"You selected Chapter {chapter}")

    for i in range(1, 11):
        btn = tk.Button(chapter_frame, text=f"Chapter {i}", image=chapter_icon,
                        compound="top", font=("Arial", 12, "bold"),
                        width=100, height=100, bg="#007fb3", fg="white",
                        command=lambda chapter=i: on_chapter_click(chapter))
        btn.image = chapter_icon  # Keep reference
        btn.grid(row=(i-1)//5, column=(i-1)%5, padx=15, pady=15)

    back_img = ImageTk.PhotoImage(Image.open("ba.png").resize((30, 30)))

    def go_back_to_part():
        chapters_window.destroy()
        chapter_window.deiconify()

    back_btn = tk.Button(chapters_window, image=back_img, text=" Back", compound="left",
                         font=("Arial", 12, "bold"), bg="gray", fg="white",
                         command=go_back_to_part, padx=10, pady=5)
    back_btn.image = back_img
    back_btn.pack(pady=40)

def open_level_window(parent_window, chapter_num):
    level_window = tk.Toplevel(parent_window)
    level_window.title(f"Chapter {chapter_num} - Levels")
    set_crystal_background_and_center(level_window)
    level_window.configure(bg="#015482")

    tk.Label(level_window, text=f"Chapter {chapter_num} - Select a Level",
             font=("Arial", 18, "bold"), bg="#A7C7E7", fg="#015482").pack(pady=30)

    level_frame = tk.Frame(level_window, bg="#015482")
    level_frame.pack(pady=10)

    def on_level_click(level):
        messagebox.showinfo("Level Selected", f"You selected Level {level}")

    for i in range(1, 26):
        level = i
        btn = tk.Button(level_frame, text=f"Level {level}", font=("Arial", 10, "bold"),
                        width=10, height=2, bg="#007fb3", fg="white",
                        command=lambda lvl=level: on_level_click(lvl))
        btn.grid(row=i//5, column=i%5, padx=10, pady=10)

    more_img = ImageTk.PhotoImage(Image.open("rba.png").resize((30, 30)))

    def open_more_levels():
        more_levels_window = tk.Toplevel(level_window)
        more_levels_window.title(f"Chapter {chapter_num} - More Levels")
        set_crystal_background_and_center(more_levels_window)
        more_levels_window.configure(bg="#015482")

        tk.Label(more_levels_window, text=f"Chapter {chapter_num} - More Levels",
                 font=("Arial", 18, "bold"), bg="#A7C7E7", fg="#015482").pack(pady=30)

        more_level_frame = tk.Frame(more_levels_window, bg="#015482")
        more_level_frame.pack(pady=10)

        for i in range(26, 51):
            level = i
            btn = tk.Button(more_level_frame, text=f"Level {level}", font=("Arial", 10, "bold"),
                            width=10, height=2, bg="#007fb3", fg="white",
                            command=lambda lvl=level: on_level_click(lvl))
            btn.grid(row=(i-26)//5, column=(i-26)%5, padx=10, pady=10)

        back_img = ImageTk.PhotoImage(Image.open("ba.png").resize((30, 30)))

        def go_back_to_levels():
            more_levels_window.destroy()

        back_btn = tk.Button(more_levels_window, image=back_img, text=" Back", compound="left",
                             font=("Arial", 12, "bold"), bg="gray", fg="white",
                             command=go_back_to_levels, padx=10, pady=5)
        back_btn.image = back_img
        back_btn.pack(pady=30)

    more_btn = tk.Button(level_window, image=more_img, text=" More Levels", compound="left",
                         font=("Arial", 12, "bold"), bg="gray", fg="white", command=open_more_levels,
                         padx=10, pady=5)
    more_btn.image = more_img
    more_btn.pack(pady=30)

    back_img = ImageTk.PhotoImage(Image.open("ba.png").resize((30, 30)))

    def go_back_to_chapters():
        level_window.destroy()
        parent_window.deiconify()

    back_btn = tk.Button(level_window, image=back_img, text=" Back", compound="left",
                         font=("Arial", 12, "bold"), bg="gray", fg="white",
                         command=go_back_to_chapters, padx=10, pady=5)
    back_btn.image = back_img
    back_btn.pack(pady=30)

def open_subject_window():
    root.withdraw()

    subject_window = tk.Toplevel()
    subject_window.title("Select Subject")
    set_crystal_background_and_center(subject_window)

    top_frame = tk.Frame(subject_window, bg='#015482')
    top_frame.pack(pady=(20, 10))

    tk.Label(top_frame, text=f"Welcome, {player_data['name']}!",
             font=("Arial", 16, "bold"), bg='#015482', fg="white").pack(side="left", padx=(0, 20))

    avatar_img = male_photo if player_data['avatar'] == "male" else female_photo
    avatar_label = tk.Label(top_frame, image=avatar_img, bg='#015482')
    avatar_label.image = avatar_img
    avatar_label.pack(side="left")

    tk.Label(subject_window, text="Select Your Subject",
             font=("Arial", 18, "bold"), bg='#015482', fg="white").pack(pady=(10, 30))

    physics_img = ImageTk.PhotoImage(Image.open("p.png").resize((100, 100)))
    chemistry_img = ImageTk.PhotoImage(Image.open("ch.png").resize((100, 100)))
    math_img = ImageTk.PhotoImage(Image.open("m.png").resize((100, 100)))
    biology_img = ImageTk.PhotoImage(Image.open("b.png").resize((100, 100)))

    subjects = [("Physics", physics_img), ("Chemistry", chemistry_img),
                ("Math", math_img), ("Biology", biology_img)]

    button_frame = tk.Frame(subject_window, bg='#015482')
    button_frame.pack(pady=10)

    for i, (subject, img) in enumerate(subjects):
        btn = tk.Button(button_frame, image=img, text=subject, compound="top",
                        font=("Arial", 12, "bold"), width=120, height=140,
                        bg="#007fb3", fg="white", relief="raised", cursor="hand2",
                        command=lambda s=subject: open_chapter_window(subject_window, s))
        btn.grid(row=0, column=i, padx=15)
        btn.image = img

    back_img = ImageTk.PhotoImage(Image.open("ba.png").resize((30, 30)))

    def go_back():
        subject_window.destroy()
        root.deiconify()

    back_btn = tk.Button(subject_window, image=back_img, text=" Back", compound="left",
                         font=("Arial", 12, "bold"), bg="gray", fg="white",
                         command=go_back, padx=10, pady=5)
    back_btn.image = back_img
    back_btn.pack(pady=30)

def start_game():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Required", "Please enter your name.")
        return
    if not selected_avatar.get():
        messagebox.showwarning("Select Avatar", "Please select an avatar.")
        return

    player_data['name'] = name
    player_data['avatar'] = selected_avatar.get()
    open_subject_window()

# ==== MAIN WINDOW ====
root = tk.Tk()
root.title("Player Setup")
set_crystal_background_and_center(root)

name_bubble = tk.Frame(root, bg="#007fb3", bd=20, relief="groove")
name_bubble.pack(pady=20, padx=20)

tk.Label(name_bubble, text="Enter Your Name:", font=("Arial", 14), bg='#007fb3').pack(pady=(10, 5))
name_entry = tk.Entry(name_bubble, font=("Arial", 12), width=30, relief="flat",
                      highlightthickness=1, highlightbackground="#121212")
name_entry.pack(pady=(0, 10))

male_img = Image.open("male_avatar.png").resize((120, 180))
female_img = Image.open("female_avatar.png").resize((120, 180))
male_photo = ImageTk.PhotoImage(male_img)
female_photo = ImageTk.PhotoImage(female_img)

selected_avatar = tk.StringVar()

avatar_bubble = tk.Frame(root, bg="#007fb3", bd=20, relief="groove")
avatar_bubble.pack(pady=10)

tk.Label(avatar_bubble, text="Select Your Avatar:", font=("Arial", 14), bg='#007fb3').pack(pady=10)

frame = tk.Frame(avatar_bubble, bg='#FAF9F6')
frame.pack(pady=5)

def select_avatar(avatar):
    selected_avatar.set(avatar)
    male_border.config(bg="black" if avatar == "male" else "#FAF9F6")
    female_border.config(bg="black" if avatar == "female" else "#FAF9F6")

male_border = tk.Frame(frame, bd=2, relief="solid", bg="#FAF9F6")
female_border = tk.Frame(frame, bd=2, relief="solid", bg="#FAF9F6")

tk.Button(male_border, image=male_photo, command=lambda: select_avatar("male"), bd=0).pack()
tk.Button(female_border, image=female_photo, command=lambda: select_avatar("female"), bd=0).pack()

male_border.grid(row=0, column=0, padx=20)
female_border.grid(row=0, column=1, padx=20)

button_bubble = tk.Frame(root, bg="#007fb3", bd=15, relief="raised")
button_bubble.pack(pady=30)

start_btn = tk.Button(button_bubble, text="Start Game", font=("Segoe Print", 15, "bold"),
                      bg="#015482", fg="black", padx=15, pady=8, relief="raised", cursor="hand2",
                      command=start_game)
start_btn.pack(padx=10, pady=10)

root.mainloop()
