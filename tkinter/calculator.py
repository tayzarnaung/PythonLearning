import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")

        # btns = [i for i in range(1, 10)]
        btns = [None] * 9
        for i in range(9):
            #     btns = btns or [[]] * 10
            btns[i] = tk.Button(self, text=i + 1, padx=40, pady=20, command=self.btn_add)

        # btn_0= tk.Button(self, text="0", padx=40, pady=20, command=self.btn_add)
        # btn_add = tk.Button(self, text="1", padx=40, pady=20, command=self.btn_add)
        # btn_equal = tk.Button(self, text="1", padx=40, pady=20, command=self.btn_add)
        # btn_clear = tk.Button(self, text="1", padx=40, pady=20, command=self.btn_add)

        index = 2
        for row in range(3):
            for col in range(3):
                try:
                    btns[index].grid(row=row, column=col)
                    index += 1
                except IndexError:
                    return

    def btn_add(self):
        pass


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
