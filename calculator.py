from tkinter import *  # Importing the necessary tkinter modules

first_number = second_number = operator = None  # Initializing variables for storing numbers and operators

def get_digit(digit):  # Function to handle getting digits and updating the result label
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():  # Function to clear the result label
    result_label.config(text='')

def get_operator(op):  # Function to handle getting operators and storing the first number
    global first_number, operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():  # Function to calculate and display the result based on the stored operator and second number
    global first_number, second_number, operator

    second_number = int(result_label['text'])

    if operator == '+':  # Addition
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':  # Subtraction
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':  # Multiplication
        result_label.config(text=str(first_number * second_number))
    else:  # Division
        if second_number == 0:
            result_label.config(text='Error')  # Error for division by zero
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))

root = Tk()  # Creating the main tkinter window
root.title('Calculator')  # Setting the title
root.geometry('280x380')  # Setting the initial window size
root.resizable(0, 0)  # Making the window non-resizable
root.configure(background='black')  # Setting the background color

result_label = Label(root, text='', bg='black', fg='white')  # Creating a label for displaying the result
result_label.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky='w')  # Placing the label on the window
result_label.config(font=('verdana', 30, 'bold'))  # Configuring the label font

# Creating buttons for digits, operators, and other functionalities, and configuring their appearance and behavior
btn7 = Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add = Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))

btn4 = Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_sub = Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))

btn1 = Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_mul = Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))

btn_clr = Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda :clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14))

btn0 = Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_equals = Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('verdana',14))

btn_div = Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))

root.mainloop()
