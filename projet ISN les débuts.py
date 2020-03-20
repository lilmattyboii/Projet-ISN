from tkinter import *
tk=Tk()
can=Canvas(tk, bg='black', height=700, width=1000)
can.pack()

rect = can.create_rectangle(30, 50, 150, 150, fill='lightblue')
disq = can.create_oval(50, 50, 80, 80, width=2, fill='red')
lign = can.create_line(0, 10, 120, 250, width=2, fill='blue')
txt1 = can.create_text(500, 50, text='PACMAN !', fill='blue')














tk.mainloop()
