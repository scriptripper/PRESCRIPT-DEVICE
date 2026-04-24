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

choices = ["LCB","LCCB","8BA","D2","JJS","BT","BDGR"]

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
    f"_Without using move {random.randint(1, 4)}, ",
    "_Without activating awakening, ",
    "_Without moving, "

]
prescript_jjs2 = [
    "eliminate a player._",
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
    f"land move {random.randint(1, 4)}._",
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
    f"perform a base attack on target #{random.randint(1, 4)}._",
    "perform a base attack._",
    f"use dynamite on target #{random.randint(1, 4)}._",
    "use dynamite._",
    "use ghost potion._",
    f"use shovel on target #{random.randint(1, 4)}._",
    "use shovel._",
    "evade an attack._",
    "retreat._",
    "defend._",
    "focus._",
    f"use an item on player #{random.randint(1, 4)}._",
    "use an item on any player._",
    "heal any player._",
    f"heal player #{random.randint(1, 4)}._",
    "use a strategy option._",
    "use any special action._",
    "use any special._",
    f"use special #{random.randint(1, 4)}._",
    f"next action must target player #{random.randint(1, 4)}._",
    f"next action must target enemy #{random.randint(1, 4)}._",
    f"eliminate enemy #{random.randint(1, 4)}._",
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
    "eliminate a player._",
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
    f"empty chamber of gun #{random.randint(1, 2)}._",
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
prescript_lccb = [
    "_Use all identities from The Index._",
    "_Use only burn identities._",
    "_Use only bleed identities._",
    "_Use only tremor identities._",
    "_Use only rupture identities._",
    "_Use only sinking identities._",
    "_Use only poise identities._",
    "_Use only charge identities._",
    "_Use all bloodfiend identities._",
    "_Use all identities from The Kurokumo Clan._",
    "_Use all identities from Blade Lineage._",
    "_Use all identities from Wuthering Heights._",
    "_Use only LCB Sinner identities._",
    "_Use all identities from Lobotomy Corporation._",
    "_Use all identities from N Corp._",
    "_Use all identities from The Fingers._",
    "_Use all identities from The Middle._",
    "_Use all identities from Walpurgis._",
    "_Use all identities from R Corp._",
    "_Use all identities from the Dieci Association._",
    "_Use all identities from H Corp._",
    "_Use all identities from The Ring._",
    "_Use all identities from W Corp._",
    "_Use only bad ending identities._",
    "_Use all identities from the Zwei Association._",
    "_Use all identities from the Great Lake._",
    f"_Use only season {random.randint(1, 7)} identities._"

]
prescript_lc1 = [
    f"_After winning a clash with unit #{random.randint(1, 7)}, ",
    f"_After losing a clash with unit #{random.randint(1, 7)}, ",
    "_After winning any clash, ",
    "_After losing any clash, ",
    f"_After {random.randint(2, 5)} turns, ",
    "_Next turn, ",
    f"_After rolling heads with unit #{random.randint(1, 7)}, ",
    f"_After rolling tails with unit #{random.randint(1, 7)}, ",
    "_After a unit dies, ",
    "_After landing a hit, ",
    "_After using a defense skill, ",
    "_As soon as possible, ",
    "_Next turn, ",
    "_After a unit gets staggered, ",
    f"_After unit #{random.randint(1, 7)} gets staggered, ",
    f"_Within the next {random.randint(1, 5)} turns, ",
    "_Without any units getting staggered, ",
    f"_Without unit #{random.randint(1, 7)} getting staggered, ",
    "_Without any units dying, ",
    f"_Without unit unit #{random.randint(1, 7)} dying, ",
    f"_Without unit #{random.randint(1, 7)} attacking, ",
    "_Without restarting the encounter, ",
    "_Next encounter, ",
    f"_Without using any skill {random.randint(1, 3)}s, ",
    f"_Without unit #{random.randint(1, 7)} using skill {random.randint(1, 3)}, ",
    "_Without targeting an enemy's core, ",
    "_While only targeting an enemy's core, ",
    "_Without rolling tails, ",
    f"_Without unit #{random.randint(1, 7)} rolling heads, ",
    f"_Without unit #{random.randint(1, 7)} rolling tails, ",
    "_Without using any E.G.O skills, ",
    f"_Without using unit #{random.randint(1, 7)}'s E.G.O skills, ",
    "_Without using a Zayin E.G.O, ",
    "_Without using a Teth E.G.O, ",
    "_Without using a He E.G.O, ",
    "_Without using a Waw E.G.O, ",
    f"_Without using unit #{random.randint(1, 7)}'s Zayin E.G.O, ",
    f"_Without using unit #{random.randint(1, 7)}'s Teth E.G.O, ",
    f"_Without using unit #{random.randint(1, 7)}'s He E.G.O, ",
    f"_Without using unit #{random.randint(1, 7)}'s Waw E.G.O, ",
]
prescript_lc2 = [
    f"use unit #{random.randint(1, 7)}'s skill {random.randint(1, 3)}._",
    f"use unit #{random.randint(1, 7)}'s defense skill._",
    "eliminate an enemy._",
    "stagger an enemy._",
    "eliminate any unit._",
    "stagger any unit._",
    "eliminate any ally._",
    "stagger any ally._",
    f"eliminate unit #{random.randint(1, 7)}._",
    f"stagger unit #{random.randint(1, 7)}._",
    "use a Zayin E.G.O._",
    "use a Teth E.G.O._",
    "use a He E.G.O._",
    "use a Waw E.G.O._",
    f"use unit #{random.randint(1, 7)}'s Zayin E.G.O._",
    f"use unit #{random.randint(1, 7)}'s Teth E.G.O._",
    f"use unit #{random.randint(1, 7)}'s He E.G.O._",
    f"use unit #{random.randint(1, 7)}'s Waw E.G.O._",
    "stagger or eliminate an enemy._",
    "stagger or eliminate all enemies._",
    "eliminate all enemies._",
    f"form a {random.randint(2, 7)}x sin resonance._",
    f"form a {random.randint(2, 4)}x sin resonance._",
    "form any sin resonance._",
    "form an absolute resonance._",
    f"form a {random.randint(2, 7)}x absolute resonance._",
    f"form a {random.randint(2, 4)}x absolute resonance._",
    "repeat last prescript command._",
    "target the slowest enemy with any unit._",
    f"target the slowest enemy with unit #{random.randint(1, 7)}._",
    "target the fastest enemy with any unit._",
    f"target the fastest enemy with unit #{random.randint(1, 7)}._",
    "target the enemy with the least HP with any unit._",
    f"target the enemy with the least HP with unit #{random.randint(1, 7)}._",
    "target the enemy with the most HP with any unit._",
    f"target the enemy with the most HP with unit #{random.randint(1, 7)}._",
    "target the slowest enemy with the unit with the least HP._",
    "target the slowest enemy with the unit with the most HP._",
    "target the fastest enemy with the unit with the least HP._",
    "target the fastest enemy with the unit with the most HP._",
    "target the enemy with the least HP with the unit with the least HP._",
    "target the enemy with the least HP with the unit with the most HP._",
    "target the enemy with the most HP with the unit with the least HP._",
    "target the enemy with the most HP with the unit with the most HP._",
    "perform an unopposed attack against an enemy._",
    f"perform an unopposed attack against an enemy with unit {random.randint(1, 7)}._",
    "use the winrate button._",
    "use the damage button._"

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
    "_Compliance increases odds._",
    "_Noncompliance will be recorded._",
    "_The answer is yes._",
    "_No. Do not ask again._",
    "_There is a better question._",
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
    elif cv == "LCB" or "LCCB":
        delay = random.randint(1000, 15000)
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
    elif cv == "LCB":
        result1 = random.choice(prescript_lc1)
        result2 = random.choice(prescript_lc2)
        prescript = f"{result1}{result2}"
    elif cv == "LCCB":
        result = random.choice(prescript_lccb)
        prescript = f"{result}"
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
context.set("LCB")

drp = OptionMenu(frame, context, *choices)
drp.config(font=("Perfect DOS VGA 437", 25), 
    bg = "#000000", fg = "#FFFFFF",
    activebackground="#000000",
    activeforeground="#4269b8")
drp.pack(side="right")

print("_DEVICE INITIATED._")
root.mainloop()
