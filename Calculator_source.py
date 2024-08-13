from tkinter import *

root = Tk()
root.configure(bg="#000000")
root.title(" Calculator")
root.iconbitmap('d:\G\Calc\calculator2.ico')

e = Entry(root, width=30, borderwidth=5, bg="#000000", fg="#FFFFFF")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Initialize global variables
f_num = 0
math = ""

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    # Check if math is set
    if math == "addition":
        e.insert(0, f_num + float(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))

    elif math == "division":
        e.insert(0, f_num / float(second_number))

    elif math == "fraction":
        e.insert(0, 1 / f_num)
        
    elif math == "squared":
        e.insert(0, f_num * f_num)
        
    elif math == "square_root":
        e.insert(0, f_num ** 0.5)
        
    elif math == "percentage":
        e.insert(0, f_num / 100)
        
    else:
        e.insert(0, "Error")

def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, END)

def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = float(first_number)
    e.delete(0, END)

def button_squared():
    first_number = e.get()
    global f_num
    global math
    math = "squared"
    f_num = float(first_number)
    e.delete(0, END)

def button_fraction():
    first_number = e.get()
    global f_num
    global math
    math = "fraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

# Define buttons
button_1 = Button(root, text="1", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=32, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=32, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=32, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=73, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click(0))
button_point = Button(root, text=".", padx=34, pady=20, bg="#000000", fg="#FFFFFF", command=lambda: button_click('.'))

# Line 1
button_fraction = Button(root, text="1\n-\nx", padx=33, pady=5, bg="#000000", fg="#FFFFFF", command=button_fraction)		#DONE
button_squared = Button(root, text="x\u00B2", padx=30, pady=20, bg="#000000", fg="#FFFFFF", command=button_squared)
button_square_root = Button(root, text="\u221Ax", padx=30, pady=20, bg="#000000", fg="#FFFFFF", command=button_square_root)
button_percentage = Button(root, text="%", padx=30, pady=20, bg="#000000", fg="#FFFFFF", command=button_percentage)

# Line 2
button_clear = Button(root, text="C", padx=32, pady=20, bg="#000000", fg="#FFFFFF", command=button_clear)					#DONE
button_divide = Button(root, text="/", padx=33, pady=20, bg="#000000", fg="#FFFFFF", command=button_divide)					#DONE
button_multiply = Button(root, text="*", padx=34, pady=20, bg="#000000", fg="#FFFFFF", command=button_multiply)				#DONE
button_subtract = Button(root, text="-", padx=32, pady=20, bg="#000000", fg="#FFFFFF", command=button_subtract)				#DONE

# Side
button_addition = Button(root, text="+", padx=32, pady=54, bg="#000000", fg="#FFFFFF", command=button_add)					#DONE
button_equal = Button(root, text="=", padx=32, pady=54, bg="#000000", fg="#FFFFFF", command=button_equal)					#DONE

# Grid layout
# Line 1
button_fraction.grid(row=1, column=0)
button_squared.grid(row=1, column=1)
button_square_root.grid(row=1, column=2)
button_percentage.grid(row=1, column=3)

# Line 2
button_clear.grid(row=2, column=0)
button_divide.grid(row=2, column=1)
button_multiply.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

# Line 3
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

# Line 4
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

# Line 5
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

# Line 6
button_0.grid(row=6, column=0, columnspan=2)
button_point.grid(row=6, column=2)

# Side buttons
button_addition.grid(row=3, column=3, rowspan=2)
button_equal.grid(row=5, column=3, rowspan=2)

root.mainloop()
