import random
import tkinter as tk
from tkinter import messagebox

top = ['','','']
midle =['','','']
botom = ['','','']

def printbord():
    global top, midle, botom, borrd_ok, text, root, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, scorex, score0
    bb1["text"] = top[0]
    bb2["text"] = top[1]
    bb3["text"] = top[2]
    bb4["text"] = midle[0]
    bb5["text"] = midle[1]
    bb6["text"] = midle[2]
    bb7["text"] = botom[0]
    bb8["text"] = botom[1]
    bb9["text"] = botom[2]
    print()
    print(top)
    print(midle)
    print(botom)
    print()

def keypress(button):
    global top, midle, botom, borrd_ok, text, root, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, scorex, score0
    if button == "t0" and top[0] == "":
        top[0] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "t1" and top[1] == "":
        top[1] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "t2" and top[2] == "":
        top[2] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "m0" and midle[0] == "":
        midle[0] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "m1" and midle[1] == "":
        midle[1] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "m2" and midle[2] == "":
        midle[2] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "b0" and botom[0] == "":
        botom[0] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "b1" and botom[1] == "":
        botom[1] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    elif button == "b2" and botom[2] == "":
        botom[2] = "x"
        text["text"] = ""
        check()
        printbord()
        verchal_per()
        printbord()
    else:
        text["text"] = "Place not valid"

def relode():
    global root, top, midle, botom
    root.destroy()
    top = ["","",""]
    midle = ["","",""]
    botom = ["","",""]
    loop()

def scoreupdate():
    global top, midle, botom, borrd_ok, text, root, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, scx, sc0, scorex, score0
    scx["text"] = scorex
    sc0["text"] = score0

def check():
    print("cheching for winer")
    printbord()
    global top, midle, botom, borrd_ok, text, root, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9,scorex, score0
    state  = 1
    if top[0] != '' and top[1] != '' and top[2] != '' and top[0] == top[1] == top[2]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = top[0] +  ' Wins'
        if top[0] == "x":
            scoreupdate()
            scorex = scorex + 1
        else:
            score0 = score0 + 1
            scoreupdate()
    elif midle[0] != '' and midle[1] != '' and midle[2] != '' and midle[0] == midle[1] == midle[2]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = midle[0] +  ' Wins'
        if midle[0] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif botom[0] != '' and botom[1] != '' and botom[2] != '' and botom[0] == botom[1] == botom[2]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = botom[0] +  ' Wins'
        if botom[0] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif  top[0] != '' and midle[1] != '' and botom[2] != '' and top[0] == midle[1] == botom[2]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = top[0] +  ' Wins'
        if top[0] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif botom[0] != '' and midle[1] != '' and top[2] != '' and top[2] == midle[1] == botom[0]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = botom[0] +  ' Wins'
        if botom[0] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif top[0] != '' and midle[0] != '' and botom[0] != '' and top[0] == midle[0] == botom[0]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = top[0] +  ' Wins'
        if top[0] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif top[1] != '' and midle[1] != '' and botom[1] != '' and top[1] == midle[1] == botom[1]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = top[1] +  ' Wins'
        if top[1] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif top[2] != '' and midle[2] != '' and botom[2] != '' and top[2] == midle[2] == botom[2]:
        print(top[0], 'Wins') 
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = top[2] +  ' Wins'
        if top[2] == "x":
            scorex = scorex + 1
            scoreupdate()
        else:
            score0 = score0 + 1
            scoreupdate()

    elif top[0] and top[1] and top[2] and botom[0] and botom[1] and botom[2] and midle[0] and midle[1] and midle[2] != "":
        print("it is a drow")
        printbord()
        bb1.config(state=tk.DISABLED)
        bb2.config(state=tk.DISABLED)
        bb3.config(state=tk.DISABLED)
        bb4.config(state=tk.DISABLED)
        bb5.config(state=tk.DISABLED)
        bb6.config(state=tk.DISABLED)
        bb7.config(state=tk.DISABLED)
        bb8.config(state=tk.DISABLED)
        bb9.config(state=tk.DISABLED)
        text["text"] = "Draw"
        scoreupdate()

def scanme():
    global top, midle, botom

    if top[0] == "0" and top[1] == "0" and top[2] == "":
        return "t2"
    elif top[2] == "0" and top[1] == "0"  and top[0] == "":
        return "t0"
    elif top[0] == "0" and top[2] == "0"  and top[1] == "":
        return "t1"
    
    elif midle[0] == "0" and midle[1] == "0" and midle[2] == "":
        return "m2"
    elif midle[2] == "0" and midle[1] == "0"and midle[0] == "":
        return "m0"
    elif midle[0] == "0" and midle[2] == "0" and midle[1] == "":
        return "m1"
    
    elif botom[0] == "0" and botom[1] == "0" and botom[2] == "":
        return "b2"
    elif botom[2] == "0" and botom[1] == "0" and botom[0] == "":
        return "b0"
    elif botom[0] == "0" and botom[2] == "0" and botom[1] == "":
        return "b1"

    elif top[0] == "0" and botom[2] == "0" and midle[1] == "":
        return "m1"
    elif top[0] == "0" and midle[1] == "0" and botom[2] == "":
        return "b2"
    elif botom[2] == "0" and midle[1] == "0" and top[0] == "":
        return "t1"

    elif top[2] == "0" and botom[0] == "0" and midle[1] == "":
        return "m1"
    elif top[2] == "0" and midle[1] == "0" and botom[0] == "":
        return "b0"
    elif botom[0] == "0" and midle[1] == "0" and top[2] == "":
        return "t2"

    elif top[0] == "0" and botom[0] == "0" and midle[0] == "":
        return "m0"
    elif top[0] == "0" and midle[0] == "0" and botom[0] == "":
        return "b0"
    elif botom[0] == "0" and midle[0] == "0" and top[0] == "":
        return "t0"

    elif top[1] == "0" and botom[1] == "0" and midle[1] == "":
        return "m1"
    elif top[1] == "0" and midle[1] == "0" and botom[1] == "":
        return "b1"
    elif botom[1] == "0" and midle[1] == "0" and top[1] == "":
        return "t1"

    elif top[2] == "0" and botom[2] == "0" and midle[2] == "":
        return "m2"
    elif top[2] == "0" and midle[2] == "0" and botom[2] == "":
        return "b2"
    elif botom[2] == "0" and midle[2] == "0" and top[2] == "":
        return "t2"

    else:
        return ""

def scan():
    global top, midle, botom

    if top[0] == "x" and top[1] == "x" and top[2] == "":
        return "t2"
    elif top[2] == "x" and top[1] == "x"  and top[0] == "":
        return "t0"
    elif top[0] == "x" and top[2] == "x"  and top[1] == "":
        return "t1"
    
    elif midle[0] == "x" and midle[1] == "x" and midle[2] == "":
        return "m2"
    elif midle[2] == "x" and midle[1] == "x"and midle[0] == "":
        return "m0"
    elif midle[0] == "x" and midle[2] == "x" and midle[1] == "":
        return "m1"
    
    elif botom[0] == "x" and botom[1] == "x" and botom[2] == "":
        return "b2"
    elif botom[2] == "x" and botom[1] == "x" and botom[0] == "":
        return "b0"
    elif botom[0] == "x" and botom[2] == "x" and botom[1] == "":
        return "b1"

    elif top[0] == "x" and botom[2] == "x" and midle[1] == "":
        return "m1"
    elif top[0] == "x" and midle[1] == "x" and botom[2] == "":
        return "b2"
    elif botom[2] == "x" and midle[1] == "x" and top[0] == "":
        return "t1"

    elif top[2] == "x" and botom[0] == "x" and midle[1] == "":
        return "m1"
    elif top[2] == "x" and midle[1] == "x" and botom[0] == "":
        return "b0"
    elif botom[0] == "x" and midle[1] == "x" and top[2] == "":
        return "t2"

    elif top[0] == "x" and botom[0] == "x" and midle[0] == "":
        return "m0"
    elif top[0] == "x" and midle[0] == "x" and botom[0] == "":
        return "b0"
    elif botom[0] == "x" and midle[0] == "x" and top[0] == "":
        return "t0"

    elif top[1] == "x" and botom[1] == "x" and midle[1] == "":
        return "m1"
    elif top[1] == "x" and midle[1] == "x" and botom[1] == "":
        return "b1"
    elif botom[1] == "x" and midle[1] == "x" and top[1] == "":
        return "t1"

    elif top[2] == "x" and botom[2] == "x" and midle[2] == "":
        return "m2"
    elif top[2] == "x" and midle[2] == "x" and botom[2] == "":
        return "b2"
    elif botom[2] == "x" and midle[2] == "x" and top[2] == "":
        return "t2"

    else:
        return ""



        


def verchal_per():
    block2 = scanme()
    if block2 != "":
        print("hi")
        if block2 == "t0":
            if top[0] == '':
                top[0] = '0'
            else:
                print("something when rong")
        elif block2 == "t1":
            if top[1] == '':
                top[1] = '0'
            else:
                print("something when rong")
        elif block2 == "t2":
            if top[2] == '':
                top[2] = '0'
            else:
                print("something when rong")
        elif block2 == "m0":
            if midle[0] == '':
                midle[0] = '0'
            else:
                print("something when rong")
        elif block2 == "m1":
            if midle[1] == '':
                midle[1] = '0'
            else:
                print("something when rong")
        elif block2 == "m2":
            if midle[2] == '':
                midle[2] = '0'
            else:
                print("something when rong")
        elif block2 == "b0":
            if botom[0] == '':
                botom[0] = '0'
            else:
                print("something when rong")
        elif block2 == "b1":
            if botom[1] == '':
                botom[1] = '0'
            else:
                print("something when rong")
        elif block2 == "b2":
            if botom[2] == '':
                botom[2] = '0'
            else:
                print("something when rong")
    else:
        
        block = scan()
        if block != "":
            if block == "t0":
                if top[0] == '':
                    top[0] = '0'
                else:
                    print("something when rong")
            elif block == "t1":
                if top[1] == '':
                    top[1] = '0'
                else:
                    print("something when rong")
            elif block == "t2":
                if top[2] == '':
                    top[2] = '0'
                else:
                    print("something when rong")
            elif block == "m0":
                if midle[0] == '':
                    midle[0] = '0'
                else:
                    print("something when rong")
            elif block == "m1":
                if midle[1] == '':
                    midle[1] = '0'
                else:
                    print("something when rong")
            elif block == "m2":
                if midle[2] == '':
                    midle[2] = '0'
                else:
                    print("something when rong")
            elif block == "b0":
                if botom[0] == '':
                    botom[0] = '0'
                else:
                    print("something when rong")
            elif block == "b1":
                if botom[1] == '':
                    botom[1] = '0'
                else:
                    print("something when rong")
            elif block == "b2":
                if botom[2] == '':
                    botom[2] = '0'
                else:
                    print("something when rong")
        else:
            
            if top[0] == "x" or top[2] == "x" or botom[0] == "x" or botom[2] == "x" and midle[1] != "x":
                if midle[1] == '':
                    midle[1] = '0'
                else:
                    if midle[2] == '':
                        midle[2] = '0'
                    else:
                        if midle[0] == '':
                            midle[0] = '0'
                        else:
                            if top[0] == '':
                                top[0] = '0'
                            elif top[2] == '':
                                top[2] = '0'
                            elif botom[2] == '':
                                botom[2] = '0'
                            elif botom[0] == '':
                                botom[0] = '0'
                            elif top[1] == '':
                                top[1] = '0'
                            elif midle[0] == '':
                                midle[0] = '0'
                            elif midle[1] == '':
                                midle[1] = '0'
                            elif midle[2] == '':
                                midle[2] = '0'
                            elif botom[1] == '':
                                botom[1] = '0'

            elif midle[1] == "x":
                if top[0] == '':
                    top[0] = '0'
                else: 
                    if top[2] == '':
                        top[2] = '0'

            else:
                if top[0] == '':
                    top[0] = '0'
                elif top[2] == '':
                    top[2] = '0'
                elif botom[2] == '':
                    botom[2] = '0'
                elif botom[0] == '':
                    botom[0] = '0'
                elif top[1] == '':
                    top[1] = '0'
                elif midle[0] == '':
                    midle[0] = '0'
                elif midle[1] == '':
                    midle[1] = '0'
                elif midle[2] == '':
                    midle[2] = '0'
                elif botom[1] == '':
                    botom[1] = '0'
    check()
def loop():
    global borrd_ok, text, root, bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8, bb9, scx, sc0, scorex, score0
    root = tk.Tk()
    root.title("0 and X")
    title = tk.Label(root, text= "0 and X", font=('normal', 40))
    score = tk.Label(root, text= "Score", font=('normal', 20))
    scx = tk.Label(root, text= "0", font=('normal', 20))
    sc0 = tk.Label(root, text= "0", font=('normal', 20))
    xlable = tk.Label(root, text="x", font=('normal', 15))
    olable = tk.Label(root, text="0", font=('normal', 15))
    bb1 = tk.Button(root, text= "", command=lambda:  keypress("t0"), width= 5, height= 2, font=('normal', 40))
    bb2 = tk.Button(root, text= "", command=lambda:  keypress("t1"), width= 5, height= 2, font=('normal', 40))
    bb3 = tk.Button(root, text= "", command=lambda:  keypress("t2"), width= 5, height= 2, font=('normal', 40))
    bb4 = tk.Button(root, text= "", command=lambda:  keypress("m0"), width= 5, height= 2, font=('normal', 40))
    bb5 = tk.Button(root, text= "", command=lambda:  keypress("m1"), width= 5, height= 2, font=('normal', 40))
    bb6 = tk.Button(root, text= "", command=lambda:  keypress("m2"), width= 5, height= 2, font=('normal', 40))
    bb7 = tk.Button(root, text= "", command=lambda:  keypress("b0"), width= 5, height= 2, font=('normal', 40))
    bb8 = tk.Button(root, text= "", command=lambda:  keypress("b1"), width= 5, height= 2, font=('normal', 40))
    bb9 = tk.Button(root, text= "", command=lambda:  keypress("b2"), width= 5, height= 2, font=('normal', 40))
    text = tk.Label(root, text= "", font=('normal', 20))
    but = tk.Button(root, text= "Reload", command= relode , font=('normal', 20))

    title.grid(row= 0, column= 0, columnspan= 3)
    score.grid(row=1, column=0)
    scx.grid(row=1, column=1)
    sc0.grid(row=1, column=2)
    xlable.grid(row=2, column=1)
    olable.grid(row=2, column=2)

    bb1.grid(row=3, column=0)
    bb2.grid(row=3, column=1)
    bb3.grid(row=3, column=2)
    bb4.grid(row=4, column=0)
    bb5.grid(row=4, column=1)
    bb6.grid(row=4, column=2)
    bb7.grid(row=5, column=0)
    bb8.grid(row=5, column=1)
    bb9.grid(row=5, column=2)
    text.grid(row=6, column=0, columnspan=3)
    but.grid(row=7, column= 0, columnspan=3)
    scoreupdate()
    root.mainloop()

def start0andx():
    global scorex, score0
    scorex = 0
    score0 = 0
    loop()

