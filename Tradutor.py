from google_trans_new import google_translator
import pyttsx3
from tkinter import *
from collections import Counter

#OBJETOS
#==================================================================
janela = Tk()
engine = pyttsx3.init()
translator = google_translator()
#==================================================================
x = [] # List
y = [] # List
#Janela
#==================================================================
janela.title('TradutorZ')
janela.iconbitmap('icone.ico')
#==================================================================
#Funções
#==================================================================
def voiceE():
    vdv = txtE.get()
    engine.say(vdv)
    engine.runAndWait()

def voiceP():
    engine.say(x)
    engine.runAndWait()

def traduzir():
    tra =  txtE.get()
    translate_text = translator.translate(tra, lang_tgt='pt')
    voz = translate_text
    x.append(voz)
    lbt["text"] = voz
    print(voz)

#==================================================================
#Entry
#==================================================================
txtE = Entry(janela)
txtE.place(x=30,y=200, width=350, height=100)
txtP = Entry(janela)
txtP.place(x=420,y=200, width=350, height=100)

#==================================================================
#Buttons
#==================================================================
tradu = Button(janela, text='Traduzir', font='sans-serif', width=20, command=traduzir)
tradu.place(x=310, y=330)
voiceE = Button(janela, text='Listen', font='sans-serif',command=voiceE)
voiceE.place(x=30, y=305)
voiceP = Button(janela, text='Listen', font='sans-serif',command=voiceP)
voiceP.place(x=715, y=305)

#==================================================================
#Labels
#==================================================================
lb = Label(janela,text=' Inglês', font='sans-serif')
lb.place(x=180, y=150)

lb2 = Label(janela,text=' Português', font='sans-serif')
lb2.place(x=550, y=150)
logo = PhotoImage(file='logo.png')
lb3 = Label(janela, image=logo)
lb3.place(x=280,y=515)

py = PhotoImage(file='back2.png')
lb4 = Label(janela,image=py)
lb4.place(x=350,y=50)

lb5 = Label(janela, text='1.0')
lb5.place(x=750, y=565)

lbt = Label(janela,text='')
lbt.place(x=425,y=210)
#==================================================================
janela.geometry('800x600')
janela.resizable(width=0,height=0)
janela.mainloop()
# By: Gabriel Reis