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

lbl_address2=tk.Label(master=frm_from,text='Адрес 2:')
ent_address2=tk.Entry(master=frm_from,width=50)

lbl_address2.grid(row=3,column=0,sticky=tk.E)
ent_address2.grid(row=3,column=1)

lbl_city=tk.Label(master=frm_from,text='Город')
ent_city=tk.Entry(master=frm_from,width=50)

lbl_city.grid(row=4,column=0,sticky=tk.E)
ent_city.grid(row=4,column=1)

lbl_postal_code=tk.Label(master=frm_from,text='Почтовый индекс')
ent_postal_code=tk.Entry(master=frm_from,width=50)

lbl_postal_code.grid(row=5,column=0,sticky=tk.E)
ent_postal_code.grid(row=5,column=1)





win.mainloop()
