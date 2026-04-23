print("_INITIATING PRESCRIPT DEVICE._")

from tkinter import *
import random
import keyboard
import winsound

disable=False

root = Tk()
root.title("[Device]")
root.iconbitmap("assets/mark.ico")
root.geometry('400x150')
root.config(bg = "black")
root.attributes("-topmost", True)

lbl = Label(root, text = "_Awaiting Input._", wraplength=400, justify="center", font=("Perfect DOS VGA 437", 16), bg = "#000000", fg = "#FFFFFF")
lbl.pack()
frame = Frame(root, bg = "#000000")
frame.pack()
frame.place(x=0,y=90)

glitch_chars = list("█▒░ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

choices = ["JJS","BT","BDGR","8BA","D2"]

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
    "_After attacking, ",
    "_After emoting, ",
    "_After using a voice taunt, ",
    f"_Within the next {random.randint(30, 60)} seconds, ",
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
    "seek death._",
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
    "attack a player._",
    "aurafarm._",
    "surrender._"
]
prescript_bt1 = [
    f"_At {random.randint(1, 4)} NRG, ",
    "_After landing an attack, ",
    "_As soon as possible, ",
    "_Next turn, ",
    f"_Within the next {random.randint(30, 60)} seconds, ",
    f"_After {random.randint(1, 20)} seconds, ",
    "_After being hit, ",
    "_Before next engagement, ",
    "_Without retreating, ",
    "_Without evading, ",
    "_Without blocking, ",
    "_Without attacking, ",
    "_Without using items, ",
]
prescript_bt2 = [
    "perform a base attack on target #1._",
    "perform a base attack on target #2._",
    "perform a base attack on target #3._",
    "perform a base attack on target #4._",
    "perform a base attack._",
    "use dynamite on target #1._",
    "use dynamite on target #2._",
    "use dynamite on target #3._",
    "use dynamite on target #4._",
    "use dynamite._",
    "use ghost potion._",
    "use shovel on target #1._",
    "use shovel on target #2._",
    "use shovel on target #3._",
    "use shovel on target #4._",
    "use shovel._",
    "evade an attack._",
    "retreat._",
    "defend._",
    "focus._",
    "use an item on player #1._",
    "use an item on player #2._",
    "use an item on player #3._",
    "use an item on player #4._",
    "use an item on any player._",
    "heal any player._",
    "heal player #1._",
    "heal player #2._",
    "heal player #3._",
    "heal player #4._",
    "use a strategy option._",
    "use any special action._",
    "use any special._",
    "use special #1._",
    "use special #2._",
    "use special #3._",
    "use special #4._",
    "next action must target player #1._",
    "next action must target player #2._",
    "next action must target player #3._",
    "next action must target player #4._",
    "next action must target enemy #1._",
    "next action must target enemy #2._",
    "next action must target enemy #3._",
    "next action must target enemy #4._",
    "kill enemy #1._",
    "kill enemy #2._",
    "kill enemy #3._",
    "kill enemy #4._",
    "cease all actions for the turn._",
    "offer a greeting._",
    "bid farewell._",
    "ask a question._",
    "provide an answer._",
    "repeat last prescript command._",
    "recite the first 5 digits of e._",
    "act silly._",
    "act uncertain._",
    "send an expression._",
    "provide a rating._",
    "say a one liner._",
    "enter a combat encounter._",
    "allow an enemy to hit you._",
    "seek death._",
    "pass turn._"
]
prescript_bdgr1 = [
    f"_After {random.randint(1, 20)} seconds, ",
    "_After being attacked, ",
    "_Before next engagement, ",
    "_After being ragdolled, ",
    "_After rolling, ",
    "_After dying, ",
    "_After landing a hit, ",
    "_After using occular prowess, ",
    "_As soon as possible, ",
    "_After attacking, ",
    "_After speaking, ",
    f"_Within the next {random.randint(30, 120)} seconds, ",
    "_Without side-dashing, ",
    "_Without using a throwable, ",
    "_Without dying, ",
    "_Without jumping, ",
    "_Without retreating, ",
    "_Without reloading, ",
    "_Without activating stand, ",
    "_Without moving, ",
    "_Without eating or drinking, ",
    "_Without using ocular prowess, "
]
prescript_bdgr2 = [
    "kill a player._",
    "jump on a player's head._",
    "land a headshot._",
    "seek death._",
    f"cease movement for {random.randint(1, 20)} seconds._",
    "advance to melee distance._",
    "mirror a player's last action._",
    "repeat last prescript command._",
    "delay next attack._",
    "ragdoll a player._",
    f"stop attacking for {random.randint(1, 20)} seconds._",
    f"stay alive for {random.randint(1, 20)} seconds._",
    "eat/drink._",
    "empty chamber of gun #1._",
    "empty chamber of gun #2._",
    "reload._",
    "offer a greeting._",
    "recite the first 5 digits of e._",
    "get on your horse._",
    "get off your horse._",
    "reposition behind a player._",
    "circle a player._",
    f"play passive for {random.randint(1, 20)} seconds._",
    "assume disadvantage._",
    "say a one-liner._",
    "avoid an attack._",
    "side-dash._",
    "roll._",
    "land a shot on a coin._",
    "land any ranged attack._",
    "land any melee attack._",
    "attack a player._",
    "toss a coin._",
    "reload._",
    "use an explosive._",
    "use dynamite._",
    "use an ammo pack._",
    "catch a fish._",
    "surrender._"
]
prescript_d2 = [
    "_Proceed._",
    "_Cease._"
]
prescript_8ba = [
    "_The prescript permits this action._",
    "_The prescript forbids it._",
    "_The answer is known already._",
    "_Do not deviate. Correct your course._",
    "_The outcome is acceptable._",
    "_Proceed. Do not hesitate._",
    "_Insuficient data. Await further instruction._",
    "_The path is unclear._",
    "_You are being tested. Choose carefully._",
    "_Compliance increases survival probability._",
    "_Noncompliance will be recorded._",
    "_The answer is yes._",
    "_No. Do not ask again._",
    "_A better question exists._",
    "_This action aligns with the prescript's will._",
    "_No comment._",
    "_Delay. Timing is not yet correct._",
    "_Immediate action required._",
    "_You are not authorized the answer._",
    "_The result has already been decided._"
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
    print("_PRESCRIPT REQUESTED._")
    if disable == True:
        return
    disable = True
    btn.config(state=DISABLED)
    drp.config(state=DISABLED)
    winsound.PlaySound("assets/index_message_2.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    intermission = "_Please wait._"
    cv = context.get()
    if cv == "8BA" or "D2":
        delay = random.randint(1000, 5000)
        glitch_text(intermission)
    elif cv == "JJS":
        delay = random.randint(1000, 60000)
        glitch_text(intermission)
    elif cv == "BDGR":
        delay = random.randint(1000, 120000)
        glitch_text(intermission)
    elif cv == "BT":
        delay = random.randint(1000, 30000)
        glitch_text(intermission)
    root.after(delay, initiate_prescript)

def initiate_prescript():
    global disable
    disable = False
    winsound.PlaySound("assets/index_message_1.wav", winsound.SND_ASYNC)
    btn.config(state="normal")
    drp.config(state="normal")
    cv = context.get()
    if cv == "JJS":
        result1 = random.choice(prescript_jjs1)
        result2 = random.choice(prescript_jjs2)
        prescript = f"{result1}{result2}"
    elif cv == "BT":
        result1 = random.choice(prescript_bt1)
        result2 = random.choice(prescript_bt2)
        prescript = f"{result1}{result2}"
    elif cv == "BDGR":
        result1 = random.choice(prescript_bdgr1)
        result2 = random.choice(prescript_bdgr2)
        prescript = f"{result1}{result2}"
    elif cv == "8BA":
        result = random.choice(prescript_8ba)
        prescript = f"{result}"
    elif cv == "D2":
        result = random.choice(prescript_d2)
        prescript = f"{result}"
    glitch_text(prescript)
    print("_PRESCRIPT RETURNED._")
        

keyboard.add_hotkey("ctrl+f", clicked)
btn = Button(frame, text = "[+]", 
    font=("Perfect DOS VGA 437", 25), 
    bg = "#000000", fg = "#FFFFFF",
    activebackground="#000000",
    activeforeground="#4269b8",
    command=clicked)
btn.pack(side="left")

context = StringVar()
context.set("JJS")

drp = OptionMenu(frame, context, *choices)
drp.config(font=("Perfect DOS VGA 437", 25), 
    bg = "#000000", fg = "#FFFFFF",
    activebackground="#000000",
    activeforeground="#4269b8")
drp.pack(side="right")

print("_DEVICE INITIATED._")
root.mainloop()
