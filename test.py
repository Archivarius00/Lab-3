import tkinter as tk
import pygame
import random


coding = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
    }

def keygen1():
     block = genblock1()
     return block

def keygen2():
    password = []
    for _ in range(2):
        block = genblock2()
        password.append(block)
    return '-'.join(password)

def genblock1():    
    while True:
            block = random.choices(list(coding.keys()), k=5)
            weight = sum(coding[i] for i in block) / 5
            if 10 <= weight <= 15:
                return ''.join(block)

def genblock2():    
    while True:
            block = random.choices(list(coding.keys()), k=4)
            weight = sum(coding[i] for i in block) / 4
            if 10 <= weight <= 15:
                return ''.join(block)

def key():
    key1 = keygen1()
    key2 = keygen2()
    key = f"{key1}-{key2}"
    return key

def generate():
    lbl_result.configure(text = (key()))

def exit():
    window.destroy()

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Cyberpunk 2077 Unreleased OST – The Rebel Path (Cello Version).mp3")
pygame.mixer.music.play()


window = tk.Tk()
window.title('Cyberpunk code generator')
window.geometry('1165x645')
bg_img = tk.PhotoImage(file='Johny.png')

label_pic = tk.Label(window, image=bg_img)
label_pic.place(x=0, y=0, relwidth=1, relheight=1)
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.65, anchor='center')

lbl_result = tk.Label(frame, text='Press button to generate', font=('Comic Sans MS', 15))
lbl_result.grid(column=1, row=1, padx=10, pady=10)
btn_start = tk.Button(frame, text='Generate', command=generate, font=('Comic Sans MS', 10))
btn_start.grid(column=1, row=3, padx=10, pady=10)


window.mainloop()