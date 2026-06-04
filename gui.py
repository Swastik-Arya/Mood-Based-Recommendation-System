from tkinter import *
from recommender import Recommender

rec = Recommender()

root = Tk()
root.title("Mood Recommender")
root.geometry("650x700")

# ------------------ VARIABLES ------------------
mood = StringVar(value="Happy")
category = StringVar(value="Movie")
language = StringVar(value="Hindi")
reason = StringVar(value="Breakup")

current_results = []

# ------------------ TITLE ------------------
Label(root, text="Mood Based Recommender", font=("Arial", 16, "bold")).pack(pady=10)

# ------------------ MOOD ------------------
Label(root, text="Select Mood").pack()
mood_menu = OptionMenu(root, mood,
                       "Happy", "Sad", "Romantic", "Motivation", "Relaxed", "Excited", "Horror")
mood_menu.pack(pady=5)

# ------------------ REASON (ONLY FOR SAD) ------------------
reason_label = Label(root, text="Why are you feeling sad?")
reason_menu = OptionMenu(root, reason, "Breakup", "Family")

def update_reason_visibility(*args):
    if mood.get() == "Sad":
        reason_label.pack()
        reason_menu.pack()
    else:
        reason_label.pack_forget()
        reason_menu.pack_forget()

mood.trace("w", update_reason_visibility)

# ------------------ CATEGORY ------------------
Label(root, text="Select Type").pack()
OptionMenu(root, category, "Movie", "Music", "Book", "Series").pack(pady=5)

# ------------------ LANGUAGE ------------------
Label(root, text="Select Language").pack()
OptionMenu(root, language, "Hindi", "English").pack(pady=5)

# ------------------ RESULT BOX ------------------
result_box = Text(root, height=18, width=75)
result_box.pack(pady=10)

# ------------------ FUNCTIONS ------------------

def show_results():
    global current_results
    result_box.delete("1.0", END)

    current_results = rec.get_recommendations(
        mood.get(),
        category.get(),
        language.get(),
        reason.get() if mood.get() == "Sad" else None
    )

    # Display grouped output
    result_box.insert(END, "----- OLD -----\n")
    for r in current_results[:5]:
        result_box.insert(END, r + "\n")

    result_box.insert(END, "\n----- MID -----\n")
    for r in current_results[5:10]:
        result_box.insert(END, r + "\n")

    result_box.insert(END, "\n----- NEW -----\n")
    for r in current_results[10:15]:
        result_box.insert(END, r + "\n")


def like():
    if current_results:
        print("Liked:", current_results)


def dislike():
    if current_results:
        print("Disliked:", current_results)


def refresh():
    show_results()

# ------------------ BUTTON FRAME ------------------
button_frame = Frame(root)
button_frame.pack(pady=10)

Button(button_frame, text="Recommend", command=show_results, bg="green", fg="white", width=12).grid(row=0, column=0, padx=5)
Button(button_frame, text="👍 Like", command=like, width=10).grid(row=0, column=1, padx=5)
Button(button_frame, text="👎 Dislike", command=dislike, width=10).grid(row=0, column=2, padx=5)
Button(button_frame, text="🔄 Refresh", command=refresh, width=10).grid(row=0, column=3, padx=5)

root.mainloop()