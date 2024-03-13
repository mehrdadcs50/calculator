import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculater")
        self.geometry("380x490")
        self.configure(bg="black")
        self.result = tk.Entry(self, font=("Arial", 26))
        self.result.grid(row = 0, column= 0, columnspan= 4, padx=5, pady=5,
                         ipadx=40, ipady= 20, sticky=tk.W + tk.E)
        self.result.config(justify=tk.RIGHT)
        self.result.configure(bg="gray")
        self.grid_columnconfigure(0, weight = 1)
        
        
        button_frame = tk.Frame(self)
        button_frame.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
        button_frame.configure(bg="black")
        
        self.create_button("1", button_frame, 0, 0, lambda: self.add_number(1))
        self.create_button("2", button_frame, 0, 1, lambda: self.add_number(2))
        self.create_button("3", button_frame, 0, 2, lambda: self.add_number(3))
        self.create_button("4", button_frame, 1, 0, lambda: self.add_number(4))
        self.create_button("5", button_frame, 1, 1, lambda: self.add_number(5))
        self.create_button("6", button_frame, 1, 2, lambda: self.add_number(6))
        self.create_button("7", button_frame, 2, 0, lambda: self.add_number(7))
        self.create_button("8", button_frame, 2, 1, lambda: self.add_number(8))
        self.create_button("9", button_frame, 2, 2, lambda: self.add_number(9))
        self.create_button("0", button_frame, 3, 1, lambda: self.add_number(0))
        
        self.create_button("+", button_frame, 0, 3, lambda: self.add_operation("+"))
        self.create_button("-", button_frame, 1, 3, lambda: self.add_operation("-"))
        self.create_button("*", button_frame, 2, 3, lambda: self.add_operation("*"))
        self.create_button("/", button_frame, 3, 3, lambda: self.add_operation("/"))
        
        self.create_button("=", button_frame, 3, 2, self.calculate)
        self.create_button("c", button_frame, 3, 0, self.clear)
        
    def create_button(self, text, frame, row, column, command, bg ="orange"):
        button = tk.Button(frame, text = text, command = command, 
                            font=("Arial", 20), width=5, height=2)
        button.config(bg=bg)
        button.grid(row = row, column = column, padx = 3, pady= 3)
            
        
    def add_number(self, number):
        current = self.result.get()
        current += (str(number))
        self.result.delete(0, tk.END)
        self.result.insert(0, current)
        
    def add_operation(self, operator):
        current = self.result.get()
        current += operator
        self.result.delete(0, tk.END)
        self.result.insert(0, current)
            
    def calculate(self):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, eval(current))
            
    def clear(self):
        self.result.delete(0, tk.END)
            
            
        
if __name__ =="__main__":
    calculator = Calculator()
    calculator.mainloop()