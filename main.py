import tkinter as tk

win=tk.Tk()
win.title('Введите домашний адресс')

frm_from=tk.Frame(relief=tk.SUNKEN,borderwidth=3)
frm_from.pack()

lbl_first_name=tk.Label(master=frm_from,text="Имя")
ent_first_name=tk.Entry(master=frm_from,width=50)

lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)

lbl_last_name=tk.Label(master=frm_from,text="Фамилия")
ent_last_name=tk.Entry(master=frm_from,width=50)
lbl_last_name.grid(row=1,column=0,sticky='e')
ent_last_name.grid(row=1,column=1)

lbl_address1=tk.Label(master=frm_from,text='Адрес 1:')
ent_address1=tk.Entry(master=frm_from,width=50)

lbl_address1.grid(row=2,column=0,sticky=tk.E)
ent_address1.grid(row=2,column=1)



win.mainloop()
