import tkinter
import MyCalculator as cal

sqrt = cal.sqrt
sin = cal.sin
cos = cal.cos
tan = cal.tan
fact = cal.fact
mod = cal.mod
pow = cal.pow


class CalculatorClass:

    def AC(self):
        global expression
        self.expression = ""
        self.equation.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def exit(self):
        self.parent.destroy()

    def click(self,btn):
        global expression
        self.expression = self.expression + str(btn)
        self.equation.set(self.expression)

    def equals(self):

        try:
            self.ans = str(eval(self.expression))
            self.equation.set(self.ans)
            self.expression = self.ans
        except:
            self.equation.set("error")

    def __init__(self, parent):
        self.parent = parent
        self.expression = " "
        self.ans = ""
        self.frame = tkinter.Frame(parent, bg="black")
        self.frame.pack()
        self.equation = tkinter.StringVar()
        self.equation.set("")
        self.label = tkinter.Label(self.frame,textvariable = self.equation,font = "arial",height = 3)
        self.label.pack()
        self.frame1 = tkinter.Frame(self.parent)
        self.frame1.pack()
        self.button = tkinter.Button(self.frame1,text = 'sqrt',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("sqrt("))
        self.button.grid(row = 0,column = 0)
        self.button = tkinter.Button(self.frame1,text = 'sin',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("sin("))
        self.button.grid(row = 0,column = 1)
        self.button = tkinter.Button(self.frame1,text = 'cos',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("cos("))
        self.button.grid(row = 0,column = 2)
        self.button = tkinter.Button(self.frame1,text = 'tan',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("tan("))
        self.button.grid(row = 0,column = 3)
        self.button = tkinter.Button(self.frame1,text = 'fact',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("fact("))
        self.button.grid(row = 1,column = 0)
        self.button = tkinter.Button(self.frame1,text = 'mod',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("mod("))
        self.button.grid(row = 1,column = 1)
        self.button = tkinter.Button(self.frame1,text = '(',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("("))
        self.button.grid(row = 1,column = 2)
        self.button = tkinter.Button(self.frame1,text = ')',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click(")"))
        self.button.grid(row = 1,column = 3)
        self.button = tkinter.Button(self.frame1,text = 'AC',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = self.AC)
        self.button.grid(row = 2,column = 0)
        self.button = tkinter.Button(self.frame1,text = 'del',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = self.backspace)
        self.button.grid(row = 2,column = 1)
        self.button = tkinter.Button(self.frame1,text = 'pow',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("pow("))
        self.button.grid(row = 2,column = 2)
        self.button = tkinter.Button(self.frame1,text = '/',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("/"))
        self.button.grid(row = 2,column = 3)
        self.button = tkinter.Button(self.frame1,text = '7',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(7))
        self.button.grid(row = 3,column = 0)
        self.button = tkinter.Button(self.frame1,text = '8',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(8))
        self.button.grid(row = 3,column = 1)
        self.button = tkinter.Button(self.frame1,text = '9',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(9))
        self.button.grid(row = 3,column = 2)
        self.button = tkinter.Button(self.frame1,text = '*',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("*"))
        self.button.grid(row = 3,column = 3)
        self.button = tkinter.Button(self.frame1,text = '4',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(4))
        self.button.grid(row = 4,column = 0)
        self.button = tkinter.Button(self.frame1,text = '5',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(5))
        self.button.grid(row = 4,column = 1)
        self.button = tkinter.Button(self.frame1,text = '6',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(6))
        self.button.grid(row = 4,column = 2)
        self.button = tkinter.Button(self.frame1,text = '-',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("-"))
        self.button.grid(row = 4,column = 3)
        self.button = tkinter.Button(self.frame1,text = '1',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(1))
        self.button.grid(row = 5,column = 0)
        self.button = tkinter.Button(self.frame1,text = '2',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(2))
        self.button.grid(row = 5,column = 1)
        self.button = tkinter.Button(self.frame1,text = '3',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(3))
        self.button.grid(row = 5,column = 2)
        self.button = tkinter.Button(self.frame1,text = '+',font = "arial",height = 2,width = 8,fg="black",bg="light blue",command = lambda: self.click("+")) 
        self.button.grid(row = 5,column = 3)
        self.button = tkinter.Button(self.frame1,text = '.',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click("."))
        self.button.grid(row = 6,column = 0)
        self.button = tkinter.Button(self.frame1,text = '0',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(0))
        self.button.grid(row = 6,column = 1)
        self.button = tkinter.Button(self.frame1,text = ',',font = "arial",height = 2,width = 8,fg="black",bg="white",command = lambda: self.click(","))
        self.button.grid(row = 6,column = 2)
        self.button = tkinter.Button(self.frame1,text = '=',font = "arial",height = 2,width = 8,fg="white",bg="red",command = self.equals)
        self.button.grid(row = 6,column = 3)
        self.button = tkinter.Button(self.frame1,text = 'quit',font = "arial",height = 1,width = 34,fg="white",bg="grey",command = self.exit)
        self.button.grid(row = 7,columnspan=4)
        

        

if __name__ == '__main__':
    window = tkinter.Tk()
    mycal = CalculatorClass(window)
    #frame.pack()
    window.title('My Calculator')   
    #window.geometry("250x500")
    window.mainloop()