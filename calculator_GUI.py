#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kashi
#
# Created:     04-10-2023
# Copyright:   (c) kashi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import tkinter.messagebox



#button function----------->
def btnclick(number):
    global val
    val = val + str(number)
    data.set(val)

def clear():
    global val
    val = ''
    data.set('')

def equal():
    global val
    result = str(eval(val))
    data.set(result)



window = Tk()
window.title('Calculator')
window.geometry('361x381+500+200')
#window.resizable(FALSE , FALSE)

val = ''
data = StringVar()


#display where all the calculation are display
display = Entry(window ,bd= 29 ,justify='right' , textvariable= data , bg='black' ,fg='white' , font=('ariel' , 20 , 'bold') )
display.grid(row=0 , columnspan=4)


# button interface------->
nine_button = Button(window , text='9' , height=2 , width=6 , cursor='hand2' ,bg='black',fg='white' ,bd= 12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(9) )
nine_button.grid(row=1 , column=0)

eight_button = Button(window , text='8' , height=2 , width=6 , cursor='hand2', bg='black',fg='white' , bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(8) )
eight_button.grid(row=1 , column=1)

seventh_button = Button(window , text='7' , height=2 , width=6 ,cursor='hand2' , bg='black',fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(7))
seventh_button.grid(row=1 , column=2)

add_button = Button(window , text='+' , height=2 , width=6 ,cursor='hand2', bg='black' ,fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick('+') )
add_button.grid(row=1 , column=3)

sixth_button = Button(window , text='6' , height=2 , width=6 , cursor='hand2' , bg= 'black' ,fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(6) )
sixth_button.grid(row=2 , column=0)

fifth_button = Button(window , text='5' , height=2 , width=6 ,  cursor='hand2' , bg='black' ,fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(5) )
fifth_button.grid(row=2 , column=1)

fourth_button = Button(window , text='4' , height=2 , width=6 , cursor='hand2' , bg='black',fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(4) )
fourth_button.grid(row=2 , column=2)

minus_button = Button(window , text='-' , height=2 , width=6 , cursor='hand2' , bg='black' ,fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold')  , command = lambda: btnclick('-') )
minus_button.grid(row=2 , column=3)

three_button = Button(window , text='3' , height=2 , width=6 ,  cursor='hand2' ,bg='black' ,fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(3) )
three_button.grid(row=3 , column=0)

two_button = Button(window , text='2' , height=2 , width=6 , cursor='hand2' , bg='black',fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(2) )
two_button.grid(row= 3 , column=1)

first_buttton = Button(window, text='1' , height=2 , width=6 ,cursor='hand2' , bg='black',fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick(1) )
first_buttton.grid(row=3 , column=2)

multiply_button = Button(text='*' , height= 2 , width=6 ,cursor='hand2' , bg='black' , fg= 'white',bd=12  ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick('*'))
multiply_button.grid(row=3 , column=3)

clear_button = Button(window , text='C' , height=2 , width=6 , cursor='hand1' ,background='navyblue',fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command= clear)
clear_button.grid(row=4 , column=0)

equal_button = Button(window , text='=' , height=2 , width=6 , cursor='hand2', bg='black',fg='white' , bd=12 ,font=('ariel' , 12 , 'bold') , command = equal)
equal_button.grid(row=4 , column=1)

percent_button = Button(window , text='%' , height=2 , width=6 ,cursor='hand2' , bg='black',fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick('%'))
percent_button.grid(row=4 , column=2)

divide_button = Button(window , text='/' , height=2 , width=6 ,cursor='hand2', bg='black' ,fg='white' ,bd=12 ,font=('ariel' , 12 , 'bold') , command = lambda: btnclick('/'))
divide_button.grid(row=4 , column=3)


window.mainloop()