import tkinter as tk
from tkinter import ttk
from bomb import play_bombdodger
from snake import startsnake
from ticktacktow import start0andx
from pong import ponggo
from pong_1_player import ponggo1
from tetrers import trtrasopen
from fileexplorer2 import mainfiel
from lerderbord import *

def main():

    root = tk.Tk()
    root.title("Multiple Games App")
    root.geometry("400x500")

    notebook = ttk.Notebook(root)

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)

    notebook.add(tab1, text="Games")
    notebook.add(tab2, text="Lederbords")
    notebook.add(tab3, text="Other apps")

    label = ttk.Label(tab1, text="Welcome to Multiple Games", font=("Helvetica", 16))
    label.pack(pady=20)

    button_snake = ttk.Button(tab1, text="Snake", command=startsnake)
    button_snake.pack(fill=tk.X, padx=20, pady=10)

    button_tic_tac_toe = ttk.Button(tab1, text="Tic Tac Toe", command=start0andx)
    button_tic_tac_toe.pack(fill=tk.X, padx=20, pady=10)

    button_bome_game = ttk.Button(tab1, text="Bome game", command=play_bombdodger)
    button_bome_game.pack(fill=tk.X, padx=20, pady=10)

    button_pong = ttk.Button(tab1, text="Pong", command=ponggo)
    button_pong.pack(fill=tk.X, padx=20, pady=10)

    button_pong_1_player = ttk.Button(tab1, text="Pong 1 player", command=ponggo1)
    button_pong_1_player.pack(fill=tk.X, padx=20, pady=10)

    button_trtrus = ttk.Button(tab1, text="Tetris", command=trtrasopen)
    button_trtrus.pack(fill=tk.X, padx=20, pady=10)


    button_quit = ttk.Button(tab1, text="Quit", command=root.quit)
    button_quit.pack(fill=tk.X, padx=20, pady=10)




    label = ttk.Label(tab2, text="Welcome to Multiple Games lederbords", font=("Helvetica", 16))
    label.pack(pady=20)

    button_snake = ttk.Button(tab2, text="Snake", command=snakelederbord)
    button_snake.pack(fill=tk.X, padx=20, pady=10)

    button_tic_tac_toe = ttk.Button(tab2, text="Tic Tac Toe",  state="disabled")#, command=start0andx)
    button_tic_tac_toe.pack(fill=tk.X, padx=20, pady=10)

    button_bome_game = ttk.Button(tab2, text="Bome game", command=bomblederbord)
    button_bome_game.pack(fill=tk.X, padx=20, pady=10)

    button_pong = ttk.Button(tab2, text="Pong",  state="disabled")#, command=ponggo)
    button_pong.pack(fill=tk.X, padx=20, pady=10)

    button_pong_1_player = ttk.Button(tab2, text="Pong 1 player",  state="disabled")#, command=ponggo1)
    button_pong_1_player.pack(fill=tk.X, padx=20, pady=10)

    button_trtrus = ttk.Button(tab2, text="Tetris", command=tetrislederbord)
    button_trtrus.pack(fill=tk.X, padx=20, pady=10)

    button_quit = ttk.Button(tab2, text="Quit", command=root.quit)
    button_quit.pack(fill=tk.X, padx=20, pady=10)


    label = ttk.Label(tab3, text="Welcome to Multiple Games other apps", font=("Helvetica", 16))
    label.pack(pady=20)

    button_file_explorer = ttk.Button(tab3, text="File explorer", command=mainfiel)
    button_file_explorer.pack(fill=tk.X, padx=20, pady=10)

    button_quit = ttk.Button(tab3, text="Quit", command=root.quit)
    button_quit.pack(fill=tk.X, padx=20, pady=10)

    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    root.mainloop()
