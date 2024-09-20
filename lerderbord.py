import tkinter as tk
from tkinter import ttk

def bord(game, text):
    root = tk.Tk()
    root.title(game)
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")
    title = ttk.Label(root, text=game + "\n", font=("Helvetica", 16), background="#f0f0f0")
    title.pack(pady=20)
    
    text_label = tk.Label(root, text=text.strip(), font=("Helvetica", 16), bg="#f0f0f0", padx=20, pady=10)
    text_label.pack(fill=tk.X)

def snakelederbord():
    with open("scorebords/snake.txt", "r") as file:
        lines = file.readlines()
        text = ''.join(lines[:5])
    
    bord("Snake", text) 

def tetrislederbord():
    with open("scorebords/tetris.txt", "r") as file:
        lines = file.readlines()
        text = ''.join(lines[:5])
    
    bord("Tetris", text)


def bomblederbord():
    with open("scorebords/bomb.txt", "r") as file:
        lines = file.readlines()
        text = ''.join(lines[:5])
    
    bord("Bomb", text)
