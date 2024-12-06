import tkinter as tk
from tkmacosx import Button  # Importing Button from tkmacosx
from tkinter import PhotoImage
import random
from PIL import Image, ImageTk

# Function to determine the winner
def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    ai_choice = random.choice(options)

    # Update AI choice display
    ai_image_label.config(image=ai_images[ai_choice])
    ai_label.config(text=f"AI Chose: {ai_choice}")

    # Add border effect to AI choice
    ai_image_label.configure(highlightbackground="#ff9800", highlightthickness=2)

    # Game rules
    if user_choice == ai_choice:
        result_label.config(text="It's a Tie!", fg="#ff9800")
    elif (user_choice == "Rock" and ai_choice == "Scissors") or \
         (user_choice == "Paper" and ai_choice == "Rock") or \
         (user_choice == "Scissors" and ai_choice == "Paper"):
        result_label.config(text="You Win!", fg="#4caf50")
    else:
        result_label.config(text="AI Wins!", fg="#f44336")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors - AI Challenge")
root.geometry("600x800")
root.iconphoto(True, PhotoImage(file='/Users/subhamrakshit/Desktop/coding/GUI/rk-ppr-scrs-tkinter/assets/rock-paper-scissors.png'))
root.configure(bg="#e3f2fd")

# Title label
title_label = tk.Label(
    root, text="Rock Paper Scissors", font=("Helvetica", 30, "bold"), bg="#e3f2fd", fg="#2b2b2b"
)
title_label.pack(pady=20)

# Frame for player's choice
player_frame = tk.Frame(root, bg="#e3f2fd")
player_frame.pack(pady=10)

# "You Chose" label
player_label = tk.Label(
    player_frame, text="You Chose:", font=("Helvetica", 20, "bold"), bg="#e3f2fd", fg="#2b2b2b"
)
player_label.pack()

# Frame for buttons
button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=30)

# Load images for buttons
rock_image = ImageTk.PhotoImage(Image.open("/Users/subhamrakshit/Desktop/coding/GUI/rk-ppr-scrs-tkinter/assets/rock.jpg").resize((120, 120)))
paper_image = ImageTk.PhotoImage(Image.open("/Users/subhamrakshit/Desktop/coding/GUI/rk-ppr-scrs-tkinter/assets/paper.jpg").resize((120, 120)))
scissors_image = ImageTk.PhotoImage(Image.open("/Users/subhamrakshit/Desktop/coding/GUI/rk-ppr-scrs-tkinter/assets/scissors.jpg").resize((120, 120)))

# AI choice images
ai_images = {
    "Rock": rock_image,
    "Paper": paper_image,
    "Scissors": scissors_image
}

# Button styles
button_style = {
    "bd": 0,
    "highlightbackground": "#bbdefb",
    "bg": "#ffffff",
    "activebackground": "#90caf9",
    "font": ("Helvetica", 14, "bold"),
}

# Rock button
rock_button = Button(
    button_frame, image=rock_image, text="Rock", compound="top", **button_style,
    command=lambda: determine_winner("Rock")
)
rock_button.grid(row=0, column=0, padx=20, pady=20)

# Paper button
paper_button = Button(
    button_frame, image=paper_image, text="Paper", compound="top", **button_style,
    command=lambda: determine_winner("Paper")
)
paper_button.grid(row=0, column=1, padx=20, pady=20)

# Scissors button
scissors_button = Button(
    button_frame, image=scissors_image, text="Scissors", compound="top", **button_style,
    command=lambda: determine_winner("Scissors")
)
scissors_button.grid(row=0, column=2, padx=20, pady=20)

# Label for AI's choice
ai_image_label = tk.Label(root, bg="#e3f2fd", highlightthickness=0)
ai_image_label.pack(pady=20)
ai_label = tk.Label(
    root, text="AI Chose: ", font=("Helvetica", 18, "italic"), bg="#e3f2fd", fg="#2b2b2b"
)
ai_label.pack()

# Label for result
result_label = tk.Label(
    root, text="", font=("Helvetica", 22, "bold"), bg="#e3f2fd"
)
result_label.pack(pady=40)

# Footer
footer_label = tk.Label(
    root, text="Let's Play!", font=("Helvetica", 16, "italic"), bg="#e3f2fd", fg="#607d8b"
)
footer_label.pack(pady=20)

# Run the main loop
root.mainloop()
