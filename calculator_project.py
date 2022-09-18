#imports
import tkinter as tk



#initialize variables
num_list_one=[]
opperator_list=[]
num_list_two=[]
opperator=False
result=0
string_one=''
string_two=''
opp_string=''
answer=0


#function that concatenates integers together into one.
def integer_one(digit_one):

    num_list_one.append(digit_one)
    display.config(text=num_list_one)
   

#function that takes operation symbol and puts it onto the display
def operation(opp):
    global num_list_one
    global opperator
    opperator_list.append(opp)
    display.config(text=num_list_one+opperator_list)
    opperator=True

#function that concatenates the first number, operator, and second number onto the screen
def integer_two(digit_two):
    global num_list_one
    global opperator_list
    num_list_two.append(digit_two)
    display.config(text=num_list_one+opperator_list+num_list_two)
    






#create funtions for all buttons if the opperator hasn't been typed the numbers go to the first integer, if there is an opperator the numbers go to the second integer
def seven():
    if opperator==False:
        integer_one(7)
    if opperator==True:
        integer_two(7)
def four():
    if opperator==False:
        integer_one(4)
    if opperator==True:
        integer_two(4)
def one():
    if opperator==False:
        integer_one(1)
    if opperator==True:
        integer_two(1)
def eight():
    if opperator==False:
        integer_one(8)
    if opperator==True:
        integer_two(8)
def five():
    if opperator==False:
        integer_one(5)
    if opperator==True:
        integer_two(5)
def two():
    if opperator==False:
        integer_one(2)
    if opperator==True:
        integer_two(2)
def nine():
    if opperator==False:
        integer_one(9)
    if opperator==True:
        integer_two(9)
def six():
    if opperator==False:
        integer_one(6)
    if opperator==True:
        integer_two(6)
def three():
    if opperator==False:
        integer_one(3)
    if opperator==True:
        integer_two(3)
def zero():
    if opperator==False:
        integer_one(0)
    if opperator==True:
        integer_two(0)
    
#function that clears the screen and resets all values.
def clear():
    global num_list_one
    global num_list_two
    global opperator_list
    global result
    global opperator
    global string_one
    global string_two
    global opp_string
    display.config(text="")
    num_list_one=[]
    opperator_list=[]
    num_list_two=[]
    opperator=False
    result=0
    string_one=''
    string_two=''
    opp_string=''

#functions for the opperations
def subtract():
    operation("-")
def add():
    operation("+")
def division():
    operation("/")
def multiplication():
    operation("X")

#function that passes the numbers and opperator to a result function.
def enter():
    result_function(num_list_one, opperator_list, num_list_two)

#function that calculates the result of the operation.
def result_function(integerone, opperator, integertwo):
    global result
    global string_one
    global string_two
    global opp_string
    global num_list_one
    global opperator_list
    global num_list_two
    global result

    #for loops that turn the lists into integers.
    for i in integerone:
        string_one= string_one + str(i)
        int_one=int(string_one)
    for i in opperator:
        opp_string=opp_string+ str(i)
        opp=str(opp_string)
    for i in integertwo:
        string_two=string_two+ str(i)
        int_two=int(string_two)
    #if statements that do the calculations
    if (opp)=="+":
        result=(int_one + int_two)
    if (opp)=="-":
        result=(int_one - int_two)
    if (opp)=="/":
        result=(int_one / int_two)
    if (opp)=="X":
        result=(int_one * int_two)
    display.config(text=result)
    
    
    


    

    


    










#create a window
root=tk.Tk()
root.wm_geometry("400x400")
root.title("calculator app")

#create a frame
frame_main=tk.Frame(root)
frame_main.grid(sticky="news")

#create a label to show the results.
display=tk.Label(frame_main, text= "please input a function",bg="grey", bd=10, width=30)
display.pack()

#create buttons for claculator
btn_seven=tk.Button(frame_main, text="7", bg="grey", bd=8, command=seven)
btn_seven.place(x=65,y=38)

btn_four=tk.Button(frame_main,text="4", bg="grey", bd=8, command=four)
btn_four.place(x=65,y=78)

btn_one=tk.Button(frame_main, text="1", bg="grey", bd=8, command=one)
btn_one.place(x=65, y=113)

btn_eight=tk.Button(frame_main, text="8", bg="grey", bd=8, command=eight)
btn_eight.pack()

btn_five=tk.Button(frame_main, text="5", bg="grey", bd=8, command=five)
btn_five.pack()

btn_two=tk.Button(frame_main,text='2', bg="grey", bd=8, command=two )
btn_two.pack()

btn_enter=tk.Button(frame_main, text="enter", bd=5, bg="grey",command=enter)
btn_enter.pack(padx=10)

btn_nine=tk.Button(frame_main, text="9", bg="grey", bd=8, command=nine)
btn_nine.place(x=140,y=38)

btn_six=tk.Button(frame_main, text="6", bg="grey", bd=8, command=six)
btn_six.place(x=140,y=78)

btn_three=tk.Button(frame_main, text="3", bg="grey", bd=8, command=three)
btn_three.place(x=140,y=113)


btn_zero=tk.Button(frame_main, text="0", bg="grey", bd=8, command=zero)
btn_zero.place(x=65,y=150)

btn_clear=tk.Button(frame_main, text="CLEAR", bg="grey", bd=8, command=clear)
btn_clear.place(x=0,y=150)

btn_add=tk.Button(frame_main, text="+", bg="grey", bd=8, command=add)
btn_add.place(x=175,y=150)

btn_divide=tk.Button(frame_main, text="/ ", bg="grey", bd=8, command=division)
btn_divide.place(x=175,y=38)

btn_multi=tk.Button(frame_main, text="X", bg="grey", bd=8, command=multiplication)
btn_multi.place(x=175,y=78)

btn_sub=tk.Button(frame_main, text="- ", bg="grey", bd=8, command=subtract)
btn_sub.place(x=175,y=113)




root.mainloop()
