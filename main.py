from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import messagebox
from typing import List
import numpy as np
import math
from tkinter import *
from tkinter import ttk
import integtation
import matplotlib

matplotlib.use("TkAgg")


class MainWindow:
    window = Tk()
    window.title('Курсовая работа')
    window.geometry('1500x600')
    X_text_label = LabelFrame(window, text='X')
    X_text = Text(X_text_label, width=40, height=3)
    Y_text_label = LabelFrame(window, text='Y')
    Y_text = Text(Y_text_label, width=40, height=3)

    def read(self):
        try:
            with open("logs.txt", "r") as file:
                self.X_text.delete(1.0, END)
                self.Y_text.delete(1.0, END)
                self.X_text.insert(index='1.0', chars=file.readline())
                self.Y_text.insert(index='1.0', chars=file.readline())
                self.calculate()
                messagebox.showinfo('.', 'Данные получены!')
        except:
            messagebox.showinfo('Ошибка', 'Ошибка чтения данных из файла!!')

    def write(self):
        try:
            with open("logs.txt", "w") as file:
                file.write(self.X_text.get(1.0, END))
                file.write(self.Y_text.get(1.0, END))
                messagebox.showinfo('.', 'Запись прошла успешно!')
        except:
            messagebox.showinfo('Ошибка', 'Ошибка записи в файл!')

    def calculate(self):
        x: List[float] = []
        y: List[float] = []
        try:
            xs = self.X_text.get(1.0, END)
            xs = xs[0:-1].split(' ')
            for i in range(len(xs)):
                x.append(float(xs[i]))
        except:
            messagebox.showinfo('Ошибка', 'Ошибка получения значений из поля X')
        try:
            ys = self.Y_text.get(1.0, END)
            ys = ys[0:-1].split(' ')
            for i in range(len(ys)):
                y.append(float(ys[i]))
        except:
            messagebox.showinfo('Ошибка', 'Ошибка получения значений из поля Y')

        if len(x) == len(y):
            integr = integtation.Integrall(len(x), y, x)
            integr.integrateAll()
            f = Figure(figsize=(6, 4), dpi=120)
            a = f.add_subplot(111)
            a.bar(1, integr.crRectL, label='ЛевыеПрям')
            a.bar(2, integr.crRectM, label='СредниеПрям')
            a.bar(3, integr.crRectR, label='ПравыеПрям')
            a.bar(4, integr.crSimps, label='Симпсон')
            a.bar(5, integr.crTrap, label='Трапеция')
            a.bar(6, integr.cr38, label='3/8')
            a.grid()
            a.legend(loc='lower left')
            canvas = FigureCanvasTkAgg(f)
            canvas.draw()
            canvas._tkcanvas.grid(row=0, column=1, rowspan=40, columnspan=50)

            rows = []
            metod = ['Левых прямоугольников', 'Средних прямоугольников', 'Правых прямоугольников', 'Симпсона', 'Трапеции', '3/8']
            intRes = [integr.crRectL, integr.crRectM, integr.crRectR, integr.crSimps, integr.crTrap, integr.cr38]
            for i in range(len(metod)):
                rows.append((metod[i], intRes[i]))
            columns = ("Метод", "Значение")
            tree = ttk.Treeview(columns=columns, show="headings")
            tree.grid(row=0, column=52, columnspan=20, rowspan=20)
            tree.heading("Метод", text="Метод")
            tree.heading("Значение", text="Значение")
            for row in rows:
                tree.insert("", END, values=row)
        else:
            messagebox.showinfo('Ошибка', 'Количество X должно быть равно количеству Y')

    def create_window(self):
        self.X_text.pack()
        self.X_text_label.grid(row=0, column=0)
        self.X_text.insert(index='1.0', chars='1 3 7 10 11 15 16 19 21 23')

        self.Y_text.pack()
        self.Y_text_label.grid(row=1, column=0)
        self.Y_text.insert(index='1.0', chars='53 1 36 4 93 98 82 45 27 26')

        btnCalculate = Button(self.window, text='Рассчитать', command=self.calculate)
        btnWrite = Button(self.window, text='Записать в файл', command=self.write)
        btnRead = Button(self.window, text='Считать из файла', command=self.read)
        btnCalculate.grid(row=2, column=0)
        btnWrite.grid(row=3, column=0)
        btnRead.grid(row=4, column=0)

        self.window.mainloop()


if __name__ == '__main__':
    win = MainWindow()
    win.create_window()
