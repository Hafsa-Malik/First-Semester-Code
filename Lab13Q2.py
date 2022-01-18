from tkinter import *
from tkinter.font import BOLD

window=Tk()        						 #creating a window
window.title("                        CALCULATOR")  			#adding window's title
window.geometry("340x380")  					#to set size of window

#to create screen that displays inputs and outputs
text_box=Entry(window, bd=15, bg='sea green', font=("",20))
text_box.grid(row=0,columnspan=4)

#TO CREATE BUTTONS IN SECOND ROW WITH FORMATTING
btn_cls=Button(window, text="Cls" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_cls.grid(row=1 , column=0)
btn_back=Button(window, text="Back" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_back.grid(row=1 , column=1)
btn=Button(window, text="" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn.grid(row=1 , column=2)
btn_close=Button(window, text="Close" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_close.grid(row=1 , column=3)

#TO CREATE BUTTONS IN THIRD ROW WITH FORMATTING
btn7=Button(window, text="7" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn7.grid(row=2 , column=0)
btn8=Button(window, text="8" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn8.grid(row=2 , column=1)
btn9=Button(window, text="9" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn9.grid(row=2 , column=2)
btn_div=Button(window, text="/" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_div.grid(row=2 , column=3)

#TO CREATE BUTTONS IN FOURTH ROW WITH FORMATTING
btn4=Button(window, text="4" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn4.grid(row=3 , column=0)
btn5=Button(window, text="5" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn5.grid(row=3 , column=1)
btn6=Button(window, text="6" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn6.grid(row=3 , column=2)
btn_multi=Button(window, text="*" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_multi.grid(row=3 , column=3)

#TO CREATE BUTTONS IN FIFTH ROW WITH FORMATTING
btn1=Button(window, text="1" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn1.grid(row=4 , column=0)
btn2=Button(window, text="2" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn2.grid(row=4 , column=1)
btn3=Button(window, text="3" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn3.grid(row=4 , column=2)
btn_sub=Button(window, text="-" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_sub.grid(row=4 , column=3)

#TO CREATE BUTTONS IN SIXTH ROW WITH FORMATTING
btn0=Button(window, text="0" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn0.grid(row=5 , column=0)
btn_dot=Button(window, text="." , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_dot.grid(row=5 , column=1)
btn_equal=Button(window, text="=" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_equal.grid(row=5 , column=2)
btn_add=Button(window, text="+" , bd=10 , height=2 , width=6, font=('',10,BOLD))
btn_add.grid(row=5 , column=3)
window.mainloop()
