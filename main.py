print("_INITIATING PRESCRIPT DEVICE._")

from tkinter import *
import random
import keyboard
import winsound

disable=False

root = Tk()
root.title("DEVICE:")
root.iconbitmap("assets/mark.ico")
root.geometry("133x133")
root.config(bg = "black")
root.attributes("-topmost", True)

lbl = Label(root, text = "", font=("Perfect DOS VGA 437", 16), bg = "#000000", fg = "#FFFFFF")
lbl.grid(column=0, row=1, sticky="w")

glitch_chars = list("█▒░ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

prescript_jjs1 = [
    f"_After {random.randint(1, 20)} seconds, ",
    "_After being attacked, ",
    "_Before next engagement, ",
    "_After being ragdolled, ",
    "_After dashing, ",
    "_After dying, ",
    "_After landing a hit, ",
    "_After using awakening, ",
    "_As soon as possible, ",
    f"_Within the next {random.randint(1, 20)} seconds, ",
    "_Without blocking, ",
    "_Without changing characters, ",
    "_Without dying, ",
    "_Without jumping, ",
    "_Without retreating, ",
    "_Without using M1s, ",
    "_Without using special, ",
    "_Without using move 1, ",
    "_Without using move 2, ",
    "_Without using move 3, ",
    "_Without using move 4, ",
    "_Without activating awakening, ",
    "_Without moving, "

]
prescript_jjs2 = [
    "kill a player._",
    "jump on a player's head._",
    "use an emote._",
    "die._",
    f"cease movement for {random.randint(1, 20)} seconds._",
    "advance to M1 distance._",
    "mirror a player's last action._",
    "repeat last prescript command._",
    "delay next attack._",
    "ragdoll a player._",
    f"stop attacking for {random.randint(1, 20)} seconds._",
    f"stay alive for {random.randint(1, 20)} seconds._",
    "land special._",
    "land move 1._",
    "land move 2._",
    "land move 3._",
    "land move 4._",
    "activate awakening._",
    "offer a greeting._",
    "recite the first 5 digits of e._",
    "hit behind a player's block._",
    "reposition behind a player._",
    "circle a player._",
    f"play passive for {random.randint(1, 20)} seconds._",
    "assume disadvantage._",
    "use a voice emote._",
    "emote with another player._",
    "change character._",
    "evade an attack._",
    "dash._",
    f"block for {random.randint(1, 20)} seconds._",
    "land any non-M1 attack._",
    "attack a player._"

]

def glitch_text(text, index=0):
    if index <= len(text):

        display = ""

        for i in range(len(text)):
            if i < index:
                display += text[i]
            else:
                display += random.choice(glitch_chars)

        lbl.config(text=display)
        root.after(50, glitch_text, text, index + 1)

def clicked():
    global disable

    if disable == True:
        return
    disable = True
    btn.config(state=DISABLED)
    btn.config(image="",text="[+]")
    btn.grid(column=0, row=1)
    lbl.grid(column=0, row=0)
    root.geometry('175x100')
    winsound.PlaySound("assets/index_message_2.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    intermission = "_Please wait._"
    glitch_text(intermission)
    delay = random.randint(1000, 60000)
    root.after(delay, initiate_prescript)

def initiate_prescript():
    global disable
    disable = False
    winsound.PlaySound("assets/index_message_1.wav", winsound.SND_ASYNC)
    btn.grid()
    btn.config(state="normal")
    root.geometry('800x100')
    result1 = random.choice(prescript_jjs1)
    result2 = random.choice(prescript_jjs2)
    prescript = f"{result1}{result2}"
    glitch_text(prescript)
        

keyboard.add_hotkey("ctrl+f", clicked)
image = PhotoImage(file="assets/device.png")
btn = Button(root, text = "  ", 
    font=("Perfect DOS VGA 437", 25), 
    bg = "#000000", fg = "#FFFFFF",
    activebackground="#000000",
    activeforeground="#4269b8",
    image=image,
    command=clicked)
btn.grid(column=0, row=0, sticky="w")

print("_DEVICE INITIATED._")
root.mainloop()
