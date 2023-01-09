import tkinter as tk

win=tk.Tk()
win.title('Введите домашний адресс')

frm_from=tk.Frame(relief=tk.SUNKEN,borderwidth=3)
frm_from.pack()

lbl_firs_name=tk.Label(master=frm_from,text="Имя")
ent_first_name=tk.Entry(master=frm_from,width=50)

win.mainloop()
