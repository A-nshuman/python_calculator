import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.result_var = tk.StringVar()
        self.result_var.set("")
        
        self.input_field = tk.Entry(self.master, width=30, font=("Arial", 12),
                                    textvariable=self.result_var, justify="right")
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=7, height=2,
                           font=("Arial", 12), command=lambda:self.on_button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def on_button_click(self, text):
        if text == "=":
            self.evaluate_expression()
        elif text == "C":
            self.clear_input()
        else:
            self.input_field.insert(tk.END, text)

    def evaluate_expression(self):
        try:
            result = eval(self.input_field.get())
            self.result_var.set(result)
        except:
            self.result_var.set("Error")

    def clear_input(self):
        self.input_field.delete(0, tk.END)
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
