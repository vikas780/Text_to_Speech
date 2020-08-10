from gtts import gTTS
from tkinter import *
import playsound
import os

txt =""
txt2 = ""

language_code = ["en","hi","af","ja","fr-ca","ko","pl","tr"]
def clicked():
    myob = gTTS(text=txt.get(), lang=variable1.get(),slow=False)
    myob.save("Speech.mp3")
    playsound.playsound("Speech.mp3",True)


window = Tk()
window.title("Text to Speech")
window.geometry('600x400')

variable1 =StringVar(window)
variable1.set("Select-lang")

lbl2 =Label(window, text="Text to Speech",font=('lato black',17,'bold'),fg="blue")
lbl2.grid(column=0,row=0)
lbl2 =Label(window, text="Using Python",font=('lato black',17,'bold'),fg="blue")
lbl2.grid(column=0,row=1)

lbl2 =Label(window, text="",font=('lato black',20,'bold'),fg="red")
lbl2.grid(column=0,row=2)

lbl2 =Label(window, text="Enter Text",font=('lato black',12,'bold'))
lbl2.grid(column=0,row=3)

txt =Entry(window, textvariable=txt ,font=('lato black',12,'normal'))
txt.grid(column=1,row=3)

lbl2 =Label(window, text="Select language" ,font=('lato black',12,'bold'))
lbl2.grid(column=0,row=4)

txt2 = OptionMenu(window, variable1, *language_code)
txt2.grid(column=1,row=4)

lbl2 =Label(window, text="" ,font=('lato black',12,'bold'))
lbl2.grid(column=0,row=5)

btn =Button(window, font=('lato',13, 'bold'),text="play Sound",padx=2,pady=2,bg="red",fg="white",command=clicked)
btn.grid(column=0,row=6)

window.mainloop()
