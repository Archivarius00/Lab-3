import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Generate the key according to the specified rules
def generate_key():
    input_number = entry.get()
    if not input_number.isdigit() or len(input_number) != 6:
        messagebox.showerror("Error", "Введите шестизначное число.")
        return

    # Separate digits for the key format
    block1_digits = input_number[3:6]  # 4, 5, 6 digits
    block2_digits = input_number[0:3]  # 1, 2, 3 digits

    # Generate random letters
    letters1 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    letters2 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))

    # Calculate the sum of the digits in block 1 and block 2
    sum_block = sum(int(digit) for digit in block1_digits + block2_digits)

    # Format the key
    generated_key = f"{block1_digits}{letters1}-{block2_digits}{letters2}-{sum_block:04d}"
    
    # Display the generated key
    result_label.config(text=f"Сгенерированный ключ: {generated_key}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Keygen")
root.geometry("400x300")

background_image = Image.open("C:/Users/marki/Downloads/Lab 3 python/bg_pic.jpg")
background_image = background_image.resize((400, 300), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Add instructions label
instruction_label = tk.Label(root, text="Введите шестизначное число:", bg="white", font=("Arial", 12))
instruction_label.pack(pady=10)

# Entry for user input
entry = tk.Entry(root, font=("Arial", 12), width=10)
entry.pack(pady=5)

# Button to generate the key
generate_button = tk.Button(root, text="Генерировать ключ", command=generate_key, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

# Label to display the generated key
result_label = tk.Label(root, text="", bg="white", font=("Arial", 12))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
