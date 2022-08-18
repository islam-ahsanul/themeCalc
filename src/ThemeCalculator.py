from tkinter import *


class CalcApp:

    def __init__(self):
        self.expression = ""
        self.input_text = StringVar()

    def btn_click(self, item):
        self.expression = self.expression+str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression = ""


class MainClass(CalcApp):
    def main_method(self, mywindow,c1, c2, c3):
        # self.expression = ""
        # self.input_text = StringVar()

        input_frame = Frame(mywindow, width=312, height=50, bd=0, bg="white", highlightbackground="white", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=TOP)

        input_field = Entry(input_frame, font=('Century Gothic', 18, 'bold'),fg="black", textvariable=self.input_text, width=50,bg="white", bd=0, justify=RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = Frame(mywindow, width=312, height=272.5, bg="white")
        btns_frame.pack()

        clear = Button(btns_frame, text="C",fg=c3,width=32, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = Button(btns_frame, text="/", fg=c3, width=10, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_click("/")).grid(row=0, column=3, padx=1,pady=1)
        seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
        eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
        nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
        multiply = Button(btns_frame, text="*", fg=c3, width=10, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
        four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
        five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
        six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
        minus = Button(btns_frame, text="-", fg=c3, width=10, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
        one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
        two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
        three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
        plus = Button(btns_frame, text="+", fg=c3, width=10, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
        zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg=c2, cursor="hand2", command=lambda: w1.btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = Button(btns_frame, text=".", fg=c3, width=10, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
        equals = Button(btns_frame, text="=", fg=c3, width=10, height=3, bd=0, bg=c1, cursor="hand2", command=lambda: w1.btn_equal()).grid(row=4, column=3, padx=1, pady=1)


window = Tk()
w1 = MainClass()
window.geometry("312x344")
window.resizable(0, 0)
window.title("Calculator")
window.iconbitmap("calc3.ico")


def callofduty(c1,c2, c3):
    col1=c1
    col2=c2
    col3=c3
    w1.main_method(window,col1,col2,col3)


menubar = Menu(window)
window.config(menu=menubar)


settingsMenu = Menu(menubar)
themeMenu = Menu(settingsMenu)
themeMenu.add_command(label="Purple", activebackground="#4E387E", command=lambda: callofduty("#4E387E", "#FDEEFA", "#FFFFFF"))
themeMenu.add_command(label="Blue", activebackground="#368BC1", command=lambda: callofduty("#368BC1", "#FFFFFF", "#FFFFFF"))
themeMenu.add_command(label="Aqua", activeforeground="black", activebackground="#50EBEC", command=lambda: callofduty("#50EBEC", "#FFFFFF", "#000000"))
themeMenu.add_command(label="Olive", activeforeground="black", activebackground="#CCFB5D", command=lambda: callofduty("#CCFB5D", "#FFFFFF", "#000000"))
themeMenu.add_command(label="Magenta", activebackground="#800060", command=lambda: callofduty("#800060", "#FFFFFF", "#FFFFFF"))
themeMenu.add_command(label="Light Orange", activeforeground="black", activebackground="#ffe4b3", command=lambda: callofduty("#ffe4b3", "#FFFFFF", "#000000"))
themeMenu.add_command(label="Mint", activeforeground="black", activebackground="#ccffe6", command=lambda: callofduty("#ccffe6", "#FFFFFF", "#1c6352"))
themeMenu.add_command(label="Grey", activeforeground="black", activebackground="#CCD1D9", command=lambda: callofduty("#E6E9ED", "#FFFFFF", "#656D78"))
themeMenu.add_command(label="Grape", activebackground="#666699", command=lambda: callofduty("#666699", "#FFFFFF", "#FFFFFF"))
settingsMenu.add_cascade(label="Themes", menu=themeMenu)

menubar.add_cascade(label="Select Theme", menu=settingsMenu)

# start_buttonFrame = Frame(window)
# start_buttonFrame.pack()
# btn1 = Button(start_buttonFrame, text="Purple Theme", command=lambda:callofduty("#4E387E", "#FDEEFA")).grid(row=0,column=0)
# btn2 = Button(start_buttonFrame, text="Blue Theme",command=lambda:callofduty("#151B54","#FFFFFF")).grid(row=0, column=1)
# btn3 = Button(start_buttonFrame, text="Green Theme",command=lambda:callofduty("#50EBEC","#FFFFFF")).grid(row=0, column=2)

window.mainloop()
