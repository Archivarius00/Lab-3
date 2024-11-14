import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pygame  # Biblioteca para reproducir música
import time

# Inicializar pygame para la música
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/marki/Downloads/MUSICA/Imagine_Dragons_Im_so_sorry.mp3")
pygame.mixer.music.play(-1)  # -1 indica que la música se reproducirá en bucle

def generate_key():
    input_number = entry.get()
    if not input_number.isdigit() or len(input_number) != 6:
        messagebox.showerror("Error", "Введите шестизначное число.")
        return

    block1_digits = input_number[3:6]  
    block2_digits = input_number[0:3]  

    letters1 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    letters2 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))

    sum_block = sum(int(digit) for digit in block1_digits + block2_digits)

    generated_key = f"{block1_digits}{letters1}-{block2_digits}{letters2}-{sum_block:04d}"
    
    animate_text(f"Сгенерированный ключ: {generated_key}")

def animate_text(text):
    result_label.config(text=text)
    for _ in range(5):  
        result_label.config(fg="red")
        root.update()
        time.sleep(0.1)
        result_label.config(fg="blue")
        root.update()
        time.sleep(0.1)
    result_label.config(fg="black")  
root = tk.Tk()
root.title("Keygen")
root.geometry("400x300")

background_image = Image.open("C:/Users/marki/Downloads/Lab 3 python/bg_pic.jpg")
background_image = background_image.resize((400, 300), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

instruction_label = tk.Label(root, text="Введите шестизначное число:", bg="white", font=("Arial", 12))
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=10)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Генерировать ключ", command=generate_key, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="white", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

pygame.mixer.music.stop()
