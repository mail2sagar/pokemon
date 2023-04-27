from tkinter import *
import random
from PIL import ImageTk , Image

window = Tk()

window.title("Pokemon Card Game")
window.geometry("600x400")

window.config(background="dark orange")

button = ImageTk.PhotoImage(Image.open("button.jpg"))

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("button.jpg"))
meowth = ImageTk.PhotoImage(Image.open("button.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("button.jpg"))
paras = ImageTk.PhotoImage(Image.open("button.jpg"))
persion = ImageTk.PhotoImage(Image.open("button.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("button.jpg"))
ratata = ImageTk.PhotoImage(Image.open("button.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("button.jpg"))

pokemon_list = [abra,bulbasour,charmender,iyvasour,jigglypuff,kadabra,meowth,nidoking,paras
                ,persion,pikachu,ratata,squirtle]

power_list = [30,60,50,100,70,70,60,90,40,70,200,40,50]                

label = Label(window)

label1 = Label(window,text="Player 1")
label1.config(background="firebrick1")


label2 = Label(window,text="Player 2")
label2.config(background="firebrick1")

p1_score = Label(window)
p1_score.config(background="DodgerBlue2")

p2_score = Label(window)
p2_score.config(background="DodgerBlue2")

player_1_score = 0

def player1():
    global player_1_score
    random_no = random.randint(0,12)
    random_pokemon = pokemon_list[random_no]
    label["image"] = random_pokemon
    
    random_power_list = power_list[random_no]
    p1_score["text"]= str(player_1_score)

player_2_score = 0

def player2():
    global player_2_score
    random_no = random.randint(0,12)
    random_pokemon = pokemon_list[random_no]
    label["image"] = random_pokemon
    
    random_power_list = power_list[random_no]
    p2_score["text"]= str(player_2_score)

label_result = Label(window)
label_result.config(background="alice blue")

label1.place(relx=0.1,rely=0.3,anchor=CENTER)
label2.place(relx=0.9,rely=0.3,anchor=CENTER)

p1_score.place(relx=0.1,rely=0.4,anchor=CENTER)
p2_score.place(relx=0.9,rely=0.4,anchor=CENTER)


label_result.place(relx=0.5,rely=0.5,anchor=CENTER)

player1_btn = Button(window,image=button,command=player1)

player2_btn = Button(window,image=button,command=player2)

window.mainloop()