from tkinter import *
import time

root = Tk() # создаём окно приложения
root.title('Часы') # название приложения
root.resizable(width=False, height=False) # приложение нельзя растягивать по вертикали и горизонтали

def tick():
    watch.after(1000, tick)
    watch['text'] = time.strftime('%H:%M:%S')

watch = Label(root, font='Arial 100') # шрифт и размер шрифта
watch.pack()
tick()

root.mainloop()